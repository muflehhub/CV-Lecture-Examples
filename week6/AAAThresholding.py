"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read image and apply simple thresholding
different thresholding value

"""
import cv2

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    ### read the image as grayscale image

    imgsrc = cv2.imread('./w6data/cameraman.tif', cv2.IMREAD_GRAYSCALE)

    cv2.imshow("Original Grayscale", imgsrc)


    ### applying different thresholding techniques on the input image
    ### all pixels value above 127 will  be set to 255
    ### value 125 is arbitrary value
    ret, imgthresh1 = cv2.threshold(imgsrc, 25, 255, cv2.THRESH_BINARY)
    ret, imgthresh2 = cv2.threshold(imgsrc, 50, 255, cv2.THRESH_BINARY)
    ret, imgthresh3 = cv2.threshold(imgsrc, 75, 255, cv2.THRESH_BINARY)
    ret, imgthresh4 = cv2.threshold(imgsrc, 100, 255, cv2.THRESH_BINARY)
    ret, imgthresh5 = cv2.threshold(imgsrc, 125, 255, cv2.THRESH_BINARY)

    ret, imgthresh11 = cv2.threshold(imgsrc, 125, 255, cv2.THRESH_BINARY)
    ret, imgthresh12 = cv2.threshold(imgsrc, 150, 255, cv2.THRESH_BINARY)
    ret, imgthresh13 = cv2.threshold(imgsrc, 175, 255, cv2.THRESH_BINARY)
    ret, imgthresh14 = cv2.threshold(imgsrc, 200, 255, cv2.THRESH_BINARY)
    ret, imgthresh15 = cv2.threshold(imgsrc, 225, 255, cv2.THRESH_BINARY)

    titles = ['Original Image', 'BINARY25', 'BINARY50', 'BINARY75', 'BINARY100', 'BINARY125','BINARY150', 'BINARY175', 'BINARY200', 'BINARY225']
    images = [imgsrc, imgthresh1, imgthresh2, imgthresh3, imgthresh4, imgthresh5,imgthresh12, imgthresh13, imgthresh14, imgthresh15]
    for i in range(10):
        plt.subplot(2, 5, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])


    # for i in range(6):
    #     plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    #     plt.title(titles[i])
    #     plt.xticks([]), plt.yticks([])

    plt.savefig("./w6output/thresholdVar.jpg", bbox_inches='tight', dpi=300)
    plt.show()




    cv2.waitKey(0)
    cv2.destroyAllWindows()


