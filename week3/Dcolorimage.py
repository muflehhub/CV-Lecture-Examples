"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and display it with different color mode
HSV Images
"""
import cv2

import numpy as np


if __name__ == '__main__':
    # img = cv2.imread("./w3data/opencv-logo50.png", cv2.IMREAD_COLOR)
    img = cv2.imread("./w3data/messi5.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    # img = cv2.imread("./w3data/Senecabgr.jpg", cv2.IMREAD_COLOR)
    cv2.imshow('BGR image', img)
    imgHSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV  image', imgHSV)
    H, S, V = cv2.split(imgHSV)

    cv2.imshow('H CMY', H)
    cv2.imshow('S CMY', S)
    cv2.imshow('V CMY', V)



    cv2.waitKey(0)
    cv2.destroyAllWindows()
