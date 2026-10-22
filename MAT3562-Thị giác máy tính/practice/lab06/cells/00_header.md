# TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN - ĐHQGHN
## KHOA TOÁN - CƠ - TIN HỌC | BỘ MÔN TIN HỌC
### MÔN HỌC: MAT3562 - THỊ GIÁC MÁY TÍNH (COMPUTER VISION)

---
# BÀI THỰC HÀNH LAB 06: ĐỐI SÁNH HISTOGRAM VÀ HISTOGRAM BACKPROJECTION

**Học viên / Sinh viên thực hiện:** Đạt (datbritget)  
**Mục tiêu bài thực hành:**
1. **Bài 1:** Thực hiện quy trình tra cứu ảnh trên thư mục ảnh $D$ (`thu_muc_anh`) với ảnh truy vấn $Q$ (`ava.jpg`):
   - Thử nghiệm với các lựa chọn khác nhau của giá trị $k$, cấu hình histogram (số bin, không gian màu) và 4 phương pháp đối sánh (Correlation, Chi-Square, Intersection, Bhattacharyya).
   - **Bước 1:** Đối sánh trên ảnh xám (Grayscale).
   - **Bước 2:** Đối sánh trên ảnh màu (Color) với các cấu hình đa chiều (2D HSV, 3D RGB, ghép 3 kênh).
2. **Bài 2:** Phân đoạn bàn tay bằng kỹ thuật Histogram Backprojection kết hợp phân ngưỡng:
   - Học phân bố màu da từ vùng mẫu da tay (Skin ROI) trên không gian màu HSV.
   - Chiếu ngược Histogram Backprojection để tạo bản đồ xác suất (Probability Map).
   - Phân ngưỡng (Thresholding) và xử lý hình thái học (Morphology) để tách trọn vẹn bàn tay khỏi nền.
   - Hỗ trợ xử lý trên ảnh tĩnh `bantay.jpeg`, file video và luồng Webcam thời gian thực.
3. **Quy tắc bắt buộc:** Tất cả các histogram sau khi tính đều được **chuẩn hóa** bằng cách chia các giá trị cho số điểm ảnh của ảnh:
$$\bar{H}[k] = \frac{H[k]}{\text{Height} \times \text{Width}}$$
đảm bảo tổng các giá trị histogram bằng 1.0 và kết quả đối sánh không bị ảnh hưởng bởi độ phân giải của các ảnh.
