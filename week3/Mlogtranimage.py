"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and perform pixel transformation
Log transformation

"""
import cv2

import numpy as np

if __name__ == '__main__':

    imggraysrc = cv2.imread("./w3data/xray1.tif", cv2.IMREAD_REDUCED_GRAYSCALE_4)

    print(imggraysrc.shape)
    cv2.imshow('Gray image', imggraysrc)

    newimg = imggraysrc.copy().astype(np.float32)

    # Apply log transform.
    c = 255 / (np.log(1 + np.max(newimg)))
    print (c)
    imglogtransf = c * np.log(1 + newimg)

    # Specify the data type.
    imglogtransf = np.array(imglogtransf, dtype=np.uint8)
    cv2.imshow('log trans image', imglogtransf)



    cv2.waitKey(0)
    cv2.destroyAllWindows()