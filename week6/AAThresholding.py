"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read image and apply simple thresholding
different thresholding techniques

"""
import cv2

import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    ### read the image as grayscale image
    # imgsrc = cv2.imread('./w6data/dave.jpg', cv2.IMREAD_GRAYSCALE)
    # imgsrc = cv2.imread('./w6data/carplate1.jpeg', cv2.IMREAD_REDUCED_GRAYSCALE_4)
    # imgcolor = cv2.imread('./w6data/Seneca2.jpg', cv2.IMREAD_REDUCED_COLOR_4)
    imgcolor = cv2.imread('./w6data/Seneca3.png', cv2.IMREAD_COLOR)
    # imgcolor = cv2.imread('./w6data/circle.png', cv2.IMREAD_COLOR)
    # imgsrc = cv2.imread('./w6data/Seneca2.jpg', cv2.IMREAD_REDUCED_GRAYSCALE_4)
    imgsrc = cv2.imread('./w6data/Seneca3.png', cv2.IMREAD_GRAYSCALE)
    # imgsrc = cv2.imread('./w6data/circle.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Original color", imgcolor)
    cv2.imshow("Original Grayscale", imgsrc)


    ### applying different thresholding techniques on the input image
    ### all pixels value above 127 will  be set to 255
    ### value 125 is arbitrary value
    ret, imgthresh1 = cv2.threshold(imgsrc, 127, 255, cv2.THRESH_BINARY)
    ret, imgthresh2 = cv2.threshold(imgsrc, 127, 255, cv2.THRESH_BINARY_INV)
    ret, imgthresh3 = cv2.threshold(imgsrc, 127, 255, cv2.THRESH_TRUNC)
    ret, imgthresh4 = cv2.threshold(imgsrc, 127, 255, cv2.THRESH_TOZERO)
    ret, imgthresh5 = cv2.threshold(imgsrc, 127, 255, cv2.THRESH_TOZERO_INV)


    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [imgsrc, imgthresh1, imgthresh2, imgthresh3, imgthresh4, imgthresh5]

    for i in range(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.savefig("./w6output/threshold.jpg", bbox_inches='tight', dpi=300)
    plt.show()




    cv2.waitKey(0)
    cv2.destroyAllWindows()


