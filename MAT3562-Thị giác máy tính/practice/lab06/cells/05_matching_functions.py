# Định nghĩa 4 phương pháp đối sánh Histogram
def correlation(h1, h2):
    # 1. Phương pháp Correlation (Hệ số tương quan Pearson)
    # Khoảng giá trị: [-1.0, 1.0]. Giá trị càng lớn (càng gần 1.0) càng tương đồng.
    mean1 = np.mean(h1)
    mean2 = np.mean(h2)
    nom = np.sum((h1 - mean1) * (h2 - mean2))
    denom = np.sqrt(np.sum((h1 - mean1) ** 2) * np.sum((h2 - mean2) ** 2))
    if denom == 0:
        return 0.0
    return float(nom / denom)

def chi_square(h1, h2):
    # 2. Phương pháp Chi-Square (theo định nghĩa Cell 17 giáo trình)
    # Khoảng giá trị: [0.0, +inf). Giá trị càng nhỏ (càng gần 0.0) càng tương đồng.
    v = 0.0
    for i in range(h1.shape[0]):
        denom = h1[i] + h2[i]
        if denom > 0:
            v += float((h1[i] - h2[i]) * (h1[i] - h2[i])) / denom
    return float(v)

def intersection(h1, h2):
    # 3. Phương pháp Intersection (Độ giao cắt Histogram)
    # Với histogram chuẩn hóa (tổng = 1.0), khoảng giá trị: [0.0, 1.0].
    # Giá trị càng lớn (càng gần 1.0) càng tương đồng.
    v = 0.0
    for i in range(h1.shape[0]):
        v += min(h1[i], h2[i])
    return float(v)

def bhattacharyya(h1, h2):
    # 4. Phương pháp Bhattacharyya distance
    # Đo lường sự trùng lặp giữa hai phân bố xác suất.
    # Khoảng giá trị: [0.0, 1.0]. Giá trị càng nhỏ (càng gần 0.0) càng tương đồng.
    bc = np.sum(np.sqrt(np.clip(h1 * h2, 0.0, None)))
    val = max(0.0, 1.0 - bc)
    return float(np.sqrt(val))

# Bảng từ điển cấu hình và tiêu chí đánh giá
DANH_SACH_PHUONG_PHAP = {
    'Correlation': {
        'func': correlation,
        'higher_is_better': True,
        'desc': 'Hệ số tương quan (Max = 1.0)'
    },
    'Chi-Square': {
        'func': chi_square,
        'higher_is_better': False,
        'desc': 'Khoảng cách Chi bình phương (Min = 0.0)'
    },
    'Intersection': {
        'func': intersection,
        'higher_is_better': True,
        'desc': 'Độ giao cắt Histogram (Max = 1.0)'
    },
    'Bhattacharyya': {
        'func': bhattacharyya,
        'higher_is_better': False,
        'desc': 'Khoảng cách Bhattacharyya (Min = 0.0)'
    }
}

print("Đã cài đặt thành công 4 phương pháp đối sánh Histogram!")
