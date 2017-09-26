import cv2

from matplotlib import pyplot as plt


# 初级滤波功能
# blur: 每个像素的权重是相同的，线性
# GaussianBlur: 像素的权重与其距中心像素的距离成比例
# medianBlur: 以中值点作为中心点的值, 不用最大或最小值, 用于消除椒盐噪音
# 双边滤波: 考虑了像素间的几何距离和色彩距离,对图像进行平滑时能保护边缘
def blur(src):
    blur_dst = cv2.blur(src, (5, 5))
    gaussblur_dst = cv2.GaussianBlur(src, (5, 5), 1.5)
    medianblur_dst = cv2.medianBlur(src, 5)
    bilateral_dst = cv2.bilateralFilter(src, 7, 75, 75)

    plt.subplot(231), plt.imshow(src, 'gray'), plt.title('Original')
    plt.xticks([]), plt.yticks([])  # 去掉坐标轴刻度
    plt.subplot(232), plt.imshow(blur_dst, 'gray'), plt.title('Blur_Filtering')
    plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(gaussblur_dst, 'gray'), plt.title('Gaussian_Blur_Filtering')
    plt.xticks([]), plt.yticks([])
    plt.subplot(234), plt.imshow(medianblur_dst, 'gray'), plt.title('Median_Blur_Filtering')
    plt.xticks([]), plt.yticks([])
    plt.subplot(235), plt.imshow(bilateral_dst, 'gray'), plt.title('Bilateral_Blur_Filtering')
    plt.xticks([]), plt.yticks([])
    plt.show()
    return


# Sobel算子： 先对x方向，y方向求导（梯度），然后权重相加
def sobel(src):
    x = cv2.Sobel(src, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(src, cv2.CV_16S, 0, 1)
    abs_x = cv2.convertScaleAbs(x)
    abs_y = cv2.convertScaleAbs(y)

    dst = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    return dst


# Laplacian算子：先用Sobel 算子计算二阶x和y导数，再求和
def laplas(src):
    # 先用GaussianBlur除噪
    gauss_blur = cv2.GaussianBlur(src, (3, 3), 0)

    gray_lap = cv2.Laplacian(gauss_blur, cv2.CV_16S, ksize=3)
    dst = cv2.convertScaleAbs(gray_lap)
    return dst


# Canny 边缘检测： 采用双阈值法，先用高阈值将边缘链接成轮廓，在轮廓的端点处寻找满足低阈值的点，使边缘闭合
def canny(src):
    dst = cv2.Canny(src, 50, 150, apertureSize=3)
    return dst


# Sobel, Laplas, Canny
def slc(src):
    sss = src.copy()
    sob = sobel(src)
    lpls = laplas(src)
    can = canny(src)

    _, ths = cv2.threshold(sob, 70, 200, cv2.THRESH_BINARY)

    plt.subplot(231), plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)), plt.title('Color')
    plt.xticks([]), plt.yticks([])  # 去掉坐标轴刻度
    plt.subplot(232), plt.imshow(src, 'gray'), plt.title('Gray')
    plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(sob, 'gray'), plt.title('Sobel')
    plt.xticks([]), plt.yticks([])
    plt.subplot(234), plt.imshow(lpls, 'gray'), plt.title('Laplas')
    plt.xticks([]), plt.yticks([])
    plt.subplot(235), plt.imshow(can, 'gray'), plt.title('Canny')
    plt.xticks([]), plt.yticks([])
    plt.subplot(236), plt.imshow(ths, 'gray'), plt.title('Sob_ths')
    plt.xticks([]), plt.yticks([])

    plt.show()

    return


if __name__ == '__main__':
    img = cv2.imread('img/V/IMG_2512.jpg', cv2.IMREAD_GRAYSCALE)
    img_color = cv2.imread('img/V/IMG_2512.jpg')
    # dst = cv2.GaussianBlur(img, (3, 3), 1.5)

    dst = cv2.bilateralFilter(img, 5, 75, 75)
    slc(dst)

    res = cv2.equalizeHist(dst)
    slc(res)

