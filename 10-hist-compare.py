import cv2 as cv
import numpy as np


def equalHist(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow('equal', dst)


def clahe(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(5.0, (8, 8))
    dst = clahe.apply(gray)
    cv.imshow('equal', dst)


def create_rgb_hist(img):
    h, w, c = img.shape
    rgbHist = np.zeros([16 * 16 * 16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = img[row, col, 0]
            g = img[row, col, 1]
            r = img[row, col, 2]
            index = np.int(b / bsize) * 16 * 16 + np.int(g / bsize) * 16 + np.int(r / bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist



def hist_compare(img1, img2):
    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    hist1 = create_rgb_hist(img1)
    hist2 = create_rgb_hist(img2)
    match_bhat = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match_cor = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match_chi = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print('Bath: ', match_bhat)
    print('Cor: ', match_cor)
    print('Chi: ', match_chi)



src1 = cv.imread('data/opencv-logo-white.png')
src2 = cv.imread('data/opencv-logo.png')


cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input image', src1)

# equalHist(src)
# clahe(src)
hist_compare(src1, src2)

cv.waitKey(0)

cv.destroyAllWindows()