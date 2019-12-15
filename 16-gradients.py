import cv2 as cv
import numpy as np


def custom(img):
    kernel = np.array([
        [1, 1, 1],
        [1, -8, 1],
        [1, 1, 1]
    ])
    dst = cv.filter2D(img, cv.CV_32F, kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('lpls', lpls)


def laplace(img):
    dst = cv.Laplacian(img, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow('lpls', lpls)


def sobel(img):
    grad_x = cv.Sobel(img, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(img, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow('gradx', gradx)
    cv.imshow('grady', grady)

    grad = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow('gradient', grad)

src = cv.imread('data/lena.jpg')
print(src.shape)

cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)


# sobel(src)
# laplace(src)
custom(src)

cv.waitKey(0)

cv.destroyAllWindows()