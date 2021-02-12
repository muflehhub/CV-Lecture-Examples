
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image add Gaussian noise

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

###<<<Function to compute the histogram using nested for loop>>>
def compute_hist_cv2(img):
    # If image number of dimensions is 2 then we have grayscale image
    if (img.ndim == 2):
        ## greyscale image contains only one channel
        ## we would like to compute histgram for full image and full range with 256 bins
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    return hist


if __name__ == '__main__':


    # imgsrc = cv2.imread('./w5data/lena.jpg', cv2.IMREAD_REDUCED_COLOR_2)
    # imgsrc = cv2.imread('./w5data/ImageC.jpg', cv2.IMREAD_COLOR)
    # imgsrc = cv2.imread('./w5data/ImageA.jpg',cv2.IMREAD_COLOR)
    # imgsrc = cv2.imread('./w5data/ImageA.jpg', cv2.IMREAD_GRAYSCALE)


    '''
    Gray scale 
    '''
    # imgsrc = cv2.imread('./w5data/lena.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_2)
    # imgnoisey2= addGaussianNoise(imgsrc,meanvalue=0, stdvalue=20)
    # cv2.imshow('GaussM0Std20',imgnoisey2)
    # cv2.imwrite('./w5output/lenagrayGaussM0Std20.jpg', imgnoisey2)
    # imgnoisey4 = addGaussianNoise(imgsrc, meanvalue=0, stdvalue=40)
    # cv2.imshow('GaussM0Std40', imgnoisey4)
    # cv2.imwrite('./w5output/lenagrayGaussM0Std40.jpg', imgnoisey4)
    # imgnoisey6 = addGaussianNoise(imgsrc, meanvalue=0, stdvalue=60)
    # cv2.imshow('GaussM0Std60', imgnoisey6)
    # cv2.imwrite('./w5output/lenagrayGaussM0Std60.jpg', imgnoisey6)



    '''
    Pattern noise gray scale
    '''
    imgsrc = cv2.imread('./w5data/pattern.tif', cv2.IMREAD_GRAYSCALE)
    imgnoisey2 = addGaussianNoise(imgsrc, meanvalue=0, stdvalue=20)
    cv2.imshow('GaussM0Std20', imgnoisey2)
    cv2.imwrite('./w5output/patternGaussM0Std20.jpg', imgnoisey2)
    imgnoisey4 = addGaussianNoise(imgsrc, meanvalue=0, stdvalue=40)
    cv2.imshow('GaussM0Std40', imgnoisey4)
    cv2.imwrite('./w5output/patternGaussM0Std40.jpg', imgnoisey4)
    imgnoisey6 = addGaussianNoise(imgsrc, meanvalue=0, stdvalue=60)
    cv2.imshow('GaussM0Std60', imgnoisey6)
    cv2.imwrite('./w5output/patternGaussM0Std60.jpg', imgnoisey6)

    '''
    Color image 
    '''
    # imgsrc = cv2.imread('./w5data/lena.jpg', cv2.IMREAD_REDUCED_COLOR_2)
    #
    # imgnoisey2 = addGaussianNoise(imgsrc, meanvalue=0, stdvalue=20)
    # cv2.imshow('GaussM0Std20', imgnoisey2)
    # cv2.imwrite('./w5output/lenacolorGaussM0Std20.jpg', imgnoisey2)
    # imgnoisey4 = addGaussianNoise(imgsrc, meanvalue=0, stdvalue=40)
    # cv2.imshow('GaussM0Std40', imgnoisey4)
    # cv2.imwrite('./w5output/lenacolorGaussM0Std40.jpg', imgnoisey4)
    # imgnoisey6 = addGaussianNoise(imgsrc, meanvalue=0, stdvalue=60)
    # cv2.imshow('GaussM0Std60', imgnoisey6)
    # cv2.imwrite('./w5output/lenacolorGaussM0Std60.jpg', imgnoisey6)

    cv2.imshow("original", imgsrc)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
