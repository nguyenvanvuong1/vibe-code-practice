---
description: "Use when running a multi-step Vibe Coding workflow with AI (Inspect, Plan, Generate code, Run, Read errors, Fix, Validate, Explain, Report) for assignments or capstone projects."
applyTo: "assignments/**,.github/prompts/**"
---

# 03. Vibe Coding Workflow

Sinh viên không chỉ hỏi AI "hãy phân tích file". Workflow chuẩn:

`Inspect → Plan → Generate code → Run → Read errors → Fix → Validate → Explain → Report`

## Prompt điều phối mẫu

```text
Không phân tích ngay. Trước tiên hãy đọc schema và đề xuất kế hoạch phân tích.
Sau khi tôi xác nhận kế hoạch, hãy tạo code theo từng bước nhỏ.
Mỗi bước phải cho biết input, output mong đợi và phép kiểm tra.
Nếu code lỗi, giải thích nguyên nhân trước khi sửa.
Không thay đổi dữ liệu gốc âm thầm.
```

## Nhật ký bắt buộc

Sinh viên ghi: prompt ban đầu; lỗi AI; thay đổi prompt; lỗi code; cách sửa; số liệu đã kiểm chứng; điều học được.
