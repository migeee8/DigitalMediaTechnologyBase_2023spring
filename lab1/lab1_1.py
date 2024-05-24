from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def my_histogram(image):
        # 创建储存灰度值的数组
        hist_array = np.zeros(256,dtype=int)
        # 遍历图像像素
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                gray_level = int(image[i,j])
                hist_array[gray_level]+=1
         # 设置绘图属性  
        plt.bar(range(256),hist_array)
        plt.title('Grayscale Histogram')
        plt.xlabel('Gray Level')
        plt.ylabel('Pixel Count')
        plt.show()

img = Image.open('./data/sample_gray.jpg')
img_array = np.asarray(img)
my_histogram(img_array)
