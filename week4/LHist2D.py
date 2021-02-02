

"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and compute the 2D histogram using cv2.calcHist





"""



import cv2

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def compute2DHist(img):
    # 2D histogram for Blue and Red channels.
    hist = cv2.calcHist([img], [0, 2], None, [256, 256], [0, 256, 0, 256])


    fig1 = plt.figure()
    # show using matplotlib
    plt.imshow(hist, interpolation='nearest')
    plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.24)
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)
    plt.savefig("./w4output/2DHist.jpg", bbox_inches='tight', dpi=300)
    plt.show()
    plt.show()


def compute2DHSVHist(img):

    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    fig2 = plt.figure()


    # 2D histogram for Hue and Saturation channels.
    hist = cv2.calcHist([imghsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # show using matplotlib
    plt.imshow(hist, interpolation='nearest')
    plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.24)
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)
    plt.savefig("./w4output/2DHistHSV.jpg", bbox_inches='tight', dpi=300)
    plt.show()
    plt.show()

def compute3DHist(img):
    # our 2D histogram could only take into account 2 out
    # of the 3 channels in the image so now let's build a
    # 3D color histogram (utilizing all channels) with 8 bins
    # in each direction -- we can't plot the 3D histogram, but
    # the theory is exactly like that of a 2D histogram, so
    # we'll just show the shape of the histogram
    hist3d = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    print("shape of 3D histogram is {}".format(hist3d.shape))
    print("number of elements 3D histogram is {}".format(hist3d.size))

    plt.bar(np.arange(hist3d.size), hist3d.flatten(), color='red', alpha=0.6)
    plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha=0.24)
    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.12)
    plt.savefig("./w4output/3DHistBGR.jpg", bbox_inches='tight', dpi=300)
    plt.show()
    plt.show()


if __name__ == '__main__':
    ### read the image in grey scale
    # imggraysrc1 = cv2.imread('./w4data/einsteinmedContrast.tif', 0)
    # imggraysrc1 = cv2.imread('./w4data/BHistLight.tif', 0)
    # imggraysrc1 = cv2.imread('./w4data/AHistDark.tif', 0)

    # imgsrc = cv2.imread('./w4data/lenasmall.jpg', cv2.IMREAD_COLOR)
    imgsrc = cv2.imread('./w4data/messi5.jpg', cv2.IMREAD_COLOR)
    compute2DHist(imgsrc)
    compute2DHSVHist(imgsrc)
    compute3DHist(imgsrc)
    print(imgsrc.shape)
    print(imgsrc.ndim)
    cv2.imshow('Color image', imgsrc)

    cv2.waitKey(0)
    cv2.destroyAllWindows()