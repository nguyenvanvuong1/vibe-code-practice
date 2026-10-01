---
description: "Sample prompt for marketing customer acquisition analysis by source/channel/cohort, with guardrails against fabricating CAC/LTV."
---

# Prompt mẫu – Khách hàng marketing

```text
Phân tích customer acquisition theo source/channel, cohort hoặc segment nếu dữ liệu cho phép. Xác định dữ liệu cần thiết để tính CAC/LTV chính xác. Nếu thiếu retention hoặc gross margin thì không tạo LTV giả; hãy ghi "không đủ dữ liệu" và đề xuất schema bổ sung.
Lưu kết quả vào `output/marketing-customer-analysis/report.md`, và code/script (nếu có) vào `output/marketing-customer-analysis/script.py`.
```
