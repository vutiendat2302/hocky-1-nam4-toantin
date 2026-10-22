## BÀI 1 - BƯỚC 2: TRA CỨU TRÊN ẢNH MÀU (COLOR HISTOGRAM MATCHING)

Trong ảnh màu, thông tin sắc thái đóng vai trò quyết định giúp phân biệt các đối tượng. Để mô tả phân bố màu sắc, chúng ta xây dựng **3 cấu hình histogram màu** khác nhau:

### 1. Cấu hình A: 2D HSV Histogram (Hue & Saturation)
- Chuyển đổi không gian màu sang **HSV** (Hue - Saturation - Value).
- Tính 2D Histogram trên 2 kênh $H$ (Sắc thái màu, $[0, 180)$) và $S$ (Độ bão hòa màu, $[0, 256)$), thường chọn $18 \times 16 = 288$ bins.
- **Ưu điểm vượt trội:** Loại bỏ kênh $V$ (Value - cường độ sáng), giúp đặc trưng màu sắc **bất biến với sự thay đổi của ánh sáng và bóng đổ**.

### 2. Cấu hình B: 3D RGB Histogram (Joint RGB Distribution)
- Chia đều mỗi kênh $R, G, B$ thành 8 khoảng $\implies 8 \times 8 \times 8 = 512$ bins (đúng theo mô tả mở rộng của bài giảng trong Câu 2).
- Đo lường đồng thời sự kết hợp màu sắc giữa cả 3 kênh.

### 3. Cấu hình C: Concatenated 1D RGB (Ghép 3 kênh màu)
- Tính độc lập 3 histogram chuẩn hóa cho 3 kênh Red, Green, Blue (mỗi kênh 16 bins).
- Nối (concatenate) 3 vector lại thành một vector đặc trưng duy nhất có kích thước $3 \times 16 = 48$ bins.

*Lưu ý:* Cả 3 cấu hình đều được chuẩn hóa bằng cách chia cho tổng số điểm ảnh của ảnh: $\bar{H} = H / (H_{img} \times W_{img})$. Với cấu hình C ghép kênh, chia thêm cho 3 để tổng toàn vector bằng $1.0$.
