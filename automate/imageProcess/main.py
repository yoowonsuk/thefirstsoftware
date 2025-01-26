import cv2 # opencv-python (python3 -m poetry add opencv-python)
dir(cv2)

color = cv2.imread('galaxy.jpeg', 1) #grey 0
print(color.ndim) # 3
print(type(color)) # <class 'numpy.darray'>

cv2.imwrite('galaxy-gray.jpeg', color)

import os
import cv2
images = os.listdir('images') #folder
for image in images:
    gray = cv2.imread(f'images/{image}', 0)
    cv2.imwrite(f'grayimages/gray-(image)', gray)

import cv2
image = cv2.imread('galaxy.jpeg')
print(image.shape) # height, width, pixel

def calculate_size(scale_percentage, width, height):
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    return (new_width, new_height)

print(calculate_size(10, image.shape[1], image.shape[0]))

def resize(image_path, scale_percentage, resized_path):
    image = cv2.imread('galaxy.jpeg')
    new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dim)
    cv2.imwrite(resized_path, resized_image)


resize('galaxy.jpeg', 10, 'resized-galaxy.jepg')

import os
images = os.listdir('images')
for image in images:
    resize(f'images/{image}', 10, f'resized/resized-{image}')
