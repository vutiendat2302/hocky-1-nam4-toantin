# Kiểm chứng tính đúng đắn trên ma trận mẫu nhân tạo (tương tự bài giảng)
I_1 = np.array([
    [224, 5, 181, 185, 38],
    [103, 60, 101, 160, 186],
    [57, 199, 175, 51, 36],
    [71, 166, 32, 30, 86]
], dtype=np.uint8)

I_2 = np.array([
    [199, 20, 129, 175, 111],
    [119, 178, 12, 186, 212],
    [76, 219, 182, 39, 16],
    [88, 145, 12, 45, 99]
], dtype=np.uint8)

h1_norm = tinh_histogram_chuan_hoa_1d(I_1, 16)
h2_norm = tinh_histogram_chuan_hoa_1d(I_2, 16)

print("=== KIỂM THỬ ĐỐI SÁNH TRÊN DỮ LIỆU MẪU CHUẨN HÓA ===")
for ten_pp, info in DANH_SACH_PHUONG_PHAP.items():
    diem = info['func'](h1_norm, h2_norm)
    tieu_chi = "Tốt nhất: LỚN NHẤT" if info['higher_is_better'] else "Tốt nhất: NHỎ NHẤT"
    print(f"- {ten_pp:15s}: {diem:8.4f} | {tieu_chi} ({info['desc']})")
