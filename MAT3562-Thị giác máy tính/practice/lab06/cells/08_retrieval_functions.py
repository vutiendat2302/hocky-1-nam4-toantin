def tra_cuu_anh(thu_muc_D, anh_Q_path, k=4, phuong_phap='Intersection', 
                 ham_trich_xuat_hist=tinh_histogram_chuan_hoa_1d):
    # Quy trình tra cứu k ảnh tương đồng nhất trong D với ảnh Q
    if phuong_phap not in DANH_SACH_PHUONG_PHAP:
        raise ValueError(f"Phương pháp không hợp lệ. Chọn từ: {list(DANH_SACH_PHUONG_PHAP.keys())}")
    
    pp_info = DANH_SACH_PHUONG_PHAP[phuong_phap]
    ham_doi_sanh = pp_info['func']
    giam_dan = pp_info['higher_is_better']
    
    # Đọc và tính histogram của ảnh truy vấn Q
    img_Q = cv2.imread(anh_Q_path)
    if img_Q is None:
        raise FileNotFoundError(f"Không tìm thấy ảnh truy vấn tại: {anh_Q_path}")
    hist_Q = ham_trich_xuat_hist(img_Q)
    
    # Lấy danh sách ảnh trong D
    duong_dan_anh_D = sorted(glob.glob(os.path.join(thu_muc_D, '*')))
    
    ket_qua = []
    for p in duong_dan_anh_D:
        img_I = cv2.imread(p)
        if img_I is None:
            continue
        hist_I = ham_trich_xuat_hist(img_I)
        score = ham_doi_sanh(hist_Q, hist_I)
        ten_file = os.path.basename(p)
        ket_qua.append({
            'duong_dan': p,
            'ten_file': ten_file,
            'score': score
        })
    
    # Sắp xếp theo tiêu chí tốt nhất
    ket_qua.sort(key=lambda x: x['score'], reverse=giam_dan)
    
    # Lấy k ảnh tốt nhất
    top_k = ket_qua[:k]
    return top_k, ket_qua

def hien_thi_ket_qua_tra_cuu(anh_Q_path, top_k, tieu_de="Kết quả tra cứu ảnh", k=4, la_anh_xam=False):
    # Trực quan hóa ảnh truy vấn Q bên cạnh k ảnh kết quả tìm được trong D
    # la_anh_xam=True: hiển thị dạng ảnh xám (cmap='gray') cho Bước 1
    # la_anh_xam=False: hiển thị dạng ảnh màu (RGB) cho Bước 2
    so_cot = k + 1
    fig, axes = plt.subplots(1, so_cot, figsize=(3.2 * so_cot, 4.2))
    
    # Vẽ ảnh truy vấn Q
    img_Q = cv2.imread(anh_Q_path)
    if la_anh_xam:
        gray_Q = cv2.cvtColor(img_Q, cv2.COLOR_BGR2GRAY)
        axes[0].imshow(gray_Q, cmap='gray')
        nhan_q = f"TRUY VẤN (Q - Xám)\n{os.path.basename(anh_Q_path)}"
    else:
        axes[0].imshow(cv2.cvtColor(img_Q, cv2.COLOR_BGR2RGB))
        nhan_q = f"TRUY VẤN (Q - Màu)\n{os.path.basename(anh_Q_path)}"
        
    axes[0].set_title(nhan_q, fontsize=11, fontweight='bold', color='navy')
    axes[0].axis('off')
    for spine in axes[0].spines.values():
        spine.set_edgecolor('blue')
        spine.set_linewidth(3)
        spine.set_visible(True)
        
    # Vẽ k ảnh kết quả
    for idx, item in enumerate(top_k):
        ax = axes[idx + 1]
        img_I = cv2.imread(item['duong_dan'])
        if la_anh_xam:
            gray_I = cv2.cvtColor(img_I, cv2.COLOR_BGR2GRAY)
            ax.imshow(gray_I, cmap='gray')
        else:
            ax.imshow(cv2.cvtColor(img_I, cv2.COLOR_BGR2RGB))
            
        ax.set_title(f"Rank #{idx+1}\n{item['ten_file']}\nScore: {item['score']:.4f}", 
                     fontsize=10, fontweight='bold', color='darkgreen')
        ax.axis('off')
        for spine in ax.spines.values():
            spine.set_edgecolor('green')
            spine.set_linewidth(2)
            spine.set_visible(True)
            
    fig.suptitle(tieu_de, fontsize=13, fontweight='bold', y=1.03)
    plt.tight_layout()
    plt.show()

print("Đã xây dựng xong các hàm tra cứu và hiển thị trực quan (Hỗ trợ hiển thị đúng chế độ xám / màu)!")
