"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and perform pixel transformation
Brightness and contrast adjustments

"""
import cv2

import numpy as np

if __name__ == '__main__':
    # img = cv2.imread("./w3data/messi5.jpg", cv2.IMREAD_REDUCED_COLOR_2)

    # img = cv2.imread("./w3data/lena.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    img = cv2.imread("./w3data/lenasmall.jpg", cv2.IMREAD_COLOR)
    # img = cv2.imread("./w3data/opencv-logo50.png", cv2.IMREAD_COLOR)
    print(img.shape)
    cv2.imshow('BGR image', img)
    newimg = img.copy()
    #alpha value [1.0-3.0]:
    alpha = 2.2
    #beta value [0-100]:
    beta = 50

    ### mofidy the contract and add brightness to the image
    newimg =  cv2.addWeighted(newimg, 2.2, newimg,0, 50)
    cv2.imshow('New image', newimg)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
