import cv2

from matplotlib import pyplot as plt

import cv2
import numpy as np
import matplotlib.pyplot as plt

img_src = cv2.imread('img/V/IMG_2512.jpg', cv2.IMREAD_GRAYSCALE)

img_can = cv2.Canny(img_src, 50, 150, apertureSize=5)

width, hight = img_src.shape

print(width, hight)

v = np.zeros([width])


v_shadow = np.zeros((width, hight, 1), np.uint8)

for i in range(width):
    for j in range(hight):
        if img_can[i][j] == 0:
            v[i] += 1

for i in range(width):
    for j in range(int(v[i])):
        v_shadow[i][j] = 255

images = [img_src, img_can, img_can]
titles = ['gray', 'canny', 'v_shadow']
for i in range(3):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
