# Cài đặt các hàm trích xuất histogram cho 3 cấu hình ảnh màu

# Cấu hình A: 2D HSV Histogram (kênh H và S)
def trich_xuat_hist_2d_hsv(img, bins_h=18, bins_s=16):
    # Tính 2D Histogram trên 2 kênh H và S trong không gian HSV, chuẩn hóa về tổng = 1.0
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist2d = cv2.calcHist([hsv], [0, 1], None, [bins_h, bins_s], [0, 180, 0, 256])
    # Chuẩn hóa chia cho tổng số điểm ảnh:
    so_diem_anh = float(img.shape[0] * img.shape[1])
    hist2d_norm = (hist2d / so_diem_anh).flatten().astype(np.float32)
    return hist2d_norm

# Cấu hình B: 3D RGB Histogram (Joint RGB)
def trich_xuat_hist_3d_rgb(img, bins_per_channel=8):
    # Tính 3D Joint Histogram trên cả 3 kênh R, G, B (bins^3 bins), chuẩn hóa về tổng = 1.0
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hist3d = cv2.calcHist([rgb], [0, 1, 2], None, 
                          [bins_per_channel, bins_per_channel, bins_per_channel], 
                          [0, 256, 0, 256, 0, 256])
    so_diem_anh = float(img.shape[0] * img.shape[1])
    hist3d_norm = (hist3d / so_diem_anh).flatten().astype(np.float32)
    return hist3d_norm

# Cấu hình C: Concatenated 1D RGB (Ghép 3 kênh)
def trich_xuat_hist_concat_rgb(img, bins_per_channel=16):
    # Tính riêng histogram 1D chuẩn hóa cho từng kênh B, G, R rồi ghép lại (tổng vector = 1.0)
    hists = []
    so_diem_anh = float(img.shape[0] * img.shape[1])
    for c in range(3):
        h, _ = np.histogram(img[:, :, c], bins=bins_per_channel, range=(0, 256))
        h_norm = h.astype(np.float32) / so_diem_anh
        hists.append(h_norm)
    # Ghép 3 kênh và chia 3 để tổng xác suất toàn vector bằng 1.0
    concat_hist = np.concatenate(hists) / 3.0
    return concat_hist.astype(np.float32)

print("Đã cài đặt xong 3 hàm trích xuất histogram ảnh màu chuẩn hóa!")
