"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and perform pixel transformation
Thresholding

"""
import cv2

import numpy as np

if __name__ == '__main__':

    imggraysrc = cv2.imread("./w3data/moon.tif", cv2.IMREAD_REDUCED_GRAYSCALE_2)

    print(imggraysrc.shape)
    cv2.imshow('Gray image', imggraysrc)
    print(np.max(imggraysrc))
    print(np.average(imggraysrc))
    ret, imgth1 = cv2.threshold(imggraysrc, 110, 255, cv2.THRESH_BINARY)
    ret, imgth2 = cv2.threshold(imggraysrc, 110, 255, cv2.THRESH_BINARY_INV)
    ret, imgth3 = cv2.threshold(imggraysrc, 110, 255, cv2.THRESH_TRUNC)
    ret, imgth4 = cv2.threshold(imggraysrc, 110, 255, cv2.THRESH_TOZERO)


    cv2.imshow('Thresholding image1', imgth1)
    cv2.imshow('Thresholding image2', imgth2)
    cv2.imshow('Thresholding image3', imgth3)
    cv2.imshow('Thresholding image4', imgth4)
    ### << one way simple
    th=100 #128
    imgth = imggraysrc.copy()

    imgth [imggraysrc>=th] = 255
    imgth[imggraysrc < th] = 0
    cv2.imshow('Thresholding image', imgth)
    cv2.waitKey(0)
    cv2.destroyAllWindows()