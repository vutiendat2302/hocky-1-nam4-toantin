# Thử nghiệm 1.1: So sánh 4 phương pháp đối sánh trên ảnh xám (k=4, 16 bins)
thu_muc_D = 'thu_muc_anh'
anh_Q = 'ava.jpg'
k_test = 4
so_bin = 16

ham_hist_gray_16 = lambda img: tinh_histogram_chuan_hoa_1d(img, n_bins=so_bin)

print(f"================================================================================")
print(f"THỬ NGHIỆM 1.1: SO SÁNH 4 PHƯƠNG PHÁP ĐỐI SÁNH TRÊN ẢNH XÁM (k={k_test}, Bins={so_bin})")
print(f"Ảnh truy vấn Q: {anh_Q} | Số ảnh trong tập D: {len(glob.glob(os.path.join(thu_muc_D, '*')))}")
print(f"================================================================================")

ket_qua_cac_pp = {}

for ten_pp in DANH_SACH_PHUONG_PHAP.keys():
    top_k, full_res = tra_cuu_anh(thu_muc_D, anh_Q, k=k_test, phuong_phap=ten_pp, 
                                  ham_trich_xuat_hist=ham_hist_gray_16)
    ket_qua_cac_pp[ten_pp] = top_k
    
    tieu_de = f"Bước 1 (Ảnh xám - 16 bins) | Phương pháp: {ten_pp}"
    # ĐẶT la_anh_xam=True để hiển thị đúng ảnh dạng mức xám
    hien_thi_ket_qua_tra_cuu(anh_Q, top_k, tieu_de=tieu_de, k=k_test, la_anh_xam=True)

# In bảng tổng hợp xếp hạng Top 4 của 4 phương pháp
print("\nBẢNG XẾP HẠNG TOP 4 ẢNH TƯƠNG ĐỒNG THEO TỪNG PHƯƠNG PHÁP (ẢNH XÁM - 16 BINS):")
print("-" * 88)
print(f"{'Thứ hạng':<10} | {'Correlation':<18} | {'Chi-Square':<18} | {'Intersection':<18} | {'Bhattacharyya':<18}")
print("-" * 88)
for r in range(k_test):
    c_f = f"{ket_qua_cac_pp['Correlation'][r]['ten_file'][:10]} ({ket_qua_cac_pp['Correlation'][r]['score']:.2f})"
    cs_f = f"{ket_qua_cac_pp['Chi-Square'][r]['ten_file'][:10]} ({ket_qua_cac_pp['Chi-Square'][r]['score']:.2f})"
    in_f = f"{ket_qua_cac_pp['Intersection'][r]['ten_file'][:10]} ({ket_qua_cac_pp['Intersection'][r]['score']:.2f})"
    bh_f = f"{ket_qua_cac_pp['Bhattacharyya'][r]['ten_file'][:10]} ({ket_qua_cac_pp['Bhattacharyya'][r]['score']:.2f})"
    print(f"Rank #{r+1:<5} | {c_f:<18} | {cs_f:<18} | {in_f:<18} | {bh_f:<18}")
print("-" * 88)
