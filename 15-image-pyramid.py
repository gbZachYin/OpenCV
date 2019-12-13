import cv2 as cv
import numpy as np


def pyramid(img):
    level = 3
    temp = img.copy()
    pyramids = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramids.append(dst)
        cv.imshow(str(i), dst)
        temp = dst.copy()
    return pyramids


def laplace(img):
    pyramids = pyramid(img)
    pyramids.reverse()
    for i in range(len(pyramids)):
        if i == 2:
            temp = cv.pyrUp(pyramids[i], dstsize=img.shape[:2])
            lpls = cv.subtract(img, temp)
        else:
            temp = cv.pyrUp(pyramids[i], dstsize=pyramids[i + 1].shape[:2])
            lpls = cv.subtract(pyramids[i + 1], temp)
        cv.imshow('lpls: ' + str(i), lpls)



src = cv.imread('data/lena.jpg')
print(src.shape)

cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

laplace(src)

cv.waitKey(0)

cv.destroyAllWindows()