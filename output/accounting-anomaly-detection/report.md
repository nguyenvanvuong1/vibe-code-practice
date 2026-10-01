# Phát hiện giao dịch kế toán cần kiểm tra

**Nguồn dữ liệu:** [data/accounting/transactions.csv](../../data/accounting/transactions.csv) — 180 giao dịch, kỳ 2026-01-01 → 2026-09-26.
**Lưu ý:** Các giao dịch dưới đây chỉ **"cần kiểm tra"**, không phải kết luận gian lận. Đây là kết quả sàng lọc tự động dựa trên quy tắc thống kê/nghiệp vụ, cần người kiểm soát nội bộ xác minh bằng chứng từ gốc trước khi kết luận.

## 3 tiêu chí áp dụng

### 1. IQR outlier theo loại giao dịch (type)

Tính Q1, Q3, IQR riêng cho nhóm `Revenue` và `Expense` (hai nhóm có quy mô khác nhau nên không gộp chung). Giao dịch có `amount` nằm ngoài khoảng `[Q1 − 1.5×IQR, Q3 + 1.5×IQR]` bị gắn cờ. Đây là quy tắc thống kê chuẩn để phát hiện giá trị cực đoan so với phần còn lại của cùng nhóm.

### 2. Ngưỡng nghiệp vụ: giao dịch tiền mặt (Cash) lớn

Giao dịch `payment_method = Cash` có `amount > 10,000` bị gắn cờ. Ngưỡng 10,000 không lấy từ phân vị của bộ dữ liệu này mà dựa trên thông lệ kiểm soát tiền mặt phổ biến (tương tự ngưỡng báo cáo giao dịch tiền mặt lớn trong AML) — giao dịch tiền mặt lớn luôn khó xác minh nguồn gốc/người nhận hơn chuyển khoản hay thẻ, nên cần soát xét bất kể có "bất thường" về mặt thống kê hay không. Vì vậy quy tắc này chủ động gắn cờ nhiều giao dịch hơn hai quy tắc còn lại — đó là kỳ vọng của một kiểm soát phòng ngừa (preventive control), không phải lỗi của mô hình.

### 3. Trùng ngày + phòng ban + loại giao dịch

Nhóm giao dịch theo `(date, department, type)`; nếu một tổ hợp xuất hiện từ 2 lần trở lên, mọi giao dịch trong nhóm bị gắn cờ. Đây là dấu hiệu khả nghi cho việc một bút toán bị ghi hai lần (duplicate entry) hoặc bị tách làm nhiều phần (split transaction) để né ngưỡng phê duyệt. Lưu ý: không có cặp giao dịch nào trùng khớp _amount_ tuyệt đối trong dữ liệu này, nên quy tắc dùng tổ hợp ngày/phòng ban/loại thay vì so khớp số tiền chính xác.

## Kết quả tổng hợp

| Rule                                                      | Số giao dịch bị gắn cờ |
| --------------------------------------------------------- | ---------------------- |
| Ngưỡng nghiệp vụ (Cash lớn)                               | 24                     |
| Trùng ngày + phòng ban + loại                             | 8                      |
| IQR outlier (theo type)                                   | 2                      |
| **Tổng cộng (có thể trùng transaction_id giữa các rule)** | 34                     |

## Bảng chi tiết

