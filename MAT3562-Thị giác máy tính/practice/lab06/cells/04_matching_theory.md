## 2. Cài đặt 4 phương pháp đối sánh Histogram

Theo chuẩn lý thuyết Thị giác máy tính và tài liệu bài giảng, có 4 phương pháp đối sánh histogram cơ bản:

| Phương pháp | Công thức toán học $d(H_1, H_2)$ | Miền giá trị | Tiêu chí tốt nhất |
|---|---|---|---|
| **1. Correlation (Tương quan)** | $\frac{\sum_i (H_1(i) - \bar{H}_1)(H_2(i) - \bar{H}_2)}{\sqrt{\sum_i (H_1(i) - \bar{H}_1)^2 \sum_i (H_2(i) - \bar{H}_2)^2}}$ | $[-1.0, 1.0]$ | **LỚN NHẤT (Max)**: Càng gần $1.0$ càng giống |
| **2. Chi-Square ($\chi^2$)** | $\sum_{i, H_1+H_2>0} \frac{(H_1(i) - H_2(i))^2}{H_1(i) + H_2(i)}$ | $[0.0, +\infty)$ | **NHỎ NHẤT (Min)**: Càng gần $0.0$ càng giống |
| **3. Intersection (Giao cắt)** | $\sum_i \min(H_1(i), H_2(i))$ | $[0.0, 1.0]$ *(với hist chuẩn hóa)* | **LỚN NHẤT (Max)**: Càng gần $1.0$ càng giống |
| **4. Bhattacharyya distance** | $\sqrt{1 - \sum_i \sqrt{H_1(i) \cdot H_2(i)}}$ | $[0.0, 1.0]$ | **NHỎ NHẤT (Min)**: Càng gần $0.0$ càng giống |

*Ghi chú quan trọng:*
- Với **Correlation** và **Intersection**: Điểm số càng cao phản ánh hai histogram càng trùng khít nhau (đối sánh tốt nhất là **LỚN NHẤT**).
- Với **Chi-Square** và **Bhattacharyya**: Đo lường khoảng cách sai khác giữa hai phân bố, khoảng cách bằng $0.0$ nghĩa là đồng nhất hoàn toàn (đối sánh tốt nhất là **NHỎ NHẤT**).
