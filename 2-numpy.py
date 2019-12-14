import cv2 as cv
import numpy as np


def create_image():
    img = np.zeros([400, 400, 3], np.uint8)
    img[: , : , 0] = np.ones([400, 400]) * 255
    cv.imshow("test", img)


def alter_pixels(image):
    print(image.shape)
    height, width, channels = image.shape[0], image.shape[1], image.shape[2]
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pixel = image[row, col, c]
                image[row, col, c] = 255 - pixel
    cv.imshow('alterred', image)
                

print  ("Hello OpenCV")

image_add = 'images/nice_bra.jpg'

src = cv.imread(image_add)
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
create_image()
alter_pixels(src)
cv.waitKey(0)
cv.destroyAllWindows()