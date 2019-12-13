import cv2 as cv
import numpy as np


def binary(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, bi_img = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print('threshold: ', ret)
    cv.imshow('bi', bi_img)


def custom_binary(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    mean = gray.mean()
    ret, bi_img = cv.threshold(gray, mean, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE)
    print('threshold: ', ret)
    cv.imshow('bi', bi_img)


def local_binary(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    bi_img = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow('bi', bi_img)


src = cv.imread('images/test.jpg')
print(src.shape)

cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

# binary(src)
# local_binary(src)
custom_binary(src)

cv.waitKey(0)

cv.destroyAllWindows()