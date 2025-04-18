import cv2
import numpy as np 
import matplotlib.pyplot as plt
import random
from PIL import Image, ImageDraw
import imageio

tvscreen = []

for i in range(45):
    tv = cv2.imread('input/tv.jpg', cv2.IMREAD_GRAYSCALE)
    roi = tv[45:310, 40:380]
    noisysc = np.zeros((roi.shape[0], roi.shape[1]), dtype='uint8')
    row, col = noisysc.shape
    for i in range(1, row-1):
        for j in range(1, col-1):
            noisysc[i][j] = random.choice([0, 255])
    tv[45:310, 40:380] = noisysc
    tvscreen.append(tv)
    
imageio.mimwrite('output/tvscreen1.gif', tvscreen)
cv2.waitKey()