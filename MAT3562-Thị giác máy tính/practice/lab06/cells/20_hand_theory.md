# PHẦN 3: BÀI 2 - PHÂN ĐOẠN BÀN TAY BẰNG HISTOGRAM BACKPROJECTION VÀ PHÂN NGƯỠNG

### 1. Cơ sở lý thuyết của Histogram Backprojection
- **Ý tưởng cốt lõi:** Cho trước một đối tượng mẫu (ở đây là vùng da tay $I_{roi}$), ta tính histogram phân bố màu của đối tượng mẫu này. Khi muốn tìm đối tượng tương tự trong một bức ảnh lớn $I_{target}$ (hoặc từng khung hình webcam), ta thực hiện **chiếu ngược (backprojection)** histogram mẫu lên ảnh đích:
  - Với mỗi điểm ảnh $(x, y)$ trong ảnh đích có giá trị màu $c(x, y)$, giá trị tại vị trí đó trên ảnh kết quả sẽ bằng xác suất (mật độ) của màu $c(x, y)$ trong histogram mẫu:
$$I_{bp}(x, y) = H_{sample}(c(x, y))$$
  - Điểm ảnh nào có màu sắc trùng khớp cao với mẫu da tay sẽ nhận giá trị xác suất lớn (sáng), còn các điểm ảnh thuộc về nền (không phải da tay) sẽ nhận giá trị xác suất rất bé hoặc bằng $0$ (tối).

### 2. So sánh các không gian màu cho Backprojection: RGB vs HSV
- **Không gian màu RGB:**
  - **2D Red - Green Histogram:** Như bảng ví dụ trong Câu 2 bài học, ta có thể xây dựng histogram 2 chiều trên 2 kênh Red và Green. Vùng da tay người thường có tỷ lệ Red cao hơn hẳn Green và Blue.
  - **3D RGB Histogram:** Tính phân bố đồng thời trên cả 3 kênh $R, G, B$ ($16 \times 16 \times 16$ bins).
- **Không gian màu HSV:**
  - Tách riêng thành **Hue ($H$)** (sắc thái màu), **Saturation ($S$)** (độ bão hòa), và **Value ($V$)** (cường độ sáng).
  - Bỏ qua kênh $V$ giúp thuật toán không bị ảnh hưởng bởi bóng đổ hay thay đổi cường độ sáng môi trường.

### 3. Khảo sát toàn diện các phương pháp phân ngưỡng (Thresholding Methods)
Sau khi có bản đồ xác suất từ Backprojection, chúng ta sẽ thử nghiệm và so sánh **toàn bộ các phương pháp phân ngưỡng phổ biến trong xử lý ảnh**:
1. **Phân ngưỡng nhị phân cố định (Fixed Binary Thresholding):** Quét qua dải ngưỡng $T = 20, 40, 60, 80$.
2. **Phân ngưỡng toàn cục tự động Otsu (`cv2.THRESH_OTSU`):** Tự động tìm ngưỡng tối ưu cực đại hóa phương sai giữa 2 lớp (bàn tay và nền).
3. **Phân ngưỡng toàn cục tự động Triangle (`cv2.THRESH_TRIANGLE`):** Tìm ngưỡng dựa trên khoảng cách hình học cực đại trên biểu đồ histogram đơn đỉnh lệch.
4. **Phân ngưỡng thích nghi cục bộ (Adaptive Thresholding):**
   - **Adaptive Mean (`cv2.ADAPTIVE_THRESH_MEAN_C`)**
   - **Adaptive Gaussian (`cv2.ADAPTIVE_THRESH_GAUSSIAN_C`)**
5. **Phân ngưỡng theo dải màu trực tiếp (`cv2.inRange`):**
   - Phân ngưỡng dải màu trên RGB
   - Phân ngưỡng dải màu trên HSV
