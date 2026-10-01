---
description: "Use when performing data analysis with AI on business datasets. Covers the 6-step Understand/Audit/Plan/Execute/Validate/Communicate process and a checklist to avoid hallucination."
applyTo: "assignments/**,data/**,.github/prompts/**"
---

# 02. Quy trình phân tích dữ liệu với AI

## 6 bước

**1. Understand**: schema, grain, đơn vị, thời gian.  
**2. Audit**: missing, duplicate, invalid values, outliers.  
**3. Plan**: KPI, dimensions, phép so sánh.  
**4. Execute**: code/SQL hoặc phép tính có thể tái lập.  
**5. Validate**: cross-check tổng, mẫu ngẫu nhiên, denominator, edge cases.  
**6. Communicate**: Fact → Interpretation → Business Impact → Action.

## Checklist chống hallucination

- Không tạo cột hoặc số liệu không tồn tại.
- Không gọi tương quan là quan hệ nhân quả.
- Không so sánh % khi mẫu số bằng 0.
- Phân biệt % thay đổi và điểm phần trăm.
- Nêu rõ kỳ so sánh.
- Không gọi một điểm là "bất thường" nếu chưa nêu tiêu chí.
