"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Drawing different rectangle with different color


"""

import cv2
import numpy as np

if __name__ == '__main__':

    blank = np.zeros((150,300,3), dtype='uint8')
    cv2.imshow('Blank', blank)

    #  Draw a Blue Rectangle
    cv2.rectangle(blank, (0, 0), (blank.shape[1] // 3, blank.shape[0] ), (255, 0, 0), thickness=-1)
    cv2.imshow('B Rectangle', blank)
    #  Draw a Green  Rectangle
    cv2.rectangle(blank, (blank.shape[1] // 3, 0), (2*(blank.shape[1] // 3), blank.shape[0]), (0, 255, 0), thickness=-1)
    cv2.imshow('G Rectangle', blank)
    #  Draw a Red  Rectangle
    cv2.rectangle(blank, (2*(blank.shape[1] // 3), 0), (3 * (blank.shape[1] // 3), blank.shape[0]), (0, 0, 255),
                  thickness=-1)
    cv2.imshow('R Rectangle', blank)
    cv2.imwrite("./w3output/cvbgr.png", blank)
    cv2.imwrite("./w3output/cvbgr.jpg", blank)

    cv2.putText(blank, 'Seneca College', (25, 75), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
    cv2.imshow('Text', blank)

    cv2.imwrite("./w3output/Senecabgr.png",blank)
    cv2.imwrite("./w3output/Senecabgr.jpg", blank)
    '''
        wait for keyboard key to be pressed 
        '''
    cv2.waitKey(0)
    cv2.destroyAllWindows()