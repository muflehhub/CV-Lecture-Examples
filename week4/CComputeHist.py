
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and compute the histogram using cv2.calcHist

"""
"""
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_begins/py_histogram_begins.html
https://docs.opencv.org/4.0.1/d8/dbc/tutorial_histogram_calculation.html
So now we use cv2.calcHist() function to find the histogram. Let’s familiarize with the function and its parameters :
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

    images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, “[img]”.
    channels : it is also given in square brackets. It the index of channel for which we calculate histogram. 
            For example, if input is grayscale image, its value is [0]. For color image, you can pass [0],[1] or [2] 
            to calculate histogram of blue,green or red channel respectively.
    mask : mask image. To find histogram of full image, 
            it is given as “None”. But if you want to find histogram 
            of particular region of image, you have to create a mask image for 
            that and give it as mask. 
    histSize : this represents our BIN count. Need to be given in square brackets. 
                For full scale, we pass [256].
    ranges : this is our RANGE. Normally, it is [0,256].

"""


import cv2

import numpy as np
import matplotlib.pyplot as plt


###<<<Function to compute the histogram using nested for loop>>>
def compute_hist_cv2(img):
    # If image number of dimensions is 2 then we have grayscale image
    if (img.ndim == 2):
        ## greyscale image contains only one channel
        ## we would like to compute histgram for full image and full range with 256 bins
        hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    return hist

if __name__ == '__main__':
    ### read the image in grey scale
    imggraysrc1 = cv2.imread('./w4data/einsteinmedContrast.tif', 0)

    cv2.imshow('Medium Contrast Gray image', imggraysrc1)

    print(imggraysrc1.ndim)
    hist_cv2 = compute_hist_cv2(imggraysrc1)
    print(hist_cv2.shape)
    print(len(hist_cv2))
    # print(np.arange(len(hist_cv2)))
    # fig = plt.figure(figsize=(16, 9))
    fig = plt.figure(figsize=(14, 8))

    plt.bar(np.arange(len(hist_cv2)), hist_cv2.flatten(), color='red', alpha=0.6)
    # plt.title("Histogram")
    plt.xlim([0, 256])
    plt.xticks(np.arange(0, 256, step=16))
    plt.tick_params(axis='x',labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    # Show the grid lines as dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-',alpha=0.24)
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)

    plt.savefig("./w4output/einsteinmedcontrasthist.jpg", bbox_inches='tight',dpi=300)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()