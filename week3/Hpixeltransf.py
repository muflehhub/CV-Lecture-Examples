"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and perform pixel transformation
this is color image that means you have three channels
if you work with grayscale image then you work with one channel

"""
import cv2

import numpy as np

if __name__ == '__main__':
    # img = cv2.imread("./w3data/messi5.jpg", cv2.IMREAD_REDUCED_COLOR_2)

    # img = cv2.imread("./w3data/lena.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    img = cv2.imread("./w3data/flower5.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    # img = cv2.imread("./w3data/opencv-logo50.png", cv2.IMREAD_COLOR)
    print(img.shape)
    cv2.imshow('BGR image', img)
    print(img.dtype)
    newimg = img.copy()

    ## << add
    scalar = 75
    ## create image
    a = np.zeros(newimg.shape, dtype='uint8') + scalar
    # use add image function
    newimgadd= cv2.add(newimg, a)
    cv2.imshow('add image', newimgadd)
    ## use the substract image function
    newimgsub = cv2.subtract(newimg,a)
    cv2.imshow('sub image', newimgsub)

    ### same result with addWeighted function
    newimgaddw = cv2.addWeighted(newimg,1,newimg,0,75)
    cv2.imshow('addw image', newimgaddw)

    print(img[150, 150])
    print(newimgadd[150, 150])
    print(newimgsub[150, 150])

    # print(newimgaddw[150, 150])

    #####------------------------------------------------
    # ###<<<< Wrong way of add or substracting images >>>
    # newimgaddA = cv2.add(newimg, 75)
    # cv2.imshow('add 75 image', newimgaddA)
    # newimgsubA = cv2.add(newimg, -75)
    # cv2.imshow('add -75 image', newimgsubA)
    #
    # ## << wrong way of adding constant
    # newimgaddB = img.copy()
    # newimgaddB[:,:,0] += 75
    # newimgaddB[:, :, 1] += 75
    # newimgaddB[:, :, 2] += 75
    #
    #
    # cv2.imshow('add 75 imageB', newimgaddB)
    #
    #
    #
    # print(newimgaddA[150, 150])
    # print(newimgaddB[150, 150])
    #
    # print(newimgsubA[150, 150])

    cv2.waitKey(0)
    cv2.destroyAllWindows()
