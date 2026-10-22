# PHẦN 2: BÀI 1 - TRA CỨU ẢNH BẰNG ĐỐI SÁNH HISTOGRAM

### Quy trình tổng quát:
- **Đầu vào (Input):**
  - Thư mục ảnh $D$ (`thu_muc_anh` chứa 12 ảnh)
  - Ảnh truy vấn mới $Q$ (`ava.jpg`)
  - Giá trị $k$ (số lượng ảnh tương đồng nhất cần hiển thị)
  - Cấu hình histogram (Số bin, không gian màu: xám 1D, màu 2D HSV, màu 3D RGB, ghép 3 kênh)
  - Phương pháp đối sánh (Correlation, Chi-Square, Intersection, Bhattacharyya)
- **Đầu ra (Output):**
  - $k$ ảnh trong $D$ có giá trị đối sánh tốt nhất với $Q$
- **Các bước thực hiện:**
  1. Tính histogram của ảnh truy vấn $Q$ và tất cả các ảnh $I \in D$.
  2. Chuẩn hóa tất cả các histogram bằng cách chia cho số điểm ảnh của ảnh: $H = H / (H_{img} \times W_{img})$.
  3. Với mọi ảnh $I \in D$, tính điểm đối sánh giữa $H_I$ và $H_Q$ theo phương pháp đã chọn.
  4. Sắp xếp các ảnh theo điểm số:
     - Nếu phương pháp là Correlation hoặc Intersection: Sắp xếp **giảm dần** (lớn nhất là tốt nhất).
     - Nếu phương pháp là Chi-Square hoặc Bhattacharyya: Sắp xếp **tăng dần** (nhỏ nhất là tốt nhất).
  5. Chọn ra và hiển thị trực quan $k$ ảnh có kết quả tốt nhất kèm thứ hạng và điểm số.
