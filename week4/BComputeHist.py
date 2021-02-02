
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and compute the histogram using nested for loop

"""
import cv2

import numpy as np
import matplotlib.pyplot as plt


###<<<Function to compute the histogram using nested for loop>>>
def compute_hist_loop(img):
    ## create numpy array to store the count
    freqCount = np.zeros([256], dtype='int')
    # print(freqCount.shape)
    ht, wt = img.shape # size of image
    # print(ht*wt)
    ## counting the frequency of each pixel
    ## we visit each pixel
    for x in range(ht):
        for y in range(wt):
            freqCount[img[x][y]] = freqCount[img[x][y]] + 1
    return freqCount

if __name__ == '__main__':
    ### read the image in grey scale
    # imggraysrc1 = cv2.imread('./w4data/einsteinlowcontrast.tif', 0)
    imggraysrc1 = cv2.imread('./w4data/CHistLowContrast.tif', 0)

    cv2.imshow('Low Contrast Gray image', imggraysrc1)
    raw_hist = compute_hist_loop(imggraysrc1)
    # fig = plt.figure(figsize=(16, 9))
    fig = plt.figure(figsize=(14, 8))
    # fig = plt.figure()
    plt.bar(np.arange(len(raw_hist)), raw_hist, color='red', alpha=0.6)
    # plt.title("Histogram")
    plt.xlim([0, 256])
    plt.xticks(np.arange(0, 256, step=16))
    # plt.xlabel('xlabel', fontsize=18)
    # plt.rc('xtick', labelsize=20)
    # plt.rc('ytick', labelsize=20)
    plt.tick_params(axis='x',labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    # Show the grid lines as dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-',alpha=0.24)
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)

    # plt.savefig("./w4output/einsteinlowcontrasthist.jpg", bbox_inches='tight',dpi=300)
    plt.savefig("./w4output/lowcontrasthist.jpg", bbox_inches='tight', dpi=300)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()