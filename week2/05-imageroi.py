"""

Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.


There are several interesting things we can do by accessing raw pixels with NumPy's array
slicing; one of them is defining regions of interests (ROI).

Sometimes, you will have to play with certain regions of images.
For eye detection in images, first face detection is done over the entire image.
When a face is obtained, we select the face region alone and search
for eyes inside it instead of searching the whole image. It improves accuracy
(because eyes are always on faces :D ) and performance (because we search in a small area).

ROI is again obtained using Numpy indexing. Here I am selecting the ball and copying it to another region in the image:

"""

import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread("./w2data/messi5.jpg")
    # im = cv2.imread("./w2data/lena.jpg")
    cv2.imshow('Original image', img)
    # extract the region of interest
    ball = img[280:340, 330:390]
    img[273:333, 100:160] = ball

    cv2.imshow('After image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()