| transaction_id | rule                        | evidence                                                                                             | priority | suggested_check                                                                     |
| -------------- | --------------------------- | ---------------------------------------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------- |
| TX0010         | Ngưỡng nghiệp vụ (Cash lớn) | amount=13064.01, payment_method=Cash, ngưỡng=10000.00                                                | High     | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0036         | Ngưỡng nghiệp vụ (Cash lớn) | amount=13628.59, payment_method=Cash, ngưỡng=10000.00                                                | High     | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0037         | IQR outlier (theo type)     | amount=81601.44, type=Revenue, ngưỡng trên=22155.53 (Q1=4025.30, Q3=11277.39, IQR=7252.09)           | High     | Đối chiếu chứng từ gốc và người phê duyệt cho giao dịch giá trị bất thường          |
| TX0079         | Ngưỡng nghiệp vụ (Cash lớn) | amount=13217.06, payment_method=Cash, ngưỡng=10000.00                                                | High     | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0121         | IQR outlier (theo type)     | amount=92960.16, type=Revenue, ngưỡng trên=22155.53 (Q1=4025.30, Q3=11277.39, IQR=7252.09)           | High     | Đối chiếu chứng từ gốc và người phê duyệt cho giao dịch giá trị bất thường          |
| TX0152         | Ngưỡng nghiệp vụ (Cash lớn) | amount=13673.31, payment_method=Cash, ngưỡng=10000.00                                                | High     | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0174         | Ngưỡng nghiệp vụ (Cash lớn) | amount=13272.28, payment_method=Cash, ngưỡng=10000.00                                                | High     | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0003         | Trùng ngày+phòng ban+loại   | date=2026-02-17, department=Operations, type=Revenue, amount=7827.65, cùng nhóm với TX0177 (7190.99) | Medium   | Xác minh đây có phải hai bút toán độc lập hay một giao dịch bị tách/ghi lặp hai lần |
| TX0004         | Trùng ngày+phòng ban+loại   | date=2026-04-12, department=IT, type=Revenue, amount=7013.53, cùng nhóm với TX0159 (8396.15)         | Medium   | Xác minh đây có phải hai bút toán độc lập hay một giao dịch bị tách/ghi lặp hai lần |
| TX0038         | Ngưỡng nghiệp vụ (Cash lớn) | amount=11876.98, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0039         | Ngưỡng nghiệp vụ (Cash lớn) | amount=10055.25, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0048         | Ngưỡng nghiệp vụ (Cash lớn) | amount=10097.13, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0071         | Ngưỡng nghiệp vụ (Cash lớn) | amount=10170.53, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0073         | Ngưỡng nghiệp vụ (Cash lớn) | amount=11180.18, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0082         | Trùng ngày+phòng ban+loại   | date=2026-03-01, department=IT, type=Expense, amount=3256.14, cùng nhóm với TX0171 (12461.44)        | Medium   | Xác minh đây có phải hai bút toán độc lập hay một giao dịch bị tách/ghi lặp hai lần |
| TX0085         | Ngưỡng nghiệp vụ (Cash lớn) | amount=10936.44, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0091         | Ngưỡng nghiệp vụ (Cash lớn) | amount=10053.34, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0101         | Ngưỡng nghiệp vụ (Cash lớn) | amount=11283.00, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0102         | Ngưỡng nghiệp vụ (Cash lớn) | amount=12678.01, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0106         | Trùng ngày+phòng ban+loại   | date=2026-03-20, department=Operations, type=Revenue, amount=6515.58, cùng nhóm với TX0120 (7366.64) | Medium   | Xác minh đây có phải hai bút toán độc lập hay một giao dịch bị tách/ghi lặp hai lần |
| TX0109         | Ngưỡng nghiệp vụ (Cash lớn) | amount=12875.00, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0111         | Ngưỡng nghiệp vụ (Cash lớn) | amount=10198.67, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0120         | Trùng ngày+phòng ban+loại   | date=2026-03-20, department=Operations, type=Revenue, amount=7366.64, cùng nhóm với TX0106 (6515.58) | Medium   | Xác minh đây có phải hai bút toán độc lập hay một giao dịch bị tách/ghi lặp hai lần |
| TX0124         | Ngưỡng nghiệp vụ (Cash lớn) | amount=10609.30, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0134         | Ngưỡng nghiệp vụ (Cash lớn) | amount=10667.16, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0142         | Ngưỡng nghiệp vụ (Cash lớn) | amount=11209.77, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0143         | Ngưỡng nghiệp vụ (Cash lớn) | amount=12573.11, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0150         | Ngưỡng nghiệp vụ (Cash lớn) | amount=12261.56, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0156         | Ngưỡng nghiệp vụ (Cash lớn) | amount=10495.88, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0159         | Trùng ngày+phòng ban+loại   | date=2026-04-12, department=IT, type=Revenue, amount=8396.15, cùng nhóm với TX0004 (7013.53)         | Medium   | Xác minh đây có phải hai bút toán độc lập hay một giao dịch bị tách/ghi lặp hai lần |
| TX0168         | Ngưỡng nghiệp vụ (Cash lớn) | amount=12937.13, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0169         | Ngưỡng nghiệp vụ (Cash lớn) | amount=10107.46, payment_method=Cash, ngưỡng=10000.00                                                | Medium   | Yêu cầu biên lai/chứng từ thu chi tiền mặt và xác minh người nhận/người chi         |
| TX0171         | Trùng ngày+phòng ban+loại   | date=2026-03-01, department=IT, type=Expense, amount=12461.44, cùng nhóm với TX0082 (3256.14)        | Medium   | Xác minh đây có phải hai bút toán độc lập hay một giao dịch bị tách/ghi lặp hai lần |
| TX0177         | Trùng ngày+phòng ban+loại   | date=2026-02-17, department=Operations, type=Revenue, amount=7190.99, cùng nhóm với TX0003 (7827.65) | Medium   | Xác minh đây có phải hai bút toán độc lập hay một giao dịch bị tách/ghi lặp hai lần |

