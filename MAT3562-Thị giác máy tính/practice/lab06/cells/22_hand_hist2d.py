# Bước 2.2: Tính Histogram mẫu da tay trên cả không gian HSV và RGB (Chuẩn hóa bắt buộc)
hsv_roi = cv2.cvtColor(roi_da_tay, cv2.COLOR_BGR2HSV)
hsv_hand = cv2.cvtColor(img_hand, cv2.COLOR_BGR2HSV)
rgb_roi = cv2.cvtColor(roi_da_tay, cv2.COLOR_BGR2RGB)
rgb_hand = cv2.cvtColor(img_hand, cv2.COLOR_BGR2RGB)

so_pixel_roi = float(roi_da_tay.shape[0] * roi_da_tay.shape[1])

# 1. 2D HSV Histogram (kênh H và S: 180x256 bins)
hist_skin_hsv = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
hist_skin_hsv_norm = hist_skin_hsv / so_pixel_roi

# 2. 2D Red-Green Histogram (kênh R và G: 32x32 bins theo bảng ví dụ Câu 2 giáo trình)
hist_skin_rg = cv2.calcHist([rgb_roi], [0, 1], None, [32, 32], [0, 256, 0, 256])
hist_skin_rg_norm = hist_skin_rg / so_pixel_roi

# 3. 3D RGB Histogram (16x16x16 bins)
hist_skin_rgb3d = cv2.calcHist([rgb_roi], [0, 1, 2], None, [16, 16, 16], [0, 256, 0, 256, 0, 256])
hist_skin_rgb3d_norm = hist_skin_rgb3d / so_pixel_roi

print("Tổng xác suất sau chuẩn hóa của 2D HSV      :", np.sum(hist_skin_hsv_norm))
print("Tổng xác suất sau chuẩn hóa của 2D Red-Green:", np.sum(hist_skin_rg_norm))
print("Tổng xác suất sau chuẩn hóa của 3D RGB      :", np.sum(hist_skin_rgb3d_norm))

# Trực quan hóa Heatmap so sánh phân bố màu da trên 2D HSV và 2D Red-Green
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

# Heatmap 2D HSV (H in [0, 40], S in [0, 150])
im1 = ax1.imshow(hist_skin_hsv_norm[:40, :150], origin='lower', cmap='hot', aspect='auto')
ax1.set_title('1. Bản đồ nhiệt 2D HSV (Hue vs Saturation)', fontweight='bold')
ax1.set_xlabel('Saturation (Độ bão hòa màu)')
ax1.set_ylabel('Hue (Sắc thái màu)')
cbar1 = plt.colorbar(im1, ax=ax1)
cbar1.set_label('Mật độ xác suất')

# Heatmap 2D Red-Green (R in [16, 32], G in [16, 32])
im2 = ax2.imshow(hist_skin_rg_norm, origin='lower', cmap='plasma', aspect='auto')
ax2.set_title('2. Bản đồ nhiệt 2D Red-Green (Red vs Green)', fontweight='bold')
ax2.set_xlabel('Green channel bin (0-31)')
ax2.set_ylabel('Red channel bin (0-31)')
cbar2 = plt.colorbar(im2, ax=ax2)
cbar2.set_label('Mật độ xác suất')

plt.tight_layout()
plt.show()
