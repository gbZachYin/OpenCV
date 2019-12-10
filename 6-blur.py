import cv2 as cv
import numpy as np

def blur(img):
    dst = cv.blur(img, (5, 5))
    cv.imshow('blur', dst)


def median_blur(img):
    dst = cv.medianBlur(img, 5)
    cv.imshow('median', dst) 


def custom_blur(img):
    # kernel = np.ones([5, 5], np.float32) / 25
    # kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1], ], np.float32) / 9
    # 和等于1 锐化, 等于0 梯度
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0], ], np.float32)
    
    dst = cv.filter2D(img, -1, kernel=kernel)
    cv.imshow('custom_blur', dst) 


src = cv.imread('images/test.jpg')
print(src.shape)

cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

# blur(src)
# median_blur(src)
custom_blur(src)


cv.waitKey(0)

cv.destroyAllWindows()