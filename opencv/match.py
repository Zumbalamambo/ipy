import cv2

from matplotlib import pyplot as plt

import os.path


# 通道转换，opencv 默认为BGR； matlib 默认为RGB
def bgr2rgb(src):
    dst = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
    return dst


def template_match(src, temp):

    w, h = temp.shape[::-1]

    # 六种匹配算法
    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    methods = ['cv2.TM_SQDIFF']

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

        # plt.subplot(221), plt.imshow(src, 'gray'), plt.title('Original Image')
        # plt.subplot(222), plt.imshow(temp, 'gray'),  plt.title('template Image')
        # plt.subplot(223), plt.imshow(res, 'gray'),  plt.title('Matching Result')
        # plt.subplot(224), plt.imshow(src2, 'gray'),  plt.title('Detected Point')
        # plt.show()

        return src2


def plt_imgs(nx, ny, img_list):
    f, axes = plt.subplots(nx, ny, sharex = True, sharey = True)
    for rows in axes:
        for col in rows:
            item = img_list.pop()
            col.imshow(item, 'gray')

    plt.show()


def template_all():
    rootdir = 'img/V/'

    template = cv2.imread('img/sample.jpg', cv2.IMREAD_GRAYSCALE)
    template_gb = cv2.GaussianBlur(template, (3, 3), 1.5)


    img_lists = []
    for parent, dirnames, filenames in os.walk(rootdir):
        for fn in filenames:
            filedir = rootdir + fn
            img = cv2.imread(filedir, cv2.IMREAD_COLOR)
            img_rgb = bgr2rgb(img)
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img_gray_gb = cv2.GaussianBlur(img_gray, (3, 3), 1.5)

            match2 = template_match(img_gray_gb, template_gb)
            img_lists.append(match2)

    plt_imgs(4, 5, img_lists)


if __name__ == '__main__':
    template_all()
