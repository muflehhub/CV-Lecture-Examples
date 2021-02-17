"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read image and apply OpenCV: dilation

"""
import cv2

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    ### read the image as grayscale image

    # imgsrc = cv2.imread('./w6data/textwgaps.tif', cv2.IMREAD_GRAYSCALE)
    imgsrc = cv2.imread('./w6data/wirebondmask.tif', cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Original Grayscale", imgsrc)
    kernel = np.ones((3, 3), np.uint8)
    kernel[0,(0,2)]=0
    kernel[2, (0, 2)] = 0
    print (kernel)
    imgerosion = cv2.erode(imgsrc, kernel, iterations=1)

    cv2.imshow("Erosion", imgerosion)

    cv2.waitKey(0)
    cv2.destroyAllWindows()