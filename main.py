import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import faiss
import aiohttp
from googletrans import Translator
from typing import Any
from contextlib import asynccontextmanager
import json
import re
import torch
from transformers import AutoTokenizer, AutoModel

app = FastAPI()

# --- Khởi tạo PhoBERT ---
tokenizer_phobert = AutoTokenizer.from_pretrained("vinai/phobert-large")
model_phobert = AutoModel.from_pretrained("vinai/phobert-large")
model_phobert.eval()

translator = Translator()

kb_chunks = []
faiss_index = None

def load_kb_chunks(filepath: str):
    """Load and split the knowledge base file into chunks."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    parts = content.split("### ")[1:]
    chunks = ["### " + part.strip() for part in parts]
    return chunks

def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
    sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
    return sum_embeddings / sum_mask

def get_embedding(text: str):
    """Lấy embedding câu tiếng Việt bằng PhoBERT, trả về numpy float32 normalized vector."""
    encoded_input = tokenizer_phobert(text, padding=True, truncation=True, max_length=256, return_tensors='pt')
    with torch.no_grad():
        model_output = model_phobert(**encoded_input)
    sentence_embedding = mean_pooling(model_output, encoded_input['attention_mask'])
    sentence_embedding = torch.nn.functional.normalize(sentence_embedding, p=2, dim=1)
    return sentence_embedding[0].cpu().numpy().astype('float32')

def create_embeddings(chunks):
    embeddings = [get_embedding(c) for c in chunks]
    return np.vstack(embeddings).astype('float32')

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(embeddings)
    return index

async def translate_text(text: str) -> str:
    # Nếu muốn dịch tiếng Việt sang tiếng Anh để test, bỏ comment bên dưới:
    translated = await translator.translate(text, src='vi', dest='en')
    return translated.text
    # return text

async def call_ollama_llama2(question_en: str, kb_chunk: str) -> str:
    prompt = f"""
You are a data analysis assistant.

User question: "{question_en}"

Relevant information:  
{kb_chunk}

Based on the question and the information above, please generate a single JSON for 1 matchest function call object in the following format:
{{
  "functions": [
    {{
      "name": "function_name",
      "parameters": {{
          "parameter1": "Values for parameter 1",
          "parameter2": "Values for parameter 2",
          // Add more parameters as needed
      }}
    }}
  ]
}}

IMPORTANT:  
- Return ONLY one valid JSON object corresponding to a single function call.  
- DO NOT return an array of function calls or multiple functions.  
- DO NOT add any explanations, comments, examples, or extra text.  
- If you cannot produce valid JSON, return an empty string.

Please follow the instructions exactly.
"""

    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "llama2:7b",
        "prompt": prompt,
        "max_tokens": 256,
        "temperature": 0,
        "stream": False
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as resp:
            if resp.status != 200:
                raise HTTPException(status_code=500, detail=f"Ollama API error: {resp.status}")
            response = await resp.json()
            text = response.get("response", "")
            return text.strip()

@asynccontextmanager
async def lifespan(app: FastAPI):
    global kb_chunks, faiss_index
    kb_chunks = load_kb_chunks("function_calling_kb_vi.md")
    embeddings = create_embeddings(kb_chunks)
    faiss_index = build_faiss_index(embeddings)
    print("KB and Faiss index loaded.")
    yield

app = FastAPI(lifespan=lifespan)

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    json_function_call: Any

def clean_json_string(s: str) -> str:
    s = s.replace("```json", "").replace("```", "").strip()
    # Tìm đoạn JSON bắt đầu bằng { và lấy đến cuối string
    match = re.search(r'\{.*', s, re.DOTALL)
    if match:
        json_str = match.group(0)
        # Đếm ngoặc mở và đóng
        open_braces = json_str.count('{')
        close_braces = json_str.count('}')
        # Thêm ngoặc đóng nếu thiếu
        json_str += '}' * (open_braces - close_braces)
        return json_str
    return s

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(req: QuestionRequest):
    global kb_chunks, faiss_index
    question_vi = req.question

    question_en = await translate_text(question_vi)

    q_emb = get_embedding(question_en).reshape(1, -1)
    top_k = 3
    distances, indices = faiss_index.search(q_emb, top_k)
    top_chunks = [kb_chunks[i] for i in indices[0]]

    # In debug các chunk được chọn
    print("DEBUG top_chunks sent to Ollama:")
    for i, chunk in enumerate(top_chunks):
        print(f"Chunk {i+1}:")
        print(chunk)
        print("-" * 40)

    kb_context = "\n\n".join(top_chunks)

    json_call = await call_ollama_llama2(question_vi, kb_context)
    print("DEBUG json_call:", repr(json_call))

    if not json_call:
        raise HTTPException(status_code=500, detail="Empty response from Ollama API")

    cleaned_json_call = clean_json_string(json_call)
    try:
        json_obj = json.loads(cleaned_json_call)
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Invalid JSON from Ollama API after cleaning: {e}")

    return AnswerResponse(
        json_function_call=json_obj
    )