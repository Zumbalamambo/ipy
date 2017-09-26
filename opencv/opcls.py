import cv2

from matplotlib import pyplot as plt


img = cv2.imread('img/V/IMG_2512.jpg', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('img/V/IMG_2512.jpg')

# 构造5×5的结构元素，分别为十字形、菱形、方形和X型
cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
# 菱形结构元素的定义稍麻烦一些
diamond = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
diamond[0, 0] = 0
diamond[0, 1] = 0
diamond[1, 0] = 0
diamond[4, 4] = 0
diamond[4, 3] = 0
diamond[3, 4] = 0
diamond[4, 0] = 0
diamond[4, 1] = 0
diamond[3, 0] = 0
diamond[0, 3] = 0
diamond[0, 4] = 0
diamond[1, 4] = 0
square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
x = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
# 使用cross膨胀图像
result1 = cv2.dilate(img, cross)
# 使用菱形腐蚀图像
result1 = cv2.erode(result1, diamond)

# 使用X膨胀原图像
result2 = cv2.dilate(img, x)
# 使用方形腐蚀图像
result2 = cv2.erode(result2, square)

# result = result1.copy()
# 将两幅闭运算的图像相减获得角
result = cv2.absdiff(result2, result1)
# 使用阈值获得二值图
retval, result = cv2.threshold(result, 10, 255, cv2.THRESH_BINARY)

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()