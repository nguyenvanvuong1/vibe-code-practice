---
description: "Use when writing or reviewing prompts for business data analysis assignments. Covers the RC-DOT-CVO prompt framework and advanced prompting techniques (decomposition, chaining, critic prompts, schema-first, evidence-first, confidence calibration)."
applyTo: "assignments/**,.github/prompts/**"
---

# 01. Prompt Engineering nâng cao

## Framework RC-DOT-CVO

1. **Role** – AI đóng vai ai?
2. **Context** – bối cảnh doanh nghiệp và người nhận kết quả.
3. **Data** – dữ liệu nào có sẵn, schema, kỳ dữ liệu, đơn vị.
4. **Objective** – quyết định kinh doanh cần hỗ trợ.
5. **Tasks** – các bước cụ thể AI phải thực hiện.
6. **Constraints** – điều AI không được làm; giả định; giới hạn.
7. **Validation** – cách kiểm tra số liệu, công thức, missing/outlier.
8. **Output** – cấu trúc đầu ra.

## Prompt tự kiểm tra

Yêu cầu AI trước khi kết luận phải: liệt kê cột; kiểm tra kiểu dữ liệu; missing/duplicate; xác định KPI tính được; ghi rõ công thức; nêu dữ liệu không đủ; phân biệt fact và suy luận.

## Kỹ thuật nâng cao

- Decomposition: chia nhiệm vụ thành Explore → Clean → Calculate → Validate → Interpret → Recommend.
- Prompt chaining: output bước trước là input bước sau.
- Critic prompt: dùng một lượt AI khác để phản biện kết quả.
- Schema-first: định nghĩa output table/JSON trước khi phân tích.
- Evidence-first: mỗi insight phải có Evidence + Impact + Action.
- Confidence calibration: High/Medium/Low kèm lý do, không dùng confidence vô căn cứ.
