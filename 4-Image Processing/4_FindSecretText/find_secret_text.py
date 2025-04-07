import cv2

img_1 = cv2.imread('inputs/a.jpg')
img_2 = cv2.imread('inputs/b.jpg')

result = img_2 - img_1
cv2.imwrite('output/find_secret_pic.jpg', result)


