import numpy as np
import cv2
import matplotlib.pyplot as plt

def my_hist_equal(img):
    # 计算直方图
    hist, bins = np.histogram(img.flatten(), 256, [0, 255])
    # 计算累积分布函数
    cdf = hist.cumsum()
    # 计算累积分布频率函数
    cdf_normalized = cdf / cdf.max()
    # 均衡化
    img2 = np.uint8(255 * cdf_normalized[img]+0.5)


    # 绘制原始图像的直方图和均衡化后的直方图
    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.subplot(2, 2, 2)
    plt.hist(img.flatten(), 256, [0, 255], color='r')
    plt.xlim([0, 256])
    plt.subplot(2, 2, 3)
    plt.imshow(img2, cmap='gray')
    plt.subplot(2, 2, 4)
    plt.hist(img2.flatten(), 256, [0, 255], color='r')
    plt.xlim([0, 256])
    plt.show()

# 加载图像
img = cv2.imread('./data/gray.bmp', cv2.IMREAD_GRAYSCALE)

# 调用 my_hist_equal 函数
my_hist_equal(img)