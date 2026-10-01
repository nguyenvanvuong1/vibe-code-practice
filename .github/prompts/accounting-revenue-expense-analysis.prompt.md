---
description: "Sample prompt for revenue/expense/profit analysis by month and department, with KPI formulas and self-check questions."
---

# Prompt mẫu – Doanh thu, chi phí, lợi nhuận

```text
Bạn là chuyên viên kế toán quản trị. Hãy phân tích dataset giao dịch tôi cung cấp.
Mục tiêu: giúp Kế toán trưởng hiểu biến động doanh thu, chi phí và lợi nhuận.
Trước khi tính toán: kiểm tra schema, missing, duplicate, giá trị âm và kỳ dữ liệu.
Tính doanh thu, chi phí, lợi nhuận và biên lợi nhuận theo tháng/phòng ban.
Mỗi insight phải có: Fact | Evidence | Interpretation | Recommended check/action.
Không suy diễn nguyên nhân nếu dataset không chứa bằng chứng. Ghi rõ công thức KPI.
Cuối cùng tạo 5 câu hỏi kiểm tra ngược kết quả phân tích.
Lưu kết quả vào `output/accounting-revenue-expense-analysis/report.md`, và code/script (nếu có) vào `output/accounting-revenue-expense-analysis/script.py`.
```
