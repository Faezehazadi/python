import cv2
import numpy as np

def rgb_to_gray(image):
    height, width, channels = image.shape
    gray_image = np.zeros((height, width), dtype =np.uint8)
    for y in range(height):
        for x in range(width):
            r, g, b = image[y, x]
            gray_value = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
            gray_image[y, x] = gray_value

    return gray_image

img = cv2.imread('input/pic.jpg')
img = rgb_to_gray(img)
cv2.imwrite('output/pic2.jpg', img)