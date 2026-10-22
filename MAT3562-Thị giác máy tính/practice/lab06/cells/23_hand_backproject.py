# Bước 2.3: Thực hiện Histogram Backprojection trên cả không gian HSV và RGB

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# 1. Backprojection trên không gian 2D HSV
cv2.normalize(hist_skin_hsv, hist_skin_hsv, 0, 255, cv2.NORM_MINMAX)
dst_hsv = cv2.calcBackProject([hsv_hand], [0, 1], hist_skin_hsv, [0, 180, 0, 256], 1)
dst_hsv_smooth = cv2.filter2D(dst_hsv, -1, disc)

# 2. Backprojection trên không gian 2D Red-Green (RG)
cv2.normalize(hist_skin_rg, hist_skin_rg, 0, 255, cv2.NORM_MINMAX)
dst_rg = cv2.calcBackProject([rgb_hand], [0, 1], hist_skin_rg, [0, 256, 0, 256], 1)
dst_rg_smooth = cv2.filter2D(dst_rg, -1, disc)

# 3. Backprojection trên không gian 3D RGB (Cài đặt vector hóa theo sơ đồ thuật toán)
bins_3d = 16
r_b = (rgb_hand[:, :, 0].astype(int) * bins_3d // 256).clip(0, bins_3d - 1)
g_b = (rgb_hand[:, :, 1].astype(int) * bins_3d // 256).clip(0, bins_3d - 1)
b_b = (rgb_hand[:, :, 2].astype(int) * bins_3d // 256).clip(0, bins_3d - 1)

dst_rgb3d = hist_skin_rgb3d_norm[r_b, g_b, b_b]
if dst_rgb3d.max() > 0:
    dst_rgb3d = (dst_rgb3d / dst_rgb3d.max() * 255).astype(np.uint8)
else:
    dst_rgb3d = np.zeros(img_hand.shape[:2], dtype=np.uint8)
dst_rgb3d_smooth = cv2.filter2D(dst_rgb3d, -1, disc)

# Hiển thị so sánh 3 bản đồ xác suất Backprojection
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

im0 = axes[0].imshow(dst_hsv_smooth, cmap='gray')
axes[0].set_title("1. Backprojection: 2D HSV (H-S)", fontweight='bold')
axes[0].axis('off')
plt.colorbar(im0, ax=axes[0], fraction=0.046, pad=0.04)

im1 = axes[1].imshow(dst_rg_smooth, cmap='gray')
axes[1].set_title("2. Backprojection: 2D Red-Green (R-G)", fontweight='bold')
axes[1].axis('off')
plt.colorbar(im1, ax=axes[1], fraction=0.046, pad=0.04)

im2 = axes[2].imshow(dst_rgb3d_smooth, cmap='gray')
axes[2].set_title("3. Backprojection: 3D RGB (R-G-B)", fontweight='bold')
axes[2].axis('off')
plt.colorbar(im2, ax=axes[2], fraction=0.046, pad=0.04)

fig.suptitle("SO SÁNH BẢN ĐỒ XÁC SUẤT BACKPROJECTION TRÊN CÁC KHÔNG GIAN MÀU KHÁC NHAU", 
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()

print("Cả 3 không gian màu đều làm nổi bật rõ vùng bàn tay và triệt tiêu nền trắng!")
