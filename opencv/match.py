import cv2
import numpy as np

from matplotlib import pyplot as plt


# 通道转换，opencv 默认为BGR； matlib 默认为RGB
def bgr2rgb(src):
    dst = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
    return dst


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

    plt.subplot(231), plt.imshow(src, "gray"), plt.title("Original")
    plt.xticks([]), plt.yticks([])  # 去掉坐标轴刻度
    plt.subplot(232), plt.imshow(blur_dst, "gray"), plt.title("Blur_Filtering")
    plt.xticks([]), plt.yticks([])
    plt.subplot(233), plt.imshow(gaussblur_dst, "gray"), plt.title("Gaussian_Blur_Filtering")
    plt.xticks([]), plt.yticks([])
    plt.subplot(234), plt.imshow(medianblur_dst, "gray"), plt.title("Median_Blur_Filtering")
    plt.xticks([]), plt.yticks([])
    plt.subplot(235), plt.imshow(bilateral_dst, "gray"), plt.title("Bilateral_Blur_Filtering")
    plt.xticks([]), plt.yticks([])
    plt.show()
    return


# Sobel算子： 先对x方向，y方向求导（梯度），然后权重相加
def sober(src):
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
    gauss_blur = cv2.GaussianBlur(src, (3, 3), 0)
    dst = cv2.Canny(gauss_blur, 50, 150)
    return dst


# Sobel, Laplas, Canny
def slc(src):
    sob = sober(src)
    lpls = laplas(src)
    can = canny(src)

    plt.subplot(221), plt.imshow(src, 'gray'), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(sob, 'gray'), plt.title('Sobel')
    plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(lpls, 'gray'), plt.title('Laplas')
    plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(can, 'gray'), plt.title('Canny')
    plt.xticks([]), plt.yticks([])
    plt.show()
    return


def template_match(src, temp):

    w, h = temp.shape[::-1]

    # 六种匹配算法
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    for meth in methods:
        src2 = src.copy()

        method = eval(meth)

        res = cv2.matchTemplate(src, temp, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(src2, top_left, bottom_right, 255, 5)

        print(meth)

        plt.subplot(221), plt.imshow(src, 'gray'), plt.title('Original Image')
        plt.subplot(222), plt.imshow(temp, 'gray'),  plt.title('template Image')
        plt.subplot(223), plt.imshow(res, 'gray'),  plt.title('Matching Result')
        plt.subplot(224), plt.imshow(src2, 'gray'),  plt.title('Detected Point')
        plt.show()


if __name__ == '__main__':

    img = cv2.imread('img/H/IMG_2482.jpg', cv2.IMREAD_COLOR)
    img_rgb = bgr2rgb(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray2 = cv2.imread('img/H/IMG_2482.jpg', cv2.IMREAD_GRAYSCALE)

    # plt.subplot(221), plt.imshow(img), plt.title('Original_BGR')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(222), plt.imshow(img_rgb), plt.title('PLOT_RGB')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(223), plt.imshow(img_gray, 'gray'), plt.title('GRAY')
    # plt.xticks([]), plt.yticks([])
    # plt.subplot(224), plt.imshow(img_gray2, 'gray'), plt.title('GRAY2')
    # plt.xticks([]), plt.yticks([])
    # plt.show()

    # blur(img_gray)
    # slc(img_gray)

    template = cv2.imread('img/sample.jpg', cv2.IMREAD_GRAYSCALE)

    template_match(img_gray, template)


