import cv2 as cv
import numpy as np


def big_img_binary(img):
    ch, cw = 127, 127
    h, w = img.shape[:2]
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row: row + ch, col: col + cw]
            # dev = np.std(roi)
            # if dev < 15:
            #     dst = 255
            # else :
            ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
            gray[row: row + ch, col: col + cw] = dst
    cv.imwrite('images/result.png', gray)


def big_img_local_binary(img):
    ch, cw = 255, 255
    h, w = img.shape[:2]
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row: row + ch, col: col + cw]
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 127, 20)
            gray[row: row + ch, col: col + cw] = dst
    cv.imwrite('images/loca_result.png', gray)


src = cv.imread('images/nice_bra.jpg')
print(src.shape)

# cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input image', src)

# big_img_local_binary(src)
big_img_binary(src)

cv.waitKey(0)

cv.destroyAllWindows()