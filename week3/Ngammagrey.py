"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and perform pixel transformation
Gamma correction for gray level

"""
import cv2

import numpy as np

if __name__ == '__main__':
    imggraysrc = cv2.imread("./w3data/xray1.tif", cv2.IMREAD_REDUCED_GRAYSCALE_4)

    print(imggraysrc.shape)
    cv2.imshow('Gray image', imggraysrc)

    ## change value of gamma and compare with log
    gamma = 0.1
    lookUpTable = np.empty((1, 256), np.uint8)
    for i in range(256):
        lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    imggammares = cv2.LUT(imggraysrc, lookUpTable)

    cv2.imshow('gamma.1 image', imggammares)

    gamma = 0.2
    lookUpTable = np.empty((1, 256), np.uint8)
    for i in range(256):
        lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    imggammares = cv2.LUT(imggraysrc, lookUpTable)

    cv2.imshow('gamma.2 image', imggammares)

    gamma = 0.4
    lookUpTable = np.empty((1, 256), np.uint8)
    for i in range(256):
        lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    imggammares = cv2.LUT(imggraysrc, lookUpTable)

    cv2.imshow('gamma.4 image', imggammares)

    gamma = 0.6
    lookUpTable = np.empty((1, 256), np.uint8)
    for i in range(256):
        lookUpTable[0, i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    imggammares = cv2.LUT(imggraysrc, lookUpTable)

    cv2.imshow('gamma.6 image', imggammares)


    cv2.waitKey(0)
    cv2.destroyAllWindows()