_(Bảng đầy đủ cũng được lưu dưới dạng CSV tại [flags.csv](./flags.csv) để tiện lọc/sort.)_

## Giải thích vì sao từng loại bị gắn cờ

- **TX0037, TX0121 (IQR outlier):** amount lần lượt là 81,601.44 và 92,960.16 — gấp hơn 7–8 lần Q3 của nhóm Revenue (11,277.39) và vượt xa ngưỡng trên IQR (22,155.53). Đây là hai điểm dữ liệu cách biệt rõ rệt so với 178 giao dịch còn lại, phù hợp với ghi chú trong [data/README.md](../../data/README.md) rằng bộ dữ liệu có "một số giá trị lớn cố ý".
- **24 giao dịch Cash > 10,000:** đều là giao dịch hợp lệ về mặt thống kê (nằm trong khoảng phân phối bình thường của dữ liệu), nhưng vi phạm ngưỡng kiểm soát tiền mặt — đây là lý do số lượng gắn cờ cao hơn hẳn hai rule kia. Priority High dành cho các giao dịch vượt ngưỡng ≥ 30% (amount > 13,000).
- **8 giao dịch trùng ngày/phòng ban/loại (4 cặp):** TX0003–TX0177, TX0004–TX0159, TX0082–TX0171, TX0106–TX0120. Không có cặp nào trùng số tiền tuyệt đối, nên đây là tín hiệu yếu hơn (priority Medium) — cần kiểm tra thủ công để loại trừ khả năng trùng ngẫu nhiên.

## Giới hạn & cảnh báo

- Dữ liệu chỉ có 180 dòng nên IQR có thể nhạy với mẫu nhỏ; nên tái đánh giá ngưỡng khi có thêm dữ liệu.
- Ngưỡng Cash 10,000 là quy tắc chính sách cố định, không tự học từ dữ liệu — cần đối chiếu với chính sách kiểm soát nội bộ thực tế của doanh nghiệp.
- Không có `receivables.csv` hay thông tin đối tác/khách hàng trong `transactions.csv`, nên không thể kiểm tra chéo với bên thứ ba — tất cả kết quả trên chỉ ở mức sàng lọc sơ bộ.
- Tất cả nhãn đều là **"cần kiểm tra"**, không phải **"gian lận"**.
