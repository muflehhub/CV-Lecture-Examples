
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Create your own image using numpy

"""

import cv2
import numpy as np

if __name__ == '__main__':
    N=256
    gray = np.zeros( (N,N), dtype="uint8" )
    for i in range(N):
        gray[i,:] = i
    imgray=gray.astype("uint8")
    gray2 = np.ones((N, N), dtype="uint8")
    for i in range(N):
        gray2[:, i] = i
    imgray2 = gray2.astype("uint8")

    cv2.imshow('Gray image', imgray)
    cv2.imshow('Gray2 image', imgray2)
    print(imgray.shape)

    '''
    Let's now convert this image into blue-green-red (BGR) format using the cv2.cvtColor function:
    '''
    imgBGR = cv2.cvtColor(imgray, cv2.COLOR_GRAY2BGR)
    print (imgBGR.shape)
    cv2.imshow('Color image', imgBGR)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

