## BÀI 1 - BƯỚC 1: TRA CỨU TRÊN ẢNH XÁM (GRAYSCALE)

Ở bước này, toàn bộ ảnh trong tập dữ liệu $D$ (`thu_muc_anh`) và ảnh truy vấn $Q$ (`ava.jpg`) được chuyển sang ảnh mức xám. Chúng ta sẽ tiến hành các thử nghiệm:
- **Thử nghiệm 1.1:** So sánh kết quả tra cứu giữa 4 phương pháp đối sánh (Correlation, Chi-Square, Intersection, Bhattacharyya) với cấu hình cố định ($k=4$, 16 bins).
- **Thử nghiệm 1.2:** Khảo sát ảnh hưởng của giá trị $k$ ($k=3, 5, 8$).
- **Thử nghiệm 1.3:** Khảo sát ảnh hưởng của cấu hình Histogram (thay đổi số bin: $n=8, 16, 32, 64, 256$).
