# Bước 2.1: Chuẩn bị dữ liệu - Đọc ảnh bàn tay và trích xuất vùng da tay mẫu (Skin ROI)
anh_ban_tay_path = 'bantay.jpeg'
img_hand = cv2.imread(anh_ban_tay_path)
if img_hand is None:
    raise FileNotFoundError(f"Không tìm thấy file: {anh_ban_tay_path}")

print("Kích thước ảnh chụp bàn tay:", img_hand.shape)

# Trích xuất vùng da tay đại diện từ lòng bàn tay: y in [110:140], x in [95:125]
y1, y2, x1, x2 = 110, 140, 95, 125
roi_da_tay = img_hand[y1:y2, x1:x2].copy()

# Lưu vùng da tay mẫu thành file độc lập da_tay.jpeg
anh_da_tay_path = 'da_tay.jpeg'
cv2.imwrite(anh_da_tay_path, roi_da_tay)
print(f"Đã trích xuất và lưu vùng da tay mẫu tại: {anh_da_tay_path} (Kích thước: {roi_da_tay.shape})")

# Hiển thị ảnh chụp bàn tay với khung ROI và ảnh mẫu da tay
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5))

img_hand_boxed = img_hand.copy()
cv2.rectangle(img_hand_boxed, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.putText(img_hand_boxed, "Skin ROI", (x1 - 10, y1 - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

ax1.imshow(cv2.cvtColor(img_hand_boxed, cv2.COLOR_BGR2RGB))
ax1.set_title("Ảnh chụp bàn tay (bantay.jpeg)\nkèm khung lấy mẫu Skin ROI", fontweight='bold')
ax1.axis('off')

ax2.imshow(cv2.cvtColor(roi_da_tay, cv2.COLOR_BGR2RGB))
ax2.set_title(f"Ảnh da tay mẫu (da_tay.jpeg)\nKích thước: {roi_da_tay.shape[0]}x{roi_da_tay.shape[1]} px", fontweight='bold')
ax2.axis('off')

plt.tight_layout()
plt.show()
