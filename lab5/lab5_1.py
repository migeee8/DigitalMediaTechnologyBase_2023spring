from PIL import Image
import numpy as np

cover = Image.open('./data/unsplash_resized.bmp')
cover = cover.convert('RGB')
msg = Image.open('./data/mask.png')
msg = msg.convert('1')

msg = np.asarray(msg)

cover = np.asarray(cover)
cover = np.copy(cover)

for i in range(cover.shape[0]):
    for j in range(cover.shape[1]):
        if cover[i, j, 0] % 2 == 1:
            if cover[i, j, 0] != 255:
                cover[i, j, 0] += 1
            else:
                cover[i, j, 0] -= 1
        if msg[i, j]:
            cover[i, j, 0] += 1

cover = Image.fromarray(np.uint8(cover))
cover.save('./data/encoded_cover.png')
