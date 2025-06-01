# Function Calling Knowledge Base

## Overview
This knowledge base provides detailed documentation for the function calling schemas defined in the `function_calling_schemas.json` file. Each function is designed to facilitate operations related to revenue, orders, and customer data, allowing for efficient data retrieval and analysis.

### Date Format:

- All dates must be in ISO 8601 format: `YYYY-MM-DD`
- The `start_date` is inclusive (the first day of the period)
- The `end_date` is inclusive (the last day of the period)

### Notes:

- When user queries mention a quarter, month, or year, map the dates to the full exact range accordingly.
- For ambiguous time references, prefer to cover the entire reasonable range.
- Ensure date ranges accurately reflect calendar rules, including leap years for February.

---

## Function Schemas

### 1. get_total_revenue
- **Description**: Calculate total revenue within a specific time period
- **Parameters**:
  - `start_date` (string): Start date (YYYY-MM-DD)
  - `end_date` (string): End date (YYYY-MM-DD)
- **Usage Example**:
  ```json
  {
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 2. get_total_orders
- **Description**: Count total number of orders within a specific time period
- **Parameters**:
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 3. get_avg_profit_by_month
- **Description**: Calculate average profit by month within a specific time period
- **Parameters**:
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "start_date": "2023-01-01",
    "end_date": "2023-12-31"
  }
  ```

### 4. compare_revenue
- **Description**: Compare revenue between two time periods
- **Parameters**:
  - `period1_start` (string)
  - `period1_end` (string)
  - `period2_start` (string)
  - `period2_end` (string)
- **Usage Example**:
  ```json
  {
    "period1_start": "2023-01-01",
    "period1_end": "2023-01-31",
    "period2_start": "2023-02-01",
    "period2_end": "2023-02-28"
  }
  ```

### 5. get_weekly_trend
- **Description**: Query weekly trend for a metric
- **Parameters**:
  - `metric` (string)
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "metric": "revenue",
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 6. get_quarterly_report
- **Description**: Query quarterly report for a year
- **Parameters**:
  - `metric` (string)
  - `year` (integer)
- **Usage Example**:
  ```json
  {
    "metric": "sales",
    "year": 2023
  }
  ```

### 7. get_top_selling_product
- **Description**: Query top selling product within a specific time period
- **Parameters**:
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 8. get_top_order
- **Description**: Query the highest value order
- **Parameters**:
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 9. compare_revenue_by_branch
- **Description**: Compare revenue between branches
- **Parameters**:
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 10. get_revenue_by_product
- **Description**: Calculate revenue by product within a specific time period
- **Parameters**:
  - `product_name` (string)
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "product_name": "Product A",
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 11. get_vip_orders
- **Description**: Count the number of VIP customer orders
- **Parameters**:
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 12. get_orders_above_value
- **Description**: Get list of orders with value above a given threshold
- **Parameters**:
  - `min_value` (number)
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "min_value": 100,
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 13. get_order_detail
- **Description**: View order details by order ID
- **Parameters**:
  - `order_id` (string)
- **Usage Example**:
  ```json
  {
    "order_id": "ORD123456"
  }
  ```

### 14. get_customer_history
- **Description**: View purchase history of a customer
- **Parameters**:
  - `customer_id` (string)
- **Usage Example**:
  ```json
  {
    "customer_id": "CUST123456"
  }
  ```

### 15. get_products_in_order
- **Description**: List products in an order
- **Parameters**:
  - `order_id` (string)
- **Usage Example**:
  ```json
  {
    "order_id": "ORD123456"
  }
  ```

### 16. get_order_completion_rate
- **Description**: Calculate order completion rate
- **Parameters**:
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 17. get_roi
- **Description**: Calculate ROI of a marketing campaign
- **Parameters**:
  - `campaign_id` (string)
- **Usage Example**:
  ```json
  {
    "campaign_id": "CAMP123456"
  }
  ```

### 18. get_traffic_stats
- **Description**: Query website traffic statistics by time period
- **Parameters**:
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 19. get_new_customer_count
- **Description**: Count the number of new customers
- **Parameters**:
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

### 20. get_customer_segment_report
- **Description**: Query report by customer segment
- **Parameters**:
  - `segment` (string)
  - `start_date` (string)
  - `end_date` (string)
- **Usage Example**:
  ```json
  {
    "segment": "VIP",
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
  }
  ```

## Conclusion
This knowledge base serves as a comprehensive guide for utilizing the function calling schemas effectively. Each function is designed to streamline data operations, providing users with the necessary tools to analyze and retrieve relevant information efficiently.