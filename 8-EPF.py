import cv2 as cv
import numpy as np


def bi(img):
    dst = cv.bilateralFilter(img,0, 100, 50)
    cv.imshow('bi', dst)


def shift(img):
    dst = cv.pyrMeanShiftFiltering(img, 10, 50)
    cv.imshow('shift', dst)

src = cv.imread('images/test.jpg')
print(src.shape)

cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

# bi(src)
shift(src)

cv.waitKey(0)

cv.destroyAllWindows()