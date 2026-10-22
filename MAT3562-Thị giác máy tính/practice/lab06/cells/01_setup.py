import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import glob
import math
import time
import warnings
warnings.filterwarnings('ignore')

# Cấu hình matplotlib
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

def cv2_imshow_safe(img, title=None, cmap=None):
    # Hàm hiển thị ảnh an toàn, tương thích cả Colab và Jupyter/VS Code
    plt.figure(figsize=(6, 6))
    if len(img.shape) == 3:
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    else:
        plt.imshow(img, cmap=cmap if cmap else 'gray')
    if title:
        plt.title(title, fontsize=12, fontweight='bold')
    plt.axis('off')
    plt.show()

print("OpenCV version:", cv2.__version__)
print("NumPy version :", np.__version__)
print("Thư mục làm việc hiện tại:", os.getcwd())
print("Môi trường và các thư viện hỗ trợ đã sẵn sàng!")
