import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)
    while(True):
        ret, frame = capture.read()
        frame = cv.flip(frame, 1)
        cv.imshow('video', frame)
        c = cv.waitKey(50)
        if c == 27:
            break

def get_image_info(img):
    print(type(img))
    print(img.shape)
    print(img.size)
    print(img.dtype)
    pixel_data = np.array(img)
    print(pixel_data)


def save_gray(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite('images/gray.png', gray)


print  ("Hello OpenCV")

image_add = 'images/nice_bra.jpg'

src = cv.imread(image_add)
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

get_image_info(src)

cv.waitKey(0)
cv.destroyAllWindows()