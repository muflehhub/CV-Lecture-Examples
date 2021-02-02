
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and compute the histogram using cv2.calcHist

Histogram Equalization
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html

"""



import cv2

import numpy as np
import matplotlib.pyplot as plt



def nump_proc(img):
    ## find the histogram
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    fig = plt.figure(figsize=(14, 8))
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')


    plt.xlim([0, 256])
    plt.xticks(np.arange(0, 256, step=16))
    plt.tick_params(axis='x',labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    # Show the grid lines as dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-',alpha=0.24)
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.savefig("./w4output/wikihistcdf.jpg", bbox_inches='tight',dpi=300)
    plt.show()

def imageEqualization(img):
    imgequ = cv2.equalizeHist(img)
    histo = cv2.calcHist([img], [0], None, [256], [0, 256])
    histequ = cv2.calcHist([imgequ], [0], None, [256], [0, 256])

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalizedo = cdf * hist.max() / cdf.max()
    hist, bins = np.histogram(imgequ.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalizedq = cdf * hist.max() / cdf.max()

    fig2 = plt.figure(figsize=(16, 9))

    plt.subplot(221)
    plt.imshow(img, cmap='gray')
    plt.title('Original image')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(223)
    plt.bar(np.arange(len(histo)), histo.flatten(), color='red', alpha=0.6)
    plt.plot(cdf_normalizedo, color='black')
    # plt.bar(np.arange(len(hist_cv2)), hist_cv2.flatten(), color='red', alpha=0.6)
    # plt.title("Histogram")
    plt.xlim([0, 256])
    plt.xticks(np.arange(0, 256, step=32))
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=10)
    # Show the grid lines as dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.24)
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)
    plt.subplot(222)
    plt.imshow(imgequ, cmap='gray')
    plt.title('Equal image')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(224)
    plt.bar(np.arange(len(histequ)), histequ.flatten(), color='blue', alpha=0.6)
    plt.plot(cdf_normalizedq, color='black')
    # plt.title("Histogram")
    plt.xlim([0, 256])
    plt.xticks(np.arange(0, 256, step=32))
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=10)
    # Show the grid lines as dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.24)
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)
    plt.savefig("./w4output/wikihistequ.jpg", bbox_inches='tight', dpi=300)
    plt.show()

if __name__ == '__main__':
    ### read the image in grey scale
    # imggraysrc1 = cv2.imread('./w4data/einsteinmedContrast.tif', 0)
    # imggraysrc1 = cv2.imread('./w4data/BHistLight.tif', 0)
    # imggraysrc1 = cv2.imread('./w4data/AHistDark.tif', 0)
    # imggraysrc1 = cv2.imread('./w4data/lenasmall.jpg', 0)
    imggraysrc1 = cv2.imread('./w4data/wiki.jpg', 0)

    # cv2.imshow('Gray image', imggraysrc1)


    # nump_proc(imggraysrc1)
    imageEqualization(imggraysrc1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

