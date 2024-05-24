from PIL import Image
import numpy as np

original_image = Image.open('./data/unsplash_resized.bmp')
watermark_image = Image.open('./data/mask.png')
original_image = original_image.convert('RGB')
watermark_image = watermark_image.resize(original_image.size)

original_pixels = np.array(original_image)
watermark_pixels = np.array(watermark_image.convert('1'))  # 将水印图像转换为二值图像

for i in range(original_pixels.shape[0]):
        for j in range(original_pixels.shape[1]):
            r_original, g_original, b_original = original_pixels[i, j]
            watermark_pixel = watermark_pixels[i, j]

            # 将水印图像的像素值的最低有效位写入原始图像的红色通道的最低有效位
            r_original = (r_original & 0xFE) | (watermark_pixel & 1)

            original_pixels[i, j] = [r_original, g_original, b_original]

watermarked_image = Image.fromarray(original_pixels)
watermarked_image.save('./data/watermarked_image.png')