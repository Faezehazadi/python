import cv2
import numpy as np
import os

img = cv2.imread('input\digits.jpg')
print(img.shape)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
image_number = 0
folder_number = 0

for col in range(0, 1000, 20):
    for row in range(0, 2000, 20):
        digit = img[col: col + 20, row: row + 20]
        os.makedirs(f"output/num_{folder_number}",exist_ok=True)
        cv2.imwrite(f'output/num_{folder_number}/digit{folder_number}_{image_number}.jpg', digit)
        image_number += 1
        if image_number > 500:
            image_number = 1
            folder_number += 1