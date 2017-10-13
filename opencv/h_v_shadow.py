import cv2
import numpy as np
import matplotlib.pyplot as plt

img_src = cv2.imread('img/V/IMG_2512.jpg', cv2.IMREAD_GRAYSCALE)

# 高斯模糊
img_blur = cv2.GaussianBlur(img_src, (5, 5), 1.5)
# 二值化
ret, img_ths = cv2.threshold(img_blur, 100, 200, cv2.THRESH_BINARY)

# Sobel算子边缘检测
x = cv2.Sobel(img_ths, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img_ths, cv2.CV_16S, 0, 1)
abs_x = cv2.convertScaleAbs(x)
abs_y = cv2.convertScaleAbs(y)
img_sob = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

height, width = img_src.shape
# print(height, width)

# 竖直水平方向投影
ver = np.zeros([width])

ver_shadow = np.zeros((height, width, 3), np.uint8)
for i in range(width):
    for j in range(height):
        if img_sob[j][i] == 0:
            ver[i] += 1
for i in range(width):
    for j in range(int(ver[i])):
        ver_shadow[j][i] = 255

# plt.imshow(ver_shadow, 'gray')
# plt.show()

# 最大序列子段和（step=180）
step = 180
temp = np.zeros([width - step])

for i in range(width - step):
    temp[i] = sum(ver[i:i+step])

l = list(temp)
maxSum = max(l)
index = l.index(maxSum)
print(maxSum, index)

# 定位轨枕的位置，绘图
img_bgr = cv2.imread('img/V/IMG_2512.jpg', cv2.IMREAD_COLOR)
img_rgb =(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
cv2.line(img_rgb, (index, 0), (index, height), (255, 255, 255), 9)
cv2.line(img_rgb, (index+step, 0), (index+step, height), (255, 255, 255), 9)

images = [img_src, img_sob, ver_shadow, img_rgb]
titles = ['gray', 'sobel', 'ver_shadow', 'location']

# for i in range(4):
#     plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()

#
#
#
#

# 二值化
ret2, img_ths2 = cv2.threshold(img_blur, 150, 200, cv2.THRESH_BINARY)

# Sobel算子边缘检测
x = cv2.Sobel(img_ths2, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img_ths2, cv2.CV_16S, 0, 1)
abs_x = cv2.convertScaleAbs(x)
abs_y = cv2.convertScaleAbs(y)
img_sob2 = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

height, width = img_src.shape

# 水平方向投影

width_left = 200

hor = np.zeros([height])
hor_shadow = np.zeros((height, width_left, 3), np.uint8)

for i in range(height):
    for j in range(width_left):
        if img_sob2[i][j] == 0:
            hor[i] += 1
for i in range(height):
    for j in range(int(hor[i])):
        hor_shadow[i][j] = 255

plt.plot(hor)
plt.show()

# 最大序列子段和（step=180）
step = 300
temp = np.zeros([height - step])

for i in range(height - step):
    temp[i] = sum(hor[i:i+step])

l = list(temp)
minSum = min(l)
index = l.index(minSum)
print(minSum, index)

# 定位轨枕的位置，绘图
cv2.line(img_rgb, (0, index), (width, index), (255, 255, 255), 9)
cv2.line(img_rgb, (0, index+step), (width, index+step), (255, 255, 255), 9)

images = [img_src, img_sob2, hor_shadow, img_rgb]
titles = ['gray', 'sobel', 'hor_shadow', 'location']

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


