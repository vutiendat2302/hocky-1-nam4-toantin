def phan_doan_ban_tay_video_webcam(nguon_video=0, anh_mau_da=None, so_frame_demo=4, che_do_gui=False):
    # Hàm phân đoạn bàn tay từ Webcam hoặc file Video sử dụng Histogram Backprojection
    # Tham số:
    # - nguon_video: 0 (webcam) hoặc đường dẫn file video (ví dụ: '../lab04/video.mp4')
    # - anh_mau_da: ảnh ROI mẫu da tay (nếu None sẽ dùng da_tay.jpeg đã chuẩn bị)
    # - so_frame_demo: số khung hình tiêu biểu cần hiển thị trong Notebook nếu chạy không có GUI
    # - che_do_gui: True nếu muốn mở cửa sổ OpenCV GUI (cần màn hình desktop)

    # 1. Chuẩn bị mẫu da tay ban đầu
    if anh_mau_da is None:
        if os.path.exists('da_tay.jpeg'):
            anh_mau_da = cv2.imread('da_tay.jpeg')
        else:
            raise FileNotFoundError("Chưa có mẫu da tay. Vui lòng cung cấp anh_mau_da hoặc chạy bước 2.1 trước.")
    
    # Tính 2D Histogram mẫu da
    hsv_roi = cv2.cvtColor(anh_mau_da, cv2.COLOR_BGR2HSV)
    hist_skin = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
    cv2.normalize(hist_skin, hist_skin, 0, 255, cv2.NORM_MINMAX)
    
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    kernel_morph = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    
    # 2. Mở nguồn video / webcam
    cap = cv2.VideoCapture(nguon_video)
    if not cap.isOpened():
        print(f"LƯU Ý: Không thể mở nguồn video/webcam '{nguon_video}'.")
        return []
    
    print(f"Đã mở thành công nguồn video: {nguon_video}")
    print(f"- Kích thước khung hình: {int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
    print(f"- Tốc độ khung hình (FPS): {cap.get(cv2.CAP_PROP_FPS):.1f}")
    
    frames_ket_qua = []
    frame_count = 0
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_count += 1
            # Resize nhẹ để xử lý mượt mà và đồng đều
            frame_resized = cv2.resize(frame, (640, 480))
            hsv = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2HSV)
            
            # Histogram Backprojection
            dst = cv2.calcBackProject([hsv], [0, 1], hist_skin, [0, 180, 0, 256], 1)
            dst_smooth = cv2.filter2D(dst, -1, disc)
            
            # Phân ngưỡng & Xử lý hình thái học
            _, mask = cv2.threshold(dst_smooth, 50, 255, cv2.THRESH_BINARY)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_morph, iterations=2)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_morph, iterations=2)
            
            # Tách bàn tay
            segmented = cv2.bitwise_and(frame_resized, frame_resized, mask=mask)
            
            # Vẽ khung ngắm lấy mẫu da ở giữa khung hình (hộp 80x80)
            cx, cy = 320, 240
            frame_display = frame_resized.copy()
            cv2.rectangle(frame_display, (cx - 40, cy - 40), (cx + 40, cy + 40), (0, 255, 0), 2)
            cv2.putText(frame_display, "ROI Target (Press 'c' to sample)", (cx - 110, cy - 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Ghép thành Dashboard 4 ô (2x2)
            dst_bgr = cv2.cvtColor(dst_smooth, cv2.COLOR_GRAY2BGR)
            mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            
            top_row = np.hstack((frame_display, dst_bgr))
            bottom_row = np.hstack((mask_bgr, segmented))
            dashboard = np.vstack((top_row, bottom_row))
            
            # Ghi chú tiêu đề trên dashboard
            cv2.putText(dashboard, "1. Camera goc & Khung ROI", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            cv2.putText(dashboard, "2. Ban do xac suat Backprojection", (660, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            cv2.putText(dashboard, "3. Mat na phan nguong Binary Mask", (20, 510), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            cv2.putText(dashboard, "4. Ban tay da tach nen (Segmented)", (660, 510), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            
            # Lưu các khung hình tiêu biểu để hiển thị trong Notebook
            if frame_count in [1, 30, 60, 90][:so_frame_demo]:
                frames_ket_qua.append({
                    'frame_num': frame_count,
                    'original': frame_resized.copy(),
                    'backproject': dst_smooth.copy(),
                    'mask': mask.copy(),
                    'segmented': segmented.copy()
                })
            
            # Nếu chạy trong môi trường GUI desktop:
            if che_do_gui:
                cv2.imshow("He thong phan doan ban tay thoi gian thuc", dashboard)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    print("Người dùng đã nhấn 'q' để thoát.")
                    break
                elif key == ord('c'):
                    # Lấy mẫu da mới từ khung ngắm trung tâm
                    roi_new = frame_resized[cy - 40:cy + 40, cx - 40:cx + 40]
                    hsv_new = cv2.cvtColor(roi_new, cv2.COLOR_BGR2HSV)
                    hist_skin = cv2.calcHist([hsv_new], [0, 1], None, [180, 256], [0, 180, 0, 256])
                    cv2.normalize(hist_skin, hist_skin, 0, 255, cv2.NORM_MINMAX)
                    print(f"-> Đã cập nhật mẫu da tay mới tại frame {frame_count}!")
            else:
                # Chạy mô phỏng đủ số frame demo thì dừng
                if frame_count >= 100 or len(frames_ket_qua) >= so_frame_demo:
                    break
                    
    finally:
        cap.release()
        if che_do_gui:
            cv2.destroyAllWindows()
            
    print(f"Đã xử lý xong video. Tổng số khung hình đã trích xuất: {len(frames_ket_qua)}")
    return frames_ket_qua

print("Đã xây dựng xong module phân đoạn bàn tay trên Video và Webcam!")
