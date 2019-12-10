import cv2 as cv
import numpy as np


def add(img1, img2):
    dist = cv.add(img1, img2)
    cv.imshow('add', dist)


def subtract(img1, img2):
    dist = cv.subtract(img1, img2)
    cv.imshow('substract', dist)


def multiply(img1, img2):
    dist = cv.multiply(img1, img2)
    cv.imshow('multiply', dist)


def divide(img1, img2):
    dist = cv.divide(img1, img2)
    cv.imshow('divide', dist)


def others(img):
    m, std = cv.meanStdDev(img)
    print(m, std)


def logic(img1, img2):
    dst = cv.bitwise_and(img1, img2)
    cv.imshow('and', dst)
    dst = cv.bitwise_or(img1, img2)
    cv.imshow('or', dst)
    dst = cv.bitwise_not(img2)
    dst = cv.imshow('not', dst)


def contrast_brightness(img, c, b):
    blank = np.zeros(img.shape, img.dtype)
    dst = cv.addWeighted(img, c, blank, 1-c, b)
    cv.imshow('con-bri', dst)



src_win = cv.imread('data/WindowsLogo.jpg')
src_lnx = cv.imread('data/LinuxLogo.jpg')

print(src_lnx.shape[:2])

# print(src_win.shape, src_lnx.shape)


# cv.namedWindow('input image1', cv.WINDOW_AUTOSIZE)
cv.imshow('input image1', src_win)
cv.imshow('input image2', src_lnx)

# add(src_lnx, src_win)
# subtract(src_lnx, src_win)
# multiply(src_lnx, src_win)
# divide(src_lnx, src_win)
# others(src_lnx)
# others(src_win)
# logic(src_lnx, src_win)
# contrast_brightness(src_win, 1.2, 10)

cv.waitKey(0)

cv.destroyAllWindows()