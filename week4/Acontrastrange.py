
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and compute the contrast of that image
contrast is  defined as the difference in intensity between the highest and lowest intensity levels in an image.

"""
import cv2

import numpy as np

if __name__ == '__main__':
    imggraysrcl = cv2.imread("./w4data/einsteinlowcontrast.tif", cv2.IMREAD_GRAYSCALE)
    print(imggraysrcl.shape)
    cv2.imshow('Gray image l', imggraysrcl)
    srclmin=np.min(imggraysrcl)
    srclmax = np.max(imggraysrcl)
    print ("Low max={}, min={}, contrast={}".format(srclmax,srclmin,srclmax-srclmin))


    imggraysrcm = cv2.imread("./w4data/einsteinmedContrast.tif", cv2.IMREAD_GRAYSCALE)
    print(imggraysrcm.shape)
    cv2.imshow('Gray image m', imggraysrcm)
    srcmmin = np.min(imggraysrcm)
    srcmmax = np.max(imggraysrcm)
    print("Medium max={}, min={}, contrast={}".format(srcmmax, srcmmin, srcmmax - srcmmin))

    imggraysrch = cv2.imread("./w4data/einsteinhighcontrast.tif", cv2.IMREAD_GRAYSCALE)
    print(imggraysrch.shape)
    cv2.imshow('Gray image h', imggraysrch)
    srchmin = np.min(imggraysrch)
    srchmax = np.max(imggraysrch)
    print("High max={}, min={}, contrast={}".format(srchmax, srchmin, srchmax - srchmin))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
