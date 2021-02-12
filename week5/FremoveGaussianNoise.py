
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image remove  gaussian noise using averaging filter

"""
import cv2

import numpy as np

def addGaussianNoise(img,meanvalue, stdvalue):
    """
    Add Gaussian noise to input image
    test if the input image is grayscale or color
    Gaussian will be added to each channel
    :param img:
    :param meanvalue:
    :param stdvalue:
    :return:
    """
    ### create the noise image similar to input image,
    ### same size and channel with same type
    noiseimg = np.zeros(img.shape, img.dtype)

    if noiseimg.ndim ==3:
        ### color image then add gaussian to each channel
        cv2.randn(noiseimg, (meanvalue,meanvalue,meanvalue), (stdvalue,stdvalue,stdvalue))
    else:
        ### grayscale only one channel
        cv2.randn(noiseimg, meanvalue, stdvalue)

    ### now add the noise to the input image
    outimg = cv2.addWeighted(img,1, noiseimg,1,0)

    return outimg



if __name__ == '__main__':


    imgsrc = cv2.imread('./w5data/lena.jpg', cv2.IMREAD_REDUCED_GRAYSCALE_2)

    imgnoiseGm0Std40 = cv2.imread('./w5output/lenagrayGaussM0Std40.jpg',cv2.IMREAD_GRAYSCALE)
    print(imgnoiseGm0Std40[125:135, 125:135])
    cv2.imshow("GaussM0Std40", imgnoiseGm0Std40)
    imgmeanblur3 = cv2.blur(src=imgnoiseGm0Std40,ksize=(3,3))
    print(imgmeanblur3[125:135, 125:135])
    imgmeanblur5 = cv2.blur(src=imgnoiseGm0Std40, ksize=(5, 5))
    imgmeanblur7 = cv2.blur(src=imgnoiseGm0Std40, ksize=(7, 7))
    # imgmeanblur3 = cv2.fastNlMeansDenoisingColored(imgnoiseGm0Std20, None, 10, 10, 7, 21)
    cv2.imshow('mean_blur3', imgmeanblur3)
    cv2.imshow('mean_blur5', imgmeanblur5)
    cv2.imshow('mean_blur7', imgmeanblur7)

    cv2.imshow("original", imgsrc)

    # value1 = cv2.PSNR(imgsrc, imgnoiseGm0Std20)
    # print(f"PSNR OriginalvsNoisy value is {value1} dB")
    # value2 = cv2.PSNR(imgsrc, imgmeanblur3)
    # print(f"PSNR OriginalvsRecover value is {value2} dB")
    # value3 = cv2.PSNR(imgnoiseGm0Std20, imgmeanblur3)
    # print(f"PSNR OriginalvsRecover value is {value3} dB")



    cv2.waitKey(0)
    cv2.destroyAllWindows()