"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and display cropping the image
"""
import cv2

import numpy as np

if __name__ == '__main__':
    img = cv2.imread("./w3data/lena.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    print(img.shape)
    cv2.imshow('BGR image', img)

    y = 50
    x = 25
    h = 125
    w = 150
    '''
    start_point: It is the starting coordinates of rectangle. (X coordinate value, Y coordinate value).
    end_point: It is the ending coordinates of rectangle.  (X coordinate value, Y coordinate value).
    color: It is the color of border line of rectangle to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
    thickness: It is the thickness of the rectangle border line in px. 
    Thickness of -1 px will fill the rectangle shape by the specified color.
    '''

    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
    cv2.imshow('Rectangle', img)

    '''
    [y1:(y2 + 1), x1:(x2 + 1)] with the pair (x1, y1) specifying the coordinates of the top left corner and 
    (x2, y2) specifying the coordinates of the bottom right corner of the pixel array, to return a cropped pixel array.
    '''
    crop_img = img[y:y + h, x:x + w]
    cv2.imshow("cropped", crop_img)
    #

    cv2.waitKey(0)
    cv2.destroyAllWindows()
