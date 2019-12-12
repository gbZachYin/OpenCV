import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def hist2d(img):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    plt.imshow(hist, interpolation='nearest')
    plt.title('2d hist')
    plt.show()


def back_proj(sample, target):
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    cv.imshow('sample', sample)
    cv.imshow('target', target)

    roi_hist = cv.calcHist([roi_hsv], [0, 1], None, [32, 32], [0, 180, 0, 256])
    cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)
    mask = cv.calcBackProject([target_hsv], [0, 1], roi_hist, [0, 180, 0, 256], 1)
    dst = cv.bitwise_and(target, target, mask=mask)
    cv.imshow('back', dst)


src_target = cv.imread('data/rubberwhale1.png')
src_sample = cv.imread('images/target.png')
print(src_sample.shape)

# cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
# hist2d(src)
back_proj(src_sample, src_target)

cv.waitKey(0)

cv.destroyAllWindows()