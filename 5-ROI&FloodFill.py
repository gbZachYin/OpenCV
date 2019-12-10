import cv2 as cv
import numpy as np

def ROI(img):
    part = img[50:250, 100:300]
    gray = cv.cvtColor(part, cv.COLOR_BGR2GRAY)
    backpart = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
    img[50:250, 100:300] = backpart
    cv.imshow('gray', gray)
    cv.imshow('changed', img)


def fill_color(img, cor_range):
    copy = img.copy()
    h, w = img.shape[:2]
    mask = np.zeros([h + 2, w + 2], np.uint8)
    cv.floodFill(copy, mask, cor_range, (255, 255, 0), (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('fill', copy)


def fill_binary():
    img = np.zeros([400, 400, 3], np.uint8)
    img[100:300, 100:300, : ] = 255
    cv.imshow('orin', img)
    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(img, mask, (200, 200), (100, 2, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow('filled', img)

src = cv.imread('images/test.jpg')
print(src.shape)

cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

# ROI(src)
# fill_color(src, (100, 200))
fill_binary()

cv.waitKey(0)

cv.destroyAllWindows()