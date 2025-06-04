import json
import subprocess

def call_llama2(prompt):
    result = subprocess.run(
        ['ollama', 'generate', '--model', 'llama2', '--prompt', prompt],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode()

# Câu hỏi từ người dùng
user_question = "Tính tổng doanh thu trong tháng 2/2025"

# System prompt cho Llama2
prompt = f"""
Bạn là một trợ lý AI chuyên phân tích câu hỏi và chuyển chúng thành các function call với tham số chính xác. Dưới đây là các hàm có sẵn:
1. get_total_revenue: Tính tổng doanh thu trong khoảng thời gian. Tham số: start_date (YYYY-MM-DD), end_date (YYYY-MM-DD).
2. get_total_orders: Đếm tổng số đơn hàng trong khoảng thời gian. Tham số: start_date (YYYY-MM-DD), end_date (YYYY-MM-DD).
3. get_avg_profit_by_month: Tính lợi nhuận trung bình theo tháng trong khoảng thời gian. Tham số: start_date (YYYY-MM-DD), end_date (YYYY-MM-DD).
...

Câu hỏi: "{user_question}"
Vui lòng trả lời dưới dạng JSON chứa tên function và các tham số (nếu có).
"""

# Gọi Llama2 để phân tích câu hỏi
response = call_llama2(prompt)
response_data = json.loads(response)

# In kết quả
print(response_data)
