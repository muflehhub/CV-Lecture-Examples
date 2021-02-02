
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and compute the histogram using cv2.calcHist

View light and dark images

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
    # imggraysrc1 = cv2.imread('./w4data/einsteinmedContrast.tif', 0)
    # imggraysrc1 = cv2.imread('./w4data/BHistLight.tif', 0)
    # imggraysrc1 = cv2.imread('./w4data/AHistDark.tif', 0)
    imggraysrc1 = cv2.imread('./w4data/AHistDark.tif', 0)
    cv2.imshow('Medium Contrast Gray image', imggraysrc1)

    print(imggraysrc1.ndim)
    hist_cv2 = compute_hist_cv2(imggraysrc1)
    print(hist_cv2.shape)
    print(len(hist_cv2))
    # print(np.arange(len(hist_cv2)))
    # fig = plt.figure(figsize=(16, 9))
    fig = plt.figure(figsize=(14, 8))

    plt.bar(np.arange(len(hist_cv2)), hist_cv2.flatten(), color='blue', alpha=0.6)
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

    plt.savefig("./w4output/darkthist.jpg", bbox_inches='tight',dpi=300)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()