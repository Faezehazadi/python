import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('input/balloon.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(img)

lower_hue = np.array([160, 0, 0])
upper_hue = np.array([180, 255, 255])
mask = cv2.inRange(img, lower_hue, upper_hue)
img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
img = cv2.bitwise_and(img, img, mask = mask)

cv2.imwrite('output/balloon2.png', img)