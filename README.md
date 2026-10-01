# AI Vibe Coding – Prompt nâng cao & Phân tích dữ liệu

Repository thực hành dành cho sinh viên học cách dùng AI để phân tích dữ liệu nghiệp vụ bằng prompt có cấu trúc, sinh mã phân tích, kiểm chứng kết quả và trình bày insight.

## Mục tiêu đầu ra

Sau khóa học, sinh viên có thể: (1) thiết kế prompt theo Role–Context–Data–Objective–Tasks–Constraints–Validation–Output; (2) yêu cầu AI khám phá và làm sạch dữ liệu; (3) sinh/đọc/sửa Python hoặc SQL; (4) kiểm chứng phép tính và tránh hallucination; (5) chuyển số liệu thành insight nghiệp vụ; (6) xây dựng workflow Vibe Coding có nhiều bước.

## Cấu trúc

- `.github/instructions/`: kiến thức và quy trình thực hành, tự động nạp cho Copilot khi làm bài trong `assignments/`.
- `.github/prompts/`: prompt mẫu đặt tên theo tiền tố `accounting-`, `business-`, `marketing-`, `general-` (chạy bằng lệnh `/` trong Copilot Chat; các file phải nằm trực tiếp trong thư mục này, không dùng thư mục con, để VS Code nhận diện). Mỗi prompt yêu cầu lưu kết quả vào `output/<tên-prompt>/`.
- `output/`: kết quả (report.md, script.py...) do chạy các prompt mẫu sinh ra, mỗi prompt một thư mục con cùng tên.
- `data/`: dữ liệu giả lập để làm bài.
- `assignments/`: 24 bài tập + 3 capstone.
- `docs/teacher/`: rubric, đáp án định hướng và checklist chấm bài.

## Quy trình mỗi bài

1. Đọc đề, không xem prompt mẫu ngay.
2. Viết Prompt V1 và lưu vào bài nộp.
3. Chạy với AI, lưu output/ảnh chụp hoặc transcript.
4. Ghi lỗi/hạn chế của V1.
5. Viết Prompt V2/V3 để cải thiện.
6. Yêu cầu AI tạo code/SQL khi phù hợp.
7. Kiểm chứng ít nhất 3 số liệu bằng cách tính độc lập hoặc code.
8. Viết kết luận nghiệp vụ, tách rõ Fact / Interpretation / Recommendation.

## Bài nộp chuẩn

```text
submission/<student-id>/<assignment-id>/
├── prompt-v1.md
├── prompt-final.md
├── analysis.md
├── code/                 # nếu có
└── reflection.md
```

## Quy tắc dùng AI

Không chấm điểm cao cho câu trả lời chỉ “nghe hợp lý”. Sinh viên phải chỉ ra dữ liệu nào hỗ trợ kết luận, công thức nào được dùng, giả định nào được đặt ra và cách kiểm chứng.
