### Nhận xét và phân tích kết quả Bước 1 (Ảnh xám):
1. **Sự đồng thuận giữa các phương pháp đối sánh:**
   - Cả 4 phương pháp (Correlation, Chi-Square, Intersection, Bhattacharyya) đều chọn **`images (4).jpeg`** là ảnh có mức độ tương đồng cao nhất (Rank #1) với ảnh truy vấn `ava.jpg`.
   - Các ảnh xếp hạng tiếp theo như `images.jpeg` và `download.jpeg` cũng xuất hiện nhất quán trong nhóm dẫn đầu của các phương pháp.
2. **Ảnh hưởng của giá trị $k$:**
   - Khi $k=3$, thuật toán lọc ra nhóm tinh hoa có độ tương đồng cao nhất.
   - Khi tăng lên $k=5$ và $k=8$, hệ thống mở rộng diện tìm kiếm, cho phép người dùng quan sát các ảnh có độ tương đồng giảm dần.
3. **Ảnh hưởng của số lượng Bin:**
   - Khi chia số bin nhỏ ($n=8$), các khoảng mức xám quá rộng làm mất tính phân biệt, điểm số tương đồng có xu hướng cao nhưng kém chi tiết.
   - Khi tăng số bin lên ($n=16, 32, 64$), histogram mô tả phân bố mức xám chi tiết hơn. Tuy nhiên, nếu số bin quá lớn ($n=256$), histogram trở nên thưa (sparse) và rất nhạy cảm với sự chênh lệch nhỏ về ánh sáng. Mức $n=16$ hoặc $n=32$ cho sự cân bằng tốt nhất giữa độ phân giải và độ ổn định.
4. **Hạn chế cố hữu của ảnh xám:**
   - Mức xám chỉ phản ánh cường độ sáng tổng hợp ($Y = 0.299R + 0.587G + 0.114B$) mà bỏ qua hoàn toàn sắc thái màu sắc. Ví dụ: một vùng màu đỏ thẫm và một vùng màu xanh lục đậm có thể có cùng mức xám $Y \approx 80$, dẫn đến việc ảnh xám coi chúng là tương đồng dù về mặt thị giác con người chúng hoàn toàn khác nhau.
   - Để khắc phục hạn chế này, ta chuyển sang **Bước 2: Đối sánh trên ảnh màu**.
