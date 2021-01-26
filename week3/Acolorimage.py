"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and display it with different color mode
"""
import cv2

import numpy as np


if __name__ == '__main__':
    # img = cv2.imread("./w3data/opencv-logo50.png", cv2.IMREAD_COLOR)
    # img = cv2.imread("./w3data/bgr.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    img = cv2.imread("./w3data/Senecabgr.jpg", cv2.IMREAD_COLOR)
    cv2.imshow('BGR image', img)
    # bimg, gimg, rimg = cv2.split(img)

    # copy the image
    bimg = np.copy(img)
    # set the channel Green and Red to zero
    bimg[:,:,1:3] = 0 #
    # show the blue image
    cv2.imshow('B image', bimg)
    # copy the original image
    gimg = np.copy(img)
    # set some channel to zero
    gimg[:,:,0]=0
    gimg[:, :, 2] = 0
    # copy the original image
    rimg = np.copy(img)
    # set some channel to zero
    rimg[:,:,0:2] = 0
    cv2.imshow('B image', bimg)
    cv2.imshow('G image', gimg)
    cv2.imshow('R image', rimg)
    # print shape and check the shape of each image
    print (img.shape)
    print(bimg.shape)
    print(gimg.shape)
    print(rimg.shape)
    # split image into different channel each as greyscal image
    b,g,r = cv2.split(img)
    cv2.imshow('b Channel image', b)
    cv2.imshow('G Channel image', g)
    cv2.imshow('R Channel image', r)

    ###<<< Convert to gray scale image>>>
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray-scale image', imggray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()