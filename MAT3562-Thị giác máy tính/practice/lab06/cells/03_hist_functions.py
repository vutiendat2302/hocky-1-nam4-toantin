# 1. Hàm tính histogram nguyên bản theo giáo trình (duyệt lặp từng pixel)
def tinh_histogram_giao_trinh(I, n):
    # Tính histogram mức xám bằng vòng lặp theo tài liệu bài giảng
    # I: ảnh xám (2D uint8), n: số khoảng (thường là 4, 8, 16, 32...)
    t = 1.0 * 256 / n
    ranges = [[math.ceil(t * i), math.ceil(t * (i + 1)) - 1] for i in range(n)]

    h = np.zeros(n, np.int32)
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            for k in range(n):
                if I[i, j] >= ranges[k][0] and I[i, j] <= ranges[k][1]:
                    h[k] = h[k] + 1
                    break
    return h, ranges

# 2. Hàm tính histogram chuẩn hóa tối ưu (vector hóa bằng NumPy)
def tinh_histogram_chuan_hoa_1d(I, n_bins=16):
    # Tính histogram ảnh xám và chuẩn hóa bằng cách chia cho số điểm ảnh
    # I: ảnh đầu vào (ảnh xám hoặc BGR), n_bins: số khoảng chia
    # Trả về: vector histogram 1D dạng float32 có tổng = 1.0
    if len(I.shape) == 3:
        gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    else:
        gray = I

    # Tính histogram qua np.histogram
    h, _ = np.histogram(gray, bins=n_bins, range=(0, 256))

    # BẮT BUỘC CHUẨN HÓA: Chia cho tổng số điểm ảnh của ảnh
    so_diem_anh = float(gray.shape[0] * gray.shape[1])
    h_norm = h.astype(np.float32) / so_diem_anh

    return h_norm

# Thử nghiệm tính và trực quan hóa ảnh xám cùng histogram chuẩn hóa trên ảnh truy vấn ava.jpg
img_test = cv2.imread('ava.jpg')
gray_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY)
h_test = tinh_histogram_chuan_hoa_1d(gray_test, n_bins=16)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Hiển thị ảnh mức xám
ax1.imshow(gray_test, cmap='gray')
ax1.set_title("Ảnh truy vấn Q ở dạng mức xám (Grayscale)", fontweight='bold')
ax1.axis('off')

# Biểu đồ Histogram
ax2.bar(range(16), h_test, color='steelblue', edgecolor='black', alpha=0.8)
ax2.set_title('Histogram chuẩn hóa của ảnh ava.jpg (16 bins, Tổng = {:.2f})'.format(np.sum(h_test)), fontweight='bold')
ax2.set_xlabel('Chỉ số Bin (Mức xám từ 0 đến 255)')
ax2.set_ylabel('Tần suất xác suất (Chuẩn hóa)')
ax2.set_xticks(range(16))
ax2.set_xticklabels([f'{i*16}-{(i+1)*16-1}' for i in range(16)], rotation=45, ha='right')
ax2.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()

print("Tổng các giá trị sau chuẩn hóa:", np.sum(h_test))
