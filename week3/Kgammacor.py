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
    # img = cv2.imread("./w3data/gamma.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    img = cv2.imread("./w3data/darkphoto.png", cv2.IMREAD_REDUCED_COLOR_2)
    # img = cv2.imread("./w3data/opencv-logo50.png", cv2.IMREAD_COLOR)
    print(img.shape)
    cv2.imshow('BGR image', img)
    print(img.dtype)
    newimg = img.copy()




    # alpha value [1.0-3.0]:
    alpha = 1.3
    # beta value [0-100]:
    beta = 40
    newimg = cv2.addWeighted(newimg, alpha, newimg, 0, beta)
    cv2.imshow('New image', newimg)
    #
    #


    gamma = 0.4
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    imggammares = cv2.LUT(img, lookUpTable)
    cv2.imshow('gamma image', imggammares)


    ###<<< another way of doing this without lookup table
    newimgA = img.copy()
    newimgA = newimgA.astype(np.float32) / 255
    corrected_image = np.power(newimgA, gamma)
    cv2.imshow('gamma imageA', corrected_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()