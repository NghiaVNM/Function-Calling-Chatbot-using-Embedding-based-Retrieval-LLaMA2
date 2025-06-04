from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
import re
from googletrans import Translator  # Thêm thư viện dịch

# Định nghĩa các hàm cần sử dụng trong Langchain (các hàm này chỉ để mô phỏng, bạn sẽ thay thế chúng bằng các logic thực tế của bạn)
def get_total_revenue(start_date, end_date):
    return 1000  # Kết quả ví dụ

def get_total_orders(start_date, end_date):
    return 150  # Kết quả ví dụ

def get_avg_profit_by_month(start_date, end_date):
    return 500  # Kết quả ví dụ

# Định nghĩa các tools (20 schemas)
tools = [
    Tool(name="get_total_revenue", func=get_total_revenue, description="Tính tổng doanh thu trong một khoảng thời gian"),
    Tool(name="get_total_orders", func=get_total_orders, description="Đếm tổng số đơn hàng trong một khoảng thời gian"),
    Tool(name="get_avg_profit_by_month", func=get_avg_profit_by_month, description="Tính lợi nhuận trung bình theo tháng trong một khoảng thời gian"),
    # Các tool khác theo mẫu trên
]

# Hàm dịch câu hỏi từ tiếng Việt sang tiếng Anh
async def translate_to_english(question):
    translator = Translator()
    translation = await translator.translate(question, src='vi', dest='en')  # Dịch bất đồng bộ
    print(f"Translated Question: {translation.text}")  # In câu hỏi đã dịch
    return translation.text

# Hàm xử lý và xác định function từ câu hỏi
async def process_user_question_with_llama(question):
    # Dịch câu hỏi sang tiếng Anh trước khi gửi cho Llama2
    question_in_english = await translate_to_english(question)

    # Khởi tạo mô hình Llama2
    llama_model = OllamaLLM(model="llama2:7b")  # Chỉ định mô hình Llama2

    # Cập nhật prompt để yêu cầu Llama2 chỉ trả về một function duy nhất
    prompt = f"""
    You are an assistant capable of understanding business-related calculations, including total revenue, orders, and profit.
    Here are the available functions:
    1. `get_total_revenue(start_date, end_date)` - Calculate total revenue for the given date range.
    2. `get_total_orders(start_date, end_date)` - Count total orders for the given date range.
    3. `get_avg_profit_by_month(start_date, end_date)` - Calculate average profit per month for the given date range.

    User's question: {question_in_english}

    Based on the user's question, determine the most appropriate function and parameters to use. Please only return the function and parameters in the format:
    `get_total_revenue(start_date='YYYY-MM-DD', end_date='YYYY-MM-DD')`
    Do not provide any additional explanation or results. Ensure that only one function is returned.
    """

    # Gửi prompt đến Llama2 và nhận câu trả lời
    response = llama_model.invoke(prompt)  # Không cần await nữa vì invoke là đồng bộ

    # Kiểm tra xem Llama2 trả về chuỗi (string)
    if isinstance(response, str):
        print(f"Response from Llama2: {response}")

        # Trích xuất function và parameters từ câu trả lời trả về của Llama2
        # Sửa regex để nhận diện function bất kể chữ hoa hay thường
        match = re.search(r"(get_total_revenue|get_total_orders|get_avg_profit_by_month)\(start_date='(\d{4}-\d{2}-\d{2})', end_date='(\d{4}-\d{2}-\d{2})'\)", response, re.IGNORECASE)
        if match:
            function_name = match.group(1).lower()  # Chuyển tên function về chữ thường
            start_date = match.group(2)
            end_date = match.group(3)

            return {
                "function": function_name,
                "parameters": {
                    "start_date": start_date,
                    "end_date": end_date
                }
            }
        else:
            print("Could not extract function and parameters.")
            return None
    else:
        print("Llama2 returned a response that is not a string.")
        return None

# Hàm để trích xuất function và parameters từ câu hỏi
async def extract_function_and_params(question):
    # Dùng Llama2 để hiểu câu hỏi của người dùng
    response = await process_user_question_with_llama(question)

    if response:
        # Trả về function và parameters
        return response
    else:
        print("Could not extract function and parameters.")
        return None

# Tiến hành tiếp nhận câu hỏi người dùng và xử lý
async def interact_with_user():
    while True:
        user_question = input("Please enter your question (or 'exit' to quit): ")
        if user_question.lower() == "exit":
            print("Exiting the program.")
            break

        # Extract function and parameters from the user's question
        extracted_data = await extract_function_and_params(user_question)

        if extracted_data:
            # Print the extracted function and parameters
            print(f"Function: {extracted_data['function']}, Parameters: {extracted_data['parameters']}")

            # Call the appropriate tool with the extracted parameters
            result = call_function(extracted_data['function'], extracted_data['parameters'])
            print(f"Result: {result}")
        else:
            print("Could not extract information from the question.")

# Hàm để gọi hàm thực tế từ các tools
def call_function(function_name, parameters):
    for tool in tools:
        if tool.name == function_name:
            return tool.func(**parameters)

# Start interacting with the user
import asyncio
asyncio.run(interact_with_user())  # Chạy tương tác bất đồng bộ
