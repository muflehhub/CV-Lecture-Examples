
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and compute the histogram using NumPy histogram


"""
"""
https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
numpy.histogram(a, bins=10, range=None, normed=None, weights=None, density=None)
    a : array_like
        Input data. The histogram is computed over the flattened array.
    bin is range that represents the width of a single bar of the histogram along the X-axis. 
    You could also call this the interval. (Wikipedia defines them more formally as "disjoint categories".)
    
    range(float, float), optional
    The lower and upper range of the bins. If not provided, range is simply (a.min(), a.max()). Values outside the range are ignored. The first element of the range must be less than or equal to the second. range affects the automatic bin computation as well. While bin width is computed to be optimal based on the actual data within range, the bin count will fill the entire range including portions containing no data.

return: 
    hist : array
        The values of the histogram. 
    bins  array of dtype float
        Return the bin edges (length(hist)+1).


"""




import cv2

import numpy as np
import matplotlib.pyplot as plt


###<<<Function to compute the histogram using nested for loop>>>
def compute_hist_numpy(img):

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    return hist, bins

if __name__ == '__main__':
    ### read the image in grey scale
    # imggraysrc1 = cv2.imread('./w4data/einsteinhighcontrast.tif', 0)
    imggraysrc1 = cv2.imread('./w4data/DHistHighContrast.tif', 0)

    cv2.imshow('High Contrast Gray image', imggraysrc1)
    histnumpy, bins = compute_hist_numpy(imggraysrc1)
    ### we need to be careful here since bins return 257 value
    ### (length(hist)+1).
    bins = bins[:256].astype('uint8')
    print(histnumpy.shape)
    print(bins.shape)
    # print(bins)
    # print(type(histnumpy))

    fig = plt.figure(figsize=(16, 9))
    fig = plt.figure(figsize=(14, 8))
    # fig = plt.figure()
    plt.bar(bins.flatten(), histnumpy.flatten(), color='red', alpha=0.6)
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

    # plt.savefig("./w4output/einsteinhighcontrasthist.jpg", bbox_inches='tight',dpi=300)
    plt.savefig("./w4output/highcontrasthist.jpg", bbox_inches='tight', dpi=300)
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()