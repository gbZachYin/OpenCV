import cv2 as cv
import numpy as np

def color_space_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('gray', gray)
    
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow('hsv', hsv)
    
    yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
    cv.imshow('yuv', yuv)

    Ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
    cv.imshow('Ycrcb', Ycrcb)


def extract_object():
    capture = cv.VideoCapture('videos/leaves.mp4')
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        low_hsv = np.array([35, 43, 46])
        high_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)
        dst = cv.bitwise_and(frame, frame, mask=mask)        
    
        cv.imshow('video', frame)
        cv.imshow('dst', dst)
        c = cv.waitKey(40)
        if c == 27:
            break



src = cv.imread('images/test.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

# b, g, r = cv.split(src)

# cv.imshow('blue', b)
# cv.imshow('green', g)
# cv.imshow('red', r)

# src[:, :, 1] = 0
# cv.imshow('changed image', src)

# src = cv.merge([b, g, r])
# cv.imshow('changed again image', src)
extract_object()

cv.waitKey(0)

cv.destroyAllWindows()