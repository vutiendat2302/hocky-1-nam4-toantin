# Thử nghiệm 2.2: So sánh 4 Phương pháp đối sánh trên Cấu hình màu 2D HSV (k = 5)
print("=== THỬ NGHIỆM 2.2: SO SÁNH 4 PHƯƠNG PHÁP ĐỐI SÁNH TRÊN CẤU HÌNH 2D HSV (k = 5) ===")

ket_qua_mau_pp = {}
for ten_pp in DANH_SACH_PHUONG_PHAP.keys():
    top_k, _ = tra_cuu_anh(thu_muc_D, anh_Q, k=5, phuong_phap=ten_pp, 
                          ham_trich_xuat_hist=trich_xuat_hist_2d_hsv)
    ket_qua_mau_pp[ten_pp] = top_k
    
    tieu_de = f"Bước 2 (2D HSV - 18x16 bins) | Phương pháp: {ten_pp} (k = 5)"
    hien_thi_ket_qua_tra_cuu(anh_Q, top_k, tieu_de=tieu_de, k=5)

# In bảng xếp hạng Top 5 ảnh màu theo 4 phương pháp
print("\nBẢNG XẾP HẠNG TOP 5 ẢNH TƯƠNG ĐỒNG THEO 4 PHƯƠNG PHÁP TRÊN 2D HSV:")
print("-" * 88)
print(f"{'Thứ hạng':<10} | {'Correlation':<18} | {'Chi-Square':<18} | {'Intersection':<18} | {'Bhattacharyya':<18}")
print("-" * 88)
for r in range(5):
    c_f = f"{ket_qua_mau_pp['Correlation'][r]['ten_file'][:10]} ({ket_qua_mau_pp['Correlation'][r]['score']:.2f})"
    cs_f = f"{ket_qua_mau_pp['Chi-Square'][r]['ten_file'][:10]} ({ket_qua_mau_pp['Chi-Square'][r]['score']:.2f})"
    in_f = f"{ket_qua_mau_pp['Intersection'][r]['ten_file'][:10]} ({ket_qua_mau_pp['Intersection'][r]['score']:.2f})"
    bh_f = f"{ket_qua_mau_pp['Bhattacharyya'][r]['ten_file'][:10]} ({ket_qua_mau_pp['Bhattacharyya'][r]['score']:.2f})"
    print(f"Rank #{r+1:<5} | {c_f:<18} | {cs_f:<18} | {in_f:<18} | {bh_f:<18}")
print("-" * 88)
