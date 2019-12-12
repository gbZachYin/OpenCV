import cv2 as cv
import numpy as np


def template(temp, target):
    cv.imshow("template image",temp)
    cv.imshow("target image",target)
    
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    
    temp_h, temp_w = temp.shape[:2]
    
    for method in methods:
        result = cv.matchTemplate(target, temp, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        
        if method == cv.TM_SQDIFF_NORMED:
            top_left = min_loc    
        else:
            top_left = max_loc
        down_right = (top_left[0] + temp_w, top_left[1] + temp_h)    
        cv.rectangle(target, top_left, down_right, (0, 0, 255), 2)
        cv.imshow(np.str(method), target)

temp = cv.imread("images/template.png")
target = cv.imread("images/101.png")


template(temp, target)
cv.waitKey(0)  
cv.destroyAllWindows() 