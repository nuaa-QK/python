import cv2
import os
img = cv2.imread('1.jpg')

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# H空间中，绿色比黄色的值高一点，所以给每个像素+15，黄色的树叶就会变绿
turn_green_hsv = img_hsv.copy()
turn_green_hsv[:, :, 0] = (turn_green_hsv[:, :, 0]-15) % 180
turn_green_img = cv2.cvtColor(turn_green_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('turn_green.jpg', turn_green_img)

# 减小饱和度会让图像损失鲜艳，变得更灰
colorless_hsv = img_hsv.copy()
colorless_hsv[:, :, 1] = 0.5 * colorless_hsv[:, :, 1]
colorless_img = cv2.cvtColor(colorless_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('colorless.jpg', colorless_img)

# 减小明度为原来一半
darker_hsv = img_hsv.copy()
darker_hsv[:, :, 2] = 0.5 * darker_hsv[:, :, 2]+0.5 * colorless_hsv[:, :, 1]
#turn_green_hsv[:, :, 0] = (turn_green_hsv[:, :, 0]-15) % 180
darker_img = cv2.cvtColor(darker_hsv,cv2.COLOR_HSV2BGR)
#darker_img = cv2.cvtColor(turn_green_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite('darker.jpg', darker_img)
#print(darker_img)

import matplotlib.pyplot as plt

src=cv2.imread("1.jpg")
#均值滤波
dst = cv2.blur(src,(1,1))
cv2.imwrite("123.jpg",dst)
#中值滤波
dst1= cv2.medianBlur(src,3)
cv2.imwrite("dst1.jpg",dst1)
#高斯滤波
dst2=cv2.GaussianBlur(src,(3,3),0)
cv2.imwrite("dst2.jpg",dst2)
#双边滤波
#9 邻域直径,两个 75 分别是空间高斯函数标准差,灰度值相似性高斯函数标准差
dst3=cv2.bilateralFilter(src,9,65,65)
cv2.imwrite("dst3.jpg",dst3)
