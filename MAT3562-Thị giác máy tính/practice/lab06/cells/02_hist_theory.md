## 1. Cơ sở lý thuyết: Tính Histogram và Chuẩn hóa

### 1.1. Khái niệm Histogram
- **Histogram mức xám** là đồ thị thống kê số lượng điểm ảnh (pixel) xuất hiện tương ứng với mỗi mức xám (hoặc khoảng mức xám) trong ảnh.
- Khi chia dải mức xám $[0, 255]$ thành $n$ khoảng (bins), bước nhảy khoảng là $t = \frac{256}{n}$. Khoảng thứ $k$ ($0 \le k < n$) sẽ bao gồm các mức xám từ $[\lceil t \cdot k \rceil, \lceil t \cdot (k+1) \rceil - 1]$.

### 1.2. Chuẩn hóa Histogram (Normalization) - Yêu cầu cốt lõi
- **Tại sao cần chuẩn hóa?** Trong thực tế, các bức ảnh có thể có kích thước (chiều cao $\times$ chiều rộng) hoàn toàn khác nhau. Nếu chỉ dùng số đếm pixel thô, một bức ảnh lớn sẽ luôn có giá trị histogram vượt trội so với ảnh nhỏ, làm sai lệch hoàn toàn quá trình đối sánh độ tương đồng.
- **Công thức chuẩn hóa:** Chia mỗi giá trị trong histogram cho tổng số điểm ảnh của ảnh:
$$\bar{H}[k] = \frac{H[k]}{H_{img} \times W_{img}}$$
Khi đó:
$$\sum_{k=0}^{n-1} \bar{H}[k] = 1.0$$
Histogram chuẩn hóa chính là **hàm mật độ xác suất (Probability Mass Function - PMF)** của mức xám trong ảnh, hoàn toàn độc lập với kích thước ảnh.
