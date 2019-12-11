import cv2 as cv
import numpy as np


def guass_blur(img):
    dst = cv.GaussianBlur(img, (5, 5), 0)
    cv.imshow('guass blur', dst)


def control(value):
    if value > 255:
        return 255
    if value < 0:
        return 0
    return value


def guass_noise(img):
    h, w, c = img.shape
    for row in range(h):
        for col in range(w):
            noise = np.random.normal(0, 20, 3)
            b = img[row, col, 0]
            g = img[row, col, 1]
            r = img[row, col, 2]
            img[row, col, 0] = control(b + noise[0]) 
            img[row, col, 1] = control(g + noise[1])
            img[row, col, 2] = control(r + noise[2])
    cv.imshow('noise', img)
    return img

src = cv.imread('images/test.jpg')
print(src.shape)

cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

noise_pic = guass_noise(src)
guass_blur(noise_pic)

cv.waitKey(0)

cv.destroyAllWindows()