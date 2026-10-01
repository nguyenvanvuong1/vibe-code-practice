---
description: "Sample prompt requiring the AI to write and run a Python script that audits a dataset (schema, missing values, duplicates, outliers) before any analysis begins."
---

# Prompt mẫu – Viết Python script kiểm tra dữ liệu

```text
Trước khi phân tích, hãy viết một Python script (dùng pandas) để kiểm tra dữ liệu trong file tôi cung cấp. Script phải:
1. Đọc file và in ra shape, dtypes, tên cột.
2. Đếm missing value và duplicate rows theo từng cột.
3. Phát hiện outlier cho các cột số (IQR hoặc z-score), in ra số lượng và ví dụ.
4. Kiểm tra giá trị âm/0 bất thường ở các cột không nên âm (ví dụ số lượng, giá, ngày).
5. In ra bảng tóm tắt "data quality report" gồm: column | issue | count | example.

Chạy script và cho tôi xem kết quả thật, không bịa số liệu.
Không tự sửa dữ liệu gốc. Nếu phát hiện vấn đề, chỉ in cảnh báo và đề xuất cách xử lý; không tự động drop hoặc fill dữ liệu trừ khi tôi xác nhận.
Sau khi chạy xong, tóm tắt 3 rủi ro dữ liệu lớn nhất trước khi tiến hành phân tích tiếp theo.
Lưu script vào `output/general-python-data-audit/script.py` và data quality report vào `output/general-python-data-audit/report.md`.
```
