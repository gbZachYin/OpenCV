import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def plot(img):
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show('hist')


def img_hist(img):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist(img, [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()



src = cv.imread('data/butterfly.jpg')
print(src.shape)

cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

# plot(src)
img_hist(src)

cv.waitKey(0)

cv.destroyAllWindows()