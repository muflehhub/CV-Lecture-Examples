"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Modify color channel
"""

import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread("./w2data/messi5.jpg")
    # im = cv2.imread("./w2data/lena.jpg")
    cv2.imshow('Original image', img)
    bimg = np.copy(img)
    gimg = np.copy(img)
    rimg = np.copy(img)
    imgcpy = np.copy(img)
    #Setting all G (green) values of an image to 0
    bimg[:, :, 0] = 0
    gimg[:, :, 1] = 0
    rimg[:, :, 2] = 0
    imgcpy[:,:,0:2] =0
    cv2.imshow('Modified Blue=0 image', bimg)
    cv2.imshow('Modified Green=0 image', gimg)
    cv2.imshow('Modified Red=0 image', rimg)
    cv2.imshow('Modified 1:3 =0 image', imgcpy)

    cv2.waitKey(0)
    cv2.destroyAllWindows()