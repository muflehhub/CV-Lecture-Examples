
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image remove  Gaussian noise using Gaussian averaging filter


"""
import cv2

import numpy as np



if __name__ == '__main__':


    imgsrc = cv2.imread('./w5data/lena.jpg', cv2.IMREAD_REDUCED_GRAYSCALE_2)

    imgnoiseGm0Std40 = cv2.imread('./w5output/lenagrayGaussM0Std40.jpg',cv2.IMREAD_GRAYSCALE)

    cv2.imshow("GaussM0Std40", imgnoiseGm0Std40)
    imgmeanGblur3 = cv2.GaussianBlur(imgnoiseGm0Std40,ksize=(3,3),sigmaX=1.5)
    imgmeanGblur5 = cv2.GaussianBlur(imgnoiseGm0Std40,ksize=(5,5),sigmaX=1.5)
    imgmeanGblur7 = cv2.GaussianBlur(imgnoiseGm0Std40,ksize=(7,7),sigmaX=1.5)

    cv2.imshow('Gauss_blur3', imgmeanGblur3)
    cv2.imshow('Gauss_blur5', imgmeanGblur5)
    cv2.imshow('Gauss_blur7', imgmeanGblur7)

    cv2.imshow("original", imgsrc)

    # value1 = cv2.PSNR(imgsrc, imgnoiseGm0Std20)
    # print(f"PSNR OriginalvsNoisy value is {value1} dB")
    # value2 = cv2.PSNR(imgsrc, imgmeanblur3)
    # print(f"PSNR OriginalvsRecover value is {value2} dB")
    # value3 = cv2.PSNR(imgnoiseGm0Std20, imgmeanblur3)
    # print(f"PSNR OriginalvsRecover value is {value3} dB")



    cv2.waitKey(0)
    cv2.destroyAllWindows()