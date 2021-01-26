"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and display it with different color mode
cyan magenta yellow
"""
import cv2

import numpy as np


if __name__ == '__main__':
    # img = cv2.imread("./w3data/opencv-logo50.png", cv2.IMREAD_COLOR)
    # img = cv2.imread("./w3data/bgr.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    img = cv2.imread("./w3data/Senecabgr.jpg", cv2.IMREAD_COLOR)
    cv2.imshow('BGR image', img)
    # split the channel
    b,g,r = cv2.split(img)
    c = 255-r
    m = 255-g
    y = 255-b
    # merge teh channel again
    imgCMYM = cv2.merge((c,m,y))

    cv2.imshow('CMY image', imgCMYM)

    ## view each channel alone
    zeros = np.ones(c.shape, np.uint8)
    C = cv2.merge((c, zeros, zeros))
    M = cv2.merge((zeros, m, zeros))
    Y = cv2.merge((zeros, zeros, y))
    cv2.imshow('Cyan CMY', C)
    cv2.imshow('Magenta CMY', M)
    cv2.imshow('Y CMY', Y)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
