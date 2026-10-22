# Thử nghiệm 1.2: Khảo sát các lựa chọn khác nhau của giá trị k (k = 3, 5, 8)
# Sử dụng phương pháp Bhattacharyya distance trên ảnh xám 16 bins
cac_gia_tri_k = [3, 5, 8]

print("=== THỬ NGHIỆM 1.2: KHẢO SÁT VỚI CÁC GIÁ TRỊ k KHÁC NHAU (k = 3, 5, 8) ===")
for k_val in cac_gia_tri_k:
    top_k, _ = tra_cuu_anh(thu_muc_D, anh_Q, k=k_val, phuong_phap='Bhattacharyya',
                          ham_trich_xuat_hist=ham_hist_gray_16)
    
    tieu_de = f"Tra cứu ảnh xám với k = {k_val} (Phương pháp: Bhattacharyya distance)"
    # ĐẶT la_anh_xam=True để hiển thị đúng ảnh dạng mức xám
    hien_thi_ket_qua_tra_cuu(anh_Q, top_k, tieu_de=tieu_de, k=k_val, la_anh_xam=True)
