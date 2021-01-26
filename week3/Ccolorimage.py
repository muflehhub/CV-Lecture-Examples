"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and display it with different color mode
YUV Images
"""
import cv2

import numpy as np


if __name__ == '__main__':
    # img = cv2.imread("./w3data/opencv-logo50.png", cv2.IMREAD_COLOR)
    img = cv2.imread("./w3data/messi5.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    # img = cv2.imread("./w3data/Senecabgr.jpg", cv2.IMREAD_COLOR)
    cv2.imshow('BGR image', img)
    ## convert the color to YUV
    imgYUV= cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    cv2.imshow('YUV  image', imgYUV)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
