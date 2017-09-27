import cv2

from matplotlib import pyplot as plt

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('img/V/IMG_2512.jpg', cv2.IMREAD_GRAYSCALE)

# opencv方法读取-cv2.calcHist（速度最快）
# 图像，通道[0]-灰度图，掩膜-无，灰度级，像素范围
hist_cv = cv2.calcHist([img], [0], None, [256], [0, 256])

# numpy方法读取-np.histogram()
hist_np, bins = np.histogram(img.ravel(), 256, [0, 256])

# numpy的另一种方法读取-np.bincount()（速度=10倍法2）
hist_np2 = np.bincount(img.ravel(), minlength=256)
plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.plot(hist_cv)
plt.subplot(223), plt.plot(hist_np)
plt.subplot(224), plt.plot(hist_np2)
plt.show()






'''
int
i, j;
// 垂直方向进行累加（积分）
for (i=0; i < src_binary.cols; i++) // 列
{
for (j=0; j < src_binary.rows; j++) // 行
{
if ( src_binary.at < uchar > ( j, i ) == 0) // 统计的是黑色像素的数量
v[i]++;
}
}
// 绘制垂直方向上的投影
for (i=0; i < src_binary.cols; i++)
{
for (j=0; j < v[i]; j++)
{
paintX.at < uchar > ( j, i ) = 255; // 填充白色的像素
}
}
// 水平方向进行累加（积分）
for (i=0; i < src_binary.rows; i++) // 行
{
for (j=0; j < src_binary.cols; j++) // 列
{
if ( src_binary.at < uchar > ( i, j ) == 0) // 统计黑色像素的数量
h[i]++;
}
}
// 绘制水平方向上的投影
for (i=0; i < src_binary.rows; i++)
{
for (j=0; j < h[i]; j++)
{
paintY.at < uchar > ( i, j ) = 255; // 填充白色的像素
}
} 
'''