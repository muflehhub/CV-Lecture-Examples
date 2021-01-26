"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and perform pixel transformation
Inverse in grayscale image

"""
import cv2

import numpy as np

if __name__ == '__main__':

    imggraysrc = cv2.imread("./w3data/xray1.tif", cv2.IMREAD_REDUCED_GRAYSCALE_4)
    print(imggraysrc.shape)
    cv2.imshow('Gray image', imggraysrc)
    newimg = imggraysrc.copy()
    ### s= L-1-r
    newimg =  cv2.addWeighted(newimg, -1, newimg,0, 255)
    cv2.imshow('Inv image', newimg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()