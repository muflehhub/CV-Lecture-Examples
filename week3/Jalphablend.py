"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and perform pixel transformation

Blending images
"""
import cv2

import numpy as np

if __name__ == '__main__':
    # img = cv2.imread("./w3data/messi5.jpg", cv2.IMREAD_REDUCED_COLOR_2)

    # imgsrc1 = cv2.imread("./w3data/flower5.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    # imgsrc2 = cv2.imread("./w3data/flower8.jpg", cv2.IMREAD_REDUCED_COLOR_2)

    imgsrc1 = cv2.imread("./w3data/flower1.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    imgsrc2 = cv2.imread("./w3data/flower8.jpg", cv2.IMREAD_REDUCED_COLOR_2)

    ## resize one of the images to match the other one
    imgsrc2 = cv2.resize(imgsrc2, imgsrc1.shape[1::-1])
    cv2.imshow('image src1', imgsrc1)
    cv2.imshow('image src2', imgsrc2)
    # img = cv2.imread("./w3data/opencv-logo50.png", cv2.IMREAD_COLOR)
    print(imgsrc1.shape)
    print(imgsrc2.shape)

    imgdst2 = cv2.addWeighted(imgsrc1, 0.2, imgsrc2, 0.4, 0)
    cv2.imshow('blend Alp=0.2,.4', imgdst2)
    imgdst4 = cv2.addWeighted(imgsrc1, 0.4, imgsrc2, 0.4, 0)
    cv2.imshow('blend Alp=0.4,.4', imgdst4)
    imgdst5 = cv2.addWeighted(imgsrc1, 0.5, imgsrc2, 0.4, 0)
    cv2.imshow('blend Alp=0.5,.4', imgdst5)
    imgdst8 = cv2.addWeighted(imgsrc1, 0.8, imgsrc2, 0.4, 0)
    cv2.imshow('blend Alp=0.8,.4', imgdst8)
    imgdst1 = cv2.addWeighted(imgsrc1, 1, imgsrc2, 0.4, 0)
    cv2.imshow('blend Alp=1,.4', imgdst1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()