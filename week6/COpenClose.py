"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read image and apply OpenCV: morphological
operations: opening and closing

"""
import cv2

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    #### input image already black and white
    imgsrc= cv2.imread('./w6data/noisy_fingerprint.tif')

    # cv2.imshow('Image Source',imgsrc)

    kernel = np.ones((3, 3), np.uint8)

    imgerosion = cv2.erode(imgsrc, kernel, iterations=1)
    imgdilation = cv2.dilate(imgsrc, kernel, iterations=1)


    imgopening = cv2.morphologyEx(imgsrc, cv2.MORPH_OPEN, kernel)
    imgclosing = cv2.morphologyEx(imgsrc, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('NoisyFingerprint', imgsrc)
    cv2.imshow("Dilation", imgdilation)
    cv2.imshow("Erosion", imgerosion)

    cv2.imshow('Opening', imgopening)
    cv2.imshow('Closing', imgclosing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


