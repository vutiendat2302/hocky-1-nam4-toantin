# PHẦN 4: TỔNG KẾT VÀ BÀI HỌC KINH NGHIỆM

Qua toàn bộ quá trình thực nghiệm trong bài thực hành Lab 06, chúng ta rút ra các kết luận quan trọng sau:

### 1. Vai trò của Chuẩn hóa Histogram:
- Việc chia tất cả các giá trị histogram cho số điểm ảnh của ảnh ($\text{Height} \times \text{Width}$) biến histogram thành **hàm mật độ xác suất (PMF)** với tổng bằng $1.0$.
- Chuẩn hóa là bước bắt buộc trong xử lý ảnh thực tế, giúp loại bỏ hoàn toàn sự thiên lệch do kích thước ảnh gây ra, cho phép so sánh công bằng giữa các ảnh chụp ở các độ phân giải khác nhau.

### 2. So sánh 4 phương pháp đối sánh Histogram:
- **Intersection (Giao cắt):** Trực quan, dễ hiểu, tính toán rất nhanh. Đo lường phần diện tích trùng nhau của 2 histogram. Giá trị trong $[0, 1]$, càng lớn càng tương đồng.
- **Bhattacharyya distance:** Dựa trên nền tảng lý thuyết xác suất thống kê vững chắc, đo độ trùng lặp giữa 2 phân bố xác suất thông qua căn bậc hai $\sqrt{H_1 \cdot H_2}$. Cho kết quả đối sánh cực kỳ ổn định, ít bị nhiễu. Giá trị trong $[0, 1]$, càng nhỏ càng tương đồng.
- **Chi-Square ($\chi^2$):** Phạt rất nặng các bin có sự sai lệch lớn. Càng nhỏ càng tốt.
- **Correlation (Tương quan):** Đo mức độ biến thiên đồng điệu xung quanh giá trị trung bình. Càng gần $1.0$ càng tốt.

### 3. So sánh các không gian màu (RGB vs HSV) trong Backprojection:
- **2D Red - Green (RG):** Bắt đúng đặc tính da người có sắc tố đỏ cao hơn lục ($R > G$). Hoạt động tốt khi nền có màu lạnh hoặc trắng, nhưng dễ nhầm lẫn nếu nền có màu gỗ hoặc vàng/cam.
- **3D RGB (R-G-B):** Tận dụng toàn diện thông tin 3 kênh, nhận diện chính xác nhưng đòi hỏi ma trận 3 chiều lớn ($16^3 = 4096$ bins) và dễ gặp hiện tượng thưa bin.
- **2D HSV (H-S):** Tối ưu và ổn định nhất do **bỏ qua kênh độ sáng $V$**, giúp thuật toán bất biến với sự thay đổi cường độ ánh sáng môi trường và bóng đổ trên bàn tay.

### 4. Đánh giá toàn diện các phương pháp phân ngưỡng (Thresholding):
- **Phân ngưỡng nhị phân cố định ($T = 40 \to 60$):** Cho kết quả rất cân bằng, tách trọn vẹn bàn tay và sạch nền.
- **Otsu ($T \approx 119$):** Tự động tìm ngưỡng dựa trên tối ưu phương sai giữa 2 lớp. Kết quả rất sạch nền, tuy nhiên có xu hướng cắt hơi sát vào rìa ngón tay.
- **Triangle ($T \approx 2$):** Rất nhạy, giữ lại tối đa các chi tiết da ở biên ngón tay, nhưng có thể để lại một ít viền mờ.
- **Adaptive Thresholding (Mean / Gaussian):** **Không phù hợp** cho bản đồ xác suất có vùng nền $0$ rộng lớn, vì thuật toán coi sự chênh lệch nhỏ tại vùng nền phẳng là cạnh biên và bật trắng phần lớn nền. Adaptive thresholding chỉ phát huy tác dụng tốt trên ảnh tài liệu chữ viết có ánh sáng không đều.
- **Color Range Thresholding (`inRange` RGB / HSV):** Hoạt động nhanh nhưng đường biên thô, không mượt mà bằng việc kết hợp **Backprojection + Convolution đĩa elip + Thresholding + Morphology**.

### 5. Xử lý thời gian thực trên Video / Webcam:
- Kết hợp Histogram Backprojection với xử lý hình thái học (Closing lấp lỗ hổng, Opening triệt tiêu nhiễu) cho phép nhận diện và tách bàn tay cực kỳ ổn định với tốc độ vượt 30 FPS trên video và Webcam thời gian thực.
