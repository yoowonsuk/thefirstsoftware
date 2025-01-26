import cv2
import numpy as np

foreground = cv2.imread('giraffe.jpeg')
background = cv2.imread('safari.jpeg')

print(foreground[40, 40]) # 28 255 76 => green
width = foregrdound.shape[1]
height = foregrdound.shape[0]
print(foreground.shape)

resized_background = cv2.resize(background, (width, height))

for i in range(width):
    for j in range(height):
        pixel = foreground[j, i]
#        print(type(pixel)) # <class 'numpy.ndarray'>
        #if list(pixel) == [28, 255, 76]:
        #if np.all(pixel == [28, 255, 76]):
        #if np.any(pixel == [28, 255, 76]):
        if np.any(pixel == [1, 255, 1]):
            #foreground[j, i] = background[j][i]
            foreground[j, i] = resized_background[j][i]

cv2.imwrite('output.jpen', foreground)

