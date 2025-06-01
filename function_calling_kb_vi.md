### 1. get_total_revenue
- **Mô tả**: Tính tổng doanh thu trong một khoảng thời gian nhất định (tháng, quý, năm)
- **Tham số**:
  - `start_date` (string): Ngày bắt đầu (YYYY-MM-DD)
  - `end_date` (string): Ngày kết thúc (YYYY-MM-DD)
- **Ví dụ sử dụng**:
  ```json
  {
    "name": "get_total_revenue",
    "parameters" {
      "start_date": "YYYY-MM-DD",
      "end_date": "YYYY-MM-DD"
    }
  }
  ```

### 2. get_total_orders
- **Mô tả**: Đếm tổng số đơn hàng trong một khoảng thời gian
- **Tham số**:
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 3. get_avg_profit_by_month
- **Mô tả**: Tính lợi nhuận trung bình theo tháng trong một khoảng thời gian
- **Tham số**:
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 4. compare_revenue
- **Mô tả**: So sánh doanh thu giữa hai khoảng thời gian (tháng, quý, năm)
- **Tham số**:
  - `period1_start` (string)
  - `period1_end` (string)
  - `period2_start` (string)
  - `period2_end` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "period1_start": "YYYY-MM-DD",
    "period1_end": "YYYY-MM-DD",
    "period2_start": "YYYY-MM-DD",
    "period2_end": "YYYY-MM-DD"
  }
  ```

### 5. get_weekly_trend
- **Mô tả**: Truy vấn xu hướng theo tuần cho một chỉ số
- **Tham số**:
  - `metric` (string)
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "metric": "revenue",
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 6. get_quarterly_report
- **Mô tả**: Truy vấn báo cáo theo quý cho một năm
- **Tham số**:
  - `metric` (string)
  - `year` (integer)
- **Ví dụ sử dụng**:
  ```json
  {
    "metric": "sales",
    "year": YYYY
  }
  ```

### 7. get_top_selling_product
- **Mô tả**: Truy vấn sản phẩm bán chạy nhất trong một khoảng thời gian
- **Tham số**:
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 8. get_top_order
- **Mô tả**: Truy vấn đơn hàng có giá trị cao nhất
- **Tham số**:
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 9. compare_revenue_by_branch
- **Mô tả**: So sánh doanh thu giữa các chi nhánh
- **Tham số**:
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 10. get_revenue_by_product
- **Mô tả**: Tính doanh thu theo sản phẩm trong một khoảng thời gian
- **Tham số**:
  - `product_name` (string)
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "product_name": "Product A",
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 11. get_vip_orders
- **Mô tả**: Đếm số đơn hàng của khách VIP
- **Tham số**:
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 12. get_orders_above_value
- **Mô tả**: Lấy danh sách đơn hàng có giá trị trên ngưỡng cho trước
- **Tham số**:
  - `min_value` (number)
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "min_value": 100,
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 13. get_order_detail
- **Mô tả**: Xem chi tiết đơn hàng theo mã đơn
- **Tham số**:
  - `order_id` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "order_id": "ORD123456"
  }
  ```

### 14. get_customer_history
- **Mô tả**: Xem lịch sử mua hàng của khách
- **Tham số**:
  - `customer_id` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "customer_id": "CUST123456"
  }
  ```

### 15. get_products_in_order
- **Mô tả**: Liệt kê sản phẩm trong một đơn hàng
- **Tham số**:
  - `order_id` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "order_id": "ORD123456"
  }
  ```

### 16. get_order_completion_rate
- **Mô tả**: Tính tỷ lệ hoàn thành đơn hàng
- **Tham số**:
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 17. get_roi
- **Mô tả**: Tính ROI của chiến dịch marketing
- **Tham số**:
  - `campaign_id` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "campaign_id": "CAMP123456"
  }
  ```

### 18. get_traffic_stats
- **Mô tả**: Truy vấn thống kê truy cập website theo thời gian
- **Tham số**:
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 19. get_new_customer_count
- **Mô tả**: Đếm số lượng khách hàng mới
- **Tham số**:
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```

### 20. get_customer_segment_report
- **Mô tả**: Truy vấn báo cáo theo phân khúc khách hàng
- **Tham số**:
  - `segment` (string)
  - `start_date` (string)
  - `end_date` (string)
- **Ví dụ sử dụng**:
  ```json
  {
    "segment": "VIP",
    "start_date": "YYYY-MM-DD",
    "end_date": "YYYY-MM-DD"
  }
  ```