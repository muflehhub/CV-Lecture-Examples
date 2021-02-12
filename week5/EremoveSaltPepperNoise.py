
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image remove  salt and pepper noise

"""
import cv2

import numpy as np






if __name__ == '__main__':


    imgsrc = cv2.imread('./w5data/lena.jpg', cv2.IMREAD_REDUCED_GRAYSCALE_2)

    imgnoise = cv2.imread('./w5output/leangreaySP20-8.jpg',cv2.IMREAD_GRAYSCALE)
    print(imgnoise[125:135, 125:135])
    cv2.imshow("SP20", imgnoise)
    imgmedianblur3 = cv2.medianBlur(imgnoise, 3)
    print(imgmedianblur3[125:135, 125:135])
    imgmedianblur5 = cv2.medianBlur(imgnoise, 5)
    imgmedianblur7 = cv2.medianBlur(imgnoise, 7)
    cv2.imshow('median_blur3', imgmedianblur3)
    cv2.imshow('median_blur5', imgmedianblur5)
    cv2.imshow('median_blur7', imgmedianblur7)

    cv2.imshow("original", imgsrc)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

