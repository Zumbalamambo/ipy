import cv2
import numpy as np

from matplotlib import pyplot as plt


def bgr2rgb(src):
    img = src.copy()
    img[:,:,0] = src[:,:,2]
    img[:,:,2] = src[:,:,0]
    return img

img = cv2.imread("track.bmp")

k = 9
kernel = np.ones((k, k), np.float32)/k**2
print(kernel)


