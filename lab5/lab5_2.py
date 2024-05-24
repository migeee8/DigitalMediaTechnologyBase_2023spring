from PIL import Image
import numpy as np
encoded = Image.open('./data/encoded_cover.png')
encoded = encoded.convert('RGB')
encoded = np.asarray(encoded)
decoded = np.random.randint(0, 1, size=(encoded.shape[0], encoded.shape[1]))
for i in range(encoded.shape[0]):
    for j in range(encoded.shape[1]):
        if encoded[i,j,0] % 2 == 1:
            decoded[i,j] = 1
        else:
            decoded[i,j] = 0
cover = Image.fromarray(np.bool_(decoded))
cover.save('./data/decoded.png')