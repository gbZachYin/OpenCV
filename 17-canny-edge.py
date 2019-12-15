import cv2 as cv
import numpy as np


def edge(img):
    blur = cv.GaussianBlur(img, (3, 3), 0)
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)

    output = cv.Canny(grad_x, grad_y, 50, 150)
    cv.imshow('Canny', output)

    color_output = cv.bitwise_and(img, img, mask=output)
    cv.imshow('color', color_output)



src = cv.imread('images/test.jpg')
print(src.shape)

cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

edge(src)

cv.waitKey(0)

cv.destroyAllWindows()