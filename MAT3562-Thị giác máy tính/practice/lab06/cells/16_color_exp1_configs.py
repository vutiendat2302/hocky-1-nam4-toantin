# Thử nghiệm 2.1: So sánh 3 Cấu hình Histogram màu (k = 4, Phương pháp: Intersection)
cau_hinh_mau = {
    'Cấu hình A: 2D HSV (18x16 = 288 bins)': trich_xuat_hist_2d_hsv,
    'Cấu hình B: 3D RGB (8x8x8 = 512 bins)': trich_xuat_hist_3d_rgb,
    'Cấu hình C: Ghép RGB (3x16 = 48 bins)': trich_xuat_hist_concat_rgb
}

print("=== THỬ NGHIỆM 2.1: SO SÁNH 3 CẤU HÌNH HISTOGRAM MÀU VỚI k = 4 (INTERSECTION) ===")
for ten_ch, ham_h in cau_hinh_mau.items():
    top_k, _ = tra_cuu_anh(thu_muc_D, anh_Q, k=4, phuong_phap='Intersection', 
                          ham_trich_xuat_hist=ham_h)
    
    tieu_de = f"Bước 2 (Ảnh màu) | {ten_ch} | Phương pháp: Intersection"
    hien_thi_ket_qua_tra_cuu(anh_Q, top_k, tieu_de=tieu_de, k=4)
