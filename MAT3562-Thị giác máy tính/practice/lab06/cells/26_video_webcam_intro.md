## BÀI 2 - MỞ RỘNG: XỬ LÝ TRÊN VIDEO VÀ WEBCAM THỜI GIAN THỰC

### Thiết kế chương trình xử lý thời gian thực:
- **Nguồn đầu vào linh hoạt:** Hàm `phan_doan_ban_tay_video_webcam` hỗ trợ cả 2 chế độ:
  1. **Webcam trực tiếp:** `nguon_video = 0` (mở camera mặc định của máy tính).
  2. **File video:** `nguon_video = "../lab04/video.mp4"` (đọc file video đã ghi sẵn).
- **Cơ chế học màu da:**
  - Mặc định sử dụng vùng mẫu da đã học từ `da_tay.jpeg`.
  - Ngoài ra, người dùng có thể giơ tay vào khung ngắm hình chữ nhật ở giữa màn hình và bấm phím **`c` (Capture)** để trích xuất ngay mẫu da tay mới từ webcam!
- **Giao diện thời gian thực (Dashboard 4 khung hình):**
  - Góc trên bên trái: Khung hình Camera gốc kèm khung chữ nhật ngắm ROI.
  - Góc trên bên phải: Bản đồ xác suất Backprojection (Probability Map).
  - Góc dưới bên trái: Mặt nạ nhị phân sau phân ngưỡng và morphology (Binary Mask).
  - Góc dưới bên phải: Bàn tay đã tách nền hoàn chỉnh (Segmented Hand).
- **Phím điều khiển:**
  - Bấm **`c`**: Cập nhật lại mẫu da tay từ khung ngắm.
  - Bấm **`q`**: Thoát chương trình và giải phóng tài nguyên camera.
