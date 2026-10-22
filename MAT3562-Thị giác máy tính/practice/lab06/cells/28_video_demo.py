# Thử nghiệm chạy module trên nguồn Video (sử dụng video thực tế ../lab04/video.mp4)
video_path = '../lab04/video.mp4'
if os.path.exists(video_path):
    print(f"Đang thực hiện phân đoạn bàn tay trên file video thực tế: {video_path}")
    demo_frames = phan_doan_ban_tay_video_webcam(nguon_video=video_path, so_frame_demo=3, che_do_gui=False)
else:
    print(f"Không tìm thấy video tại {video_path}, chạy thử nghiệm trên nguồn webcam...")
    demo_frames = phan_doan_ban_tay_video_webcam(nguon_video=0, so_frame_demo=3, che_do_gui=False)

# Trực quan hóa các khung hình tiêu biểu đã xử lý từ video
if demo_frames:
    fig, axes = plt.subplots(len(demo_frames), 4, figsize=(16, 4 * len(demo_frames)))
    if len(demo_frames) == 1:
        axes = np.expand_dims(axes, 0)
        
    for r, f_info in enumerate(demo_frames):
        # 1. Camera gốc
        axes[r, 0].imshow(cv2.cvtColor(f_info['original'], cv2.COLOR_BGR2RGB))
        axes[r, 0].set_title(f"Frame #{f_info['frame_num']}: Khung hình gốc", fontweight='bold')
        axes[r, 0].axis('off')
        
        # 2. Backprojection
        axes[r, 1].imshow(f_info['backproject'], cmap='gray')
        axes[r, 1].set_title(f"Frame #{f_info['frame_num']}: Backprojection", fontweight='bold')
        axes[r, 1].axis('off')
        
        # 3. Binary mask
        axes[r, 2].imshow(f_info['mask'], cmap='gray')
        axes[r, 2].set_title(f"Frame #{f_info['frame_num']}: Binary Mask", fontweight='bold')
        axes[r, 2].axis('off')
        
        # 4. Segmented
        axes[r, 3].imshow(cv2.cvtColor(f_info['segmented'], cv2.COLOR_BGR2RGB))
        axes[r, 3].set_title(f"Frame #{f_info['frame_num']}: Bàn tay tách nền", fontweight='bold')
        axes[r, 3].axis('off')
        
    fig.suptitle("KẾT QUẢ PHÂN ĐOẠN BÀN TAY LIÊN TỤC TRÊN CÁC KHUNG HÌNH VIDEO THỜI GIAN THỰC", 
                 fontsize=14, fontweight='bold', y=1.01)
    plt.tight_layout()
    plt.show()
