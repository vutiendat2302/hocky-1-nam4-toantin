# Thử nghiệm 1.3: Khảo sát ảnh hưởng của Cấu hình Histogram (Số lượng bin n = 8, 16, 32, 64, 256)
cac_so_bin = [8, 16, 32, 64, 256]
anh_top1_theo_bin = []
scores_top1 = []

for nb in cac_so_bin:
    ham_hist = lambda img, n=nb: tinh_histogram_chuan_hoa_1d(img, n_bins=n)
    top_k, _ = tra_cuu_anh(thu_muc_D, anh_Q, k=1, phuong_phap='Intersection', 
                          ham_trich_xuat_hist=ham_hist)
    anh_top1_theo_bin.append(top_k[0]['ten_file'])
    scores_top1.append(top_k[0]['score'])

plt.figure(figsize=(9, 4.5))
plt.plot(cac_so_bin, scores_top1, marker='o', linewidth=2.5, markersize=8, color='crimson')
plt.title('Ảnh hưởng của số lượng Bin đến độ giao cắt Intersection của ảnh Top 1', fontsize=12, fontweight='bold')
plt.xlabel('Số lượng Bin (n)')
plt.ylabel('Điểm số Intersection (Độ tương đồng)')
plt.grid(True, linestyle='--', alpha=0.6)
for i, nb in enumerate(cac_so_bin):
    plt.annotate(f"{anh_top1_theo_bin[i]}\n({scores_top1[i]:.4f})", 
                 (nb, scores_top1[i]), 
                 textcoords="offset points", 
                 xytext=(0, 10), 
                 ha='center', fontsize=9, fontweight='bold')
plt.ylim(0, 1.0)
plt.show()

print("Bảng thống kê sự ổn định của ảnh Top 1 khi thay đổi số Bin:")
for i, nb in enumerate(cac_so_bin):
    print(f"- n = {nb:3d} bins -> Ảnh Top 1: {anh_top1_theo_bin[i]:20s} | Điểm tương đồng: {scores_top1[i]:.4f}")
