# Thử nghiệm 2.3: Khảo sát độ mịn số Bin trong không gian 2D HSV (8x8, 16x16, 30x32)
do_min_bins = [(8, 8), (18, 16), (30, 32)]

print("=== THỬ NGHIỆM 2.3: KHẢO SÁT ĐỘ MỊN SỐ BIN TRÊN 2D HSV (k = 4, BHATTACHARYYA) ===")
for bh, bs in do_min_bins:
    ham_h = lambda img, h=bh, s=bs: trich_xuat_hist_2d_hsv(img, bins_h=h, bins_s=s)
    top_k, _ = tra_cuu_anh(thu_muc_D, anh_Q, k=4, phuong_phap='Bhattacharyya', 
                          ham_trich_xuat_hist=ham_h)
    
    tieu_de = f"Độ phân giải 2D HSV: {bh}x{bs} = {bh*bs} bins | Bhattacharyya distance"
    hien_thi_ket_qua_tra_cuu(anh_Q, top_k, tieu_de=tieu_de, k=4)
