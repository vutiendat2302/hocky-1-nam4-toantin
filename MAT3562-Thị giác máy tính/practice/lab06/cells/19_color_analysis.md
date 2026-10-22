### So sánh và đánh giá toàn diện giữa Bước 1 (Ảnh xám) và Bước 2 (Ảnh màu):

1. **Sự khác biệt rõ rệt về kết quả tra cứu:**
   - Trong **Bước 1 (Ảnh xám)**: Thuật toán xếp `images (4).jpeg` và `images.jpeg` ở vị trí cao nhất vì các bức ảnh này có phân bố mức độ sáng - tối tổng thể tương tự ảnh `ava.jpg`.
   - Trong **Bước 2 (Ảnh màu)**: Trên không gian màu 2D HSV, **`images (3).jpeg`** và **`images (1).jpeg`** vươn lên dẫn đầu. Lý do là ảnh `ava.jpg` có tông màu chủ đạo rất đặc trưng (màu da, nền xanh lam nhạt, trang phục), và không gian 2D HSV đã bắt trúng chính xác các sắc thái màu (Hue) và độ tinh khiết (Saturation) này.
2. **So sánh 3 cấu hình ảnh màu:**
   - **Cấu hình A (2D HSV):** Cho kết quả phản ánh ngữ nghĩa thị giác tốt nhất vì tách biệt hoàn toàn sắc thái màu ($H, S$) khỏi độ chói ($V$). Ngay cả khi hai ảnh chụp trong điều kiện ánh sáng khác nhau, nếu đối tượng cùng màu thì vẫn khớp nhau tốt.
   - **Cấu hình B (3D RGB):** Giữ được tương quan đầy đủ giữa 3 kênh nhưng kích thước histogram lớn ($512$ bins), đòi hỏi nhiều tính toán hơn và có hiện tượng thưa bin (nhiều bin bằng 0).
   - **Cấu hình C (Concatenated RGB):** Rất gọn nhẹ ($48$ bins), chạy nhanh, tuy nhiên vì tính độc lập từng kênh nên làm mất đi mối quan hệ kết hợp (joint probability) giữa các màu.
3. **Kết luận về phương pháp đối sánh:**
   - **Intersection** và **Bhattacharyya** là hai phương pháp cho kết quả ổn định và tin cậy nhất trên cả ảnh xám và ảnh màu.
   - **Correlation** nhạy cảm hơn với giá trị trung bình toàn cục.
   - **Chi-Square** phạt rất nặng các bin có sai lệch lớn, phù hợp khi cần tìm các ảnh có phân bố màu sắc gần như tuyệt đối đồng nhất.
