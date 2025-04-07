import cv2
img = cv2.imread("pic.jpg", 0)

treshold = 180
height, width = img.shape

for i in range (height):
    for j in range(width):
        img[i, j] = 255 - img[i, j]

img = cv2.resize(img, (400,400))
cv2.imshow("output", img)
cv2.waitKey()
cv2.imwrite("new_pic.jpg", img)        