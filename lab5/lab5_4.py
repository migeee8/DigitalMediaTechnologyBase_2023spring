from PIL import Image
import numpy as np


watermarked_image = Image.open('./data/watermarked_image.png')
watermarked_image = watermarked_image.convert('RGB')
pixels = np.array(watermarked_image)
watermark_pixels = np.zeros_like(pixels, dtype=np.uint8)
for i in range(pixels.shape[0]):
    for j in range(pixels.shape[1]):
        r_watermark = pixels[i, j, 0] & 1
        watermark_pixels[i, j] = [255 * r_watermark, 255 * r_watermark, 255 * r_watermark]
watermark_image = Image.fromarray(watermark_pixels)

watermark_image.save('./data/extracted_watermark.png')
