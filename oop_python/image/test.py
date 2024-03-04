import numpy as np
from PIL import Image

# Create 3d numpy array of zeros, then replace zeros (black pixels) with yell pxls
data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255,255,0]
print(data)

# Make a red patch
data[1:3] = [255, 0, 0]
# data[:, 1:3] = [255, 0, 0] column
# data[1:3, 1:3]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')
