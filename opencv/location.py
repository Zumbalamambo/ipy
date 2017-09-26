import cv2
import numpy as np

from matplotlib import pyplot as plt


# Sobel算子： 先对x方向，y方向求导（梯度），然后权重相加
def sobel(src):
    x = cv2.Sobel(src, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(src, cv2.CV_16S, 0, 1)
    abs_x = cv2.convertScaleAbs(x)
    abs_y = cv2.convertScaleAbs(y)

    dst = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    return dst


img = cv2.imread('img/V/IMG_2479.jpg', cv2.IMREAD_GRAYSCALE)

img_color = cv2.imread('img/V/IMG_2479.jpg')

gauss = cv2.bilateralFilter(img, 3, 50, 50)

sob = sobel(img)


# 经验参数
minLength = 8000
maxGap = 25
lines = cv2.HoughLinesP(sob, 1, np.pi / 180, 200, minLength, maxGap)

print(np.shape(lines))
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(img_color, (x1, y1), (x2, y2), (0, 0, 255), 1)

#
# plt.subplot(221), plt.imshow(source, 'gray'), plt.title('source')
# plt.xticks([]), plt.yticks([])  # 去掉坐标轴刻度
# plt.subplot(222), plt.imshow(gauss, 'gray'), plt.title('gauss')
# plt.xticks([]), plt.yticks([])
# plt.subplot(223), plt.imshow(canny, 'gray'), plt.title('canny')
# plt.xticks([]), plt.yticks([])
# plt.subplot(224), plt.imshow(img), plt.title('img')
# plt.xticks([]), plt.yticks([])
# plt.show()


cv2.imshow('Result', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
