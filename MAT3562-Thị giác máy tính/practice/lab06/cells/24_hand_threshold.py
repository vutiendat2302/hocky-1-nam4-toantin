# Bước 2.4: Khảo sát và Thử nghiệm TOÀN BỘ các Phương pháp Phân ngưỡng (Thresholding)

# Danh sách từ điển chứa tất cả các phương pháp phân ngưỡng cần khảo sát
phuong_phap_nguong = {}

# 1. Nhóm phân ngưỡng nhị phân cố định (Fixed Manual Thresholds: T = 20, 40, 60, 80)
for t_val in [20, 40, 60, 80]:
    _, m_fix = cv2.threshold(dst_hsv_smooth, t_val, 255, cv2.THRESH_BINARY)
    phuong_phap_nguong[f"Cố định T={t_val}"] = m_fix

# 2. Phân ngưỡng toàn cục tự động Otsu (Otsu's Thresholding)
t_otsu, m_otsu = cv2.threshold(dst_hsv_smooth, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
phuong_phap_nguong[f"Otsu (T={t_otsu:.0f})"] = m_otsu

# 3. Phân ngưỡng toàn cục tự động Triangle (Triangle Thresholding)
t_tri, m_tri = cv2.threshold(dst_hsv_smooth, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)
phuong_phap_nguong[f"Triangle (T={t_tri:.0f})"] = m_tri

# 4. Phân ngưỡng thích nghi cục bộ (Adaptive Thresholding)
# - Adaptive Mean
m_adapt_mean = cv2.adaptiveThreshold(dst_hsv_smooth, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                     cv2.THRESH_BINARY, 11, 2)
phuong_phap_nguong["Adaptive Mean"] = m_adapt_mean

# - Adaptive Gaussian
m_adapt_gauss = cv2.adaptiveThreshold(dst_hsv_smooth, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                      cv2.THRESH_BINARY, 11, 2)
phuong_phap_nguong["Adaptive Gaussian"] = m_adapt_gauss

# 5. Phân ngưỡng theo dải màu trực tiếp (Color inRange Thresholding)
# - Trên không gian RGB:
r_min, r_max = int(rgb_roi[:,:,0].min() - 25), 255
g_min, g_max = max(0, int(rgb_roi[:,:,1].min() - 25)), min(255, int(rgb_roi[:,:,1].max() + 25))
b_min, b_max = max(0, int(rgb_roi[:,:,2].min() - 25)), min(255, int(rgb_roi[:,:,2].max() + 25))
m_inrange_rgb = cv2.inRange(rgb_hand, 
                            np.array([r_min, g_min, b_min], dtype=np.uint8), 
                            np.array([r_max, g_max, b_max], dtype=np.uint8))
phuong_phap_nguong["inRange RGB"] = m_inrange_rgb

# - Trên không gian HSV (Dải màu da chuẩn: H in [0, 25], S in [30, 255], V in [50, 255]):
hsv_curr = cv2.cvtColor(img_hand, cv2.COLOR_BGR2HSV)
m_inrange_hsv = cv2.inRange(hsv_curr, 
                            np.array([0, 30, 50], dtype=np.uint8), 
                            np.array([25, 255, 255], dtype=np.uint8))
phuong_phap_nguong["inRange HSV"] = m_inrange_hsv

# In bảng thống kê định lượng của tất cả các phương pháp phân ngưỡng
tong_so_pixel = float(img_hand.shape[0] * img_hand.shape[1])
print("=" * 80)
print(f"{'Phương pháp phân ngưỡng':<26} | {'Số pixel nhận diện':<20} | {'Tỷ lệ (% ảnh)':<15}")
print("=" * 80)
for ten_pp, mask_val in phuong_phap_nguong.items():
    cnt = np.sum(mask_val == 255)
    pct = (cnt / tong_so_pixel) * 100.0
    print(f"{ten_pp:<26} | {cnt:<20d} | {pct:<15.2f}%")
print("=" * 80)

# Trực quan hóa LƯỚI SO SÁNH TẤT CẢ CÁC PHƯƠNG PHÁP PHÂN NGƯỠNG (Mặt nạ & Kết quả tách bàn tay)
danh_sach_ten = list(phuong_phap_nguong.keys())
so_luong = len(danh_sach_ten)
so_cot = 5
so_dong = math.ceil(so_luong / so_cot)

fig, axes = plt.subplots(so_dong * 2, so_cot, figsize=(18, 4.2 * so_dong * 2))

for idx, ten_pp in enumerate(danh_sach_ten):
    col = idx % so_cot
    row_mask = (idx // so_cot) * 2
    row_seg = row_mask + 1
    
    m = phuong_phap_nguong[ten_pp]
    seg = cv2.bitwise_and(img_hand, img_hand, mask=m)
    
    # Vẽ mặt nạ nhị phân
    axes[row_mask, col].imshow(m, cmap='gray')
    axes[row_mask, col].set_title(f"Mask: {ten_pp}", fontsize=10, fontweight='bold')
    axes[row_mask, col].axis('off')
    
    # Vẽ bàn tay đã tách nền
    axes[row_seg, col].imshow(cv2.cvtColor(seg, cv2.COLOR_BGR2RGB))
    axes[row_seg, col].set_title(f"Tách: {ten_pp}", fontsize=10, fontweight='bold', color='darkgreen')
    axes[row_seg, col].axis('off')

# Tắt các ô trống nếu số lượng không tròn
for i in range(so_luong, so_dong * so_cot):
    col = i % so_cot
    row_mask = (i // so_cot) * 2
    row_seg = row_mask + 1
    axes[row_mask, col].axis('off')
    axes[row_seg, col].axis('off')

fig.suptitle("SO SÁNH TOÀN DIỆN CÁC PHƯƠNG PHÁP PHÂN NGƯỠNG TÁCH BÀN TAY", 
             fontsize=14, fontweight='bold', y=0.99)
plt.tight_layout()
plt.show()

# Hậu xử lý hình thái học (Morphology) trên mặt nạ tối ưu (Otsu / Fixed T=50)
_, mask_opt = cv2.threshold(dst_hsv_smooth, 50, 255, cv2.THRESH_BINARY)
kernel_morph = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
mask_closed = cv2.morphologyEx(mask_opt, cv2.MORPH_CLOSE, kernel_morph, iterations=2)
mask_clean = cv2.morphologyEx(mask_closed, cv2.MORPH_OPEN, kernel_morph, iterations=2)
ban_tay_tach_nen = cv2.bitwise_and(img_hand, img_hand, mask=mask_clean)

print("Đã hoàn thành khảo sát toàn bộ các phương pháp phân ngưỡng và tối ưu hóa mặt nạ!")
