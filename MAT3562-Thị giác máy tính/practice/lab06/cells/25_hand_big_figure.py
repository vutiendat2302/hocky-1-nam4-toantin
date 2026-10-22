# Bước 2.5: Trực quan hóa tổng hợp toàn bộ quy trình phân đoạn bàn tay (6 bước hoàn chỉnh)
fig, axes = plt.subplots(2, 3, figsize=(14, 9))

# 1. Ảnh gốc có khung ROI
axes[0, 0].imshow(cv2.cvtColor(img_hand_boxed, cv2.COLOR_BGR2RGB))
axes[0, 0].set_title("1. Ảnh bàn tay gốc & Khung lấy mẫu da (ROI)", fontweight='bold')
axes[0, 0].axis('off')

# 2. Vùng mẫu da tay
axes[0, 1].imshow(cv2.cvtColor(roi_da_tay, cv2.COLOR_BGR2RGB))
axes[0, 1].set_title("2. Vùng da tay mẫu (da_tay.jpeg)", fontweight='bold')
axes[0, 1].axis('off')

# 3. 2D Histogram mẫu da (HSV)
axes[0, 2].imshow(hist_skin_hsv_norm[:40, :150], origin='lower', cmap='hot', aspect='auto')
axes[0, 2].set_title("3. Bản đồ nhiệt 2D HSV mẫu da", fontweight='bold')
axes[0, 2].set_xlabel('Saturation')
axes[0, 2].set_ylabel('Hue')

# 4. Bản đồ xác suất Backprojection
axes[1, 0].imshow(dst_hsv_smooth, cmap='gray')
axes[1, 0].set_title("4. Bản đồ xác suất sau Backprojection", fontweight='bold')
axes[1, 0].axis('off')

# 5. Mặt nạ nhị phân sau làm sạch
axes[1, 1].imshow(mask_clean, cmap='gray')
axes[1, 1].set_title("5. Mặt nạ nhị phân bàn tay (Binary Mask)", fontweight='bold')
axes[1, 1].axis('off')

# 6. Bàn tay đã tách nền hoàn chỉnh
axes[1, 2].imshow(cv2.cvtColor(ban_tay_tach_nen, cv2.COLOR_BGR2RGB))
axes[1, 2].set_title("6. Kết quả bàn tay đã tách nền", fontweight='bold')
axes[1, 2].axis('off')

fig.suptitle("TỔNG QUAN QUY TRÌNH PHÂN ĐOẠN BÀN TAY BẰNG HISTOGRAM BACKPROJECTION VÀ PHÂN NGƯỠNG", 
             fontsize=14, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()
