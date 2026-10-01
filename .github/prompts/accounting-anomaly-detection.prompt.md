---
description: "Sample prompt for accounting anomaly detection in transaction data (IQR/z-score, business thresholds, duplicate detection)."
---

# Prompt mẫu – Phát hiện bất thường kế toán

```text
Hãy đề xuất ít nhất 3 tiêu chí phát hiện giao dịch bất thường (ví dụ IQR/z-score, ngưỡng nghiệp vụ, giao dịch lặp). Chạy từng tiêu chí riêng, giải thích vì sao bị gắn cờ. Không gọi giao dịch là gian lận; chỉ gọi là "cần kiểm tra". Xuất bảng transaction_id | rule | evidence | priority | suggested_check.
Lưu kết quả (bảng + giải thích) vào `output/accounting-anomaly-detection/report.md`, và code/script (nếu có) vào `output/accounting-anomaly-detection/script.py`.
```
