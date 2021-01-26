"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and display new image with padding

resize the image

"""
import cv2

import numpy as np

if __name__ == '__main__':
    img = cv2.imread("./w3data/messi5.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    print(img.shape)
    cv2.imshow('BGR image', img)
    ### << original size of messi is (h=171, w=274) >>
    ## how to make this image 350 to 350 with
    ht, wd, cc = img.shape
    # create new image of desired size and color (black) for padding
    ### Fact: new image is bigger than the original image
    new_wt = 350
    new_ht = 350
    color = (0, 0, 0)
    newimg = np.full((new_ht, new_wt, cc), color, dtype=np.uint8)
    # compute center offset
    x_offset = (new_wt - wd) // 2
    y_offset = (new_ht - ht) // 2
    # copy img image into center of result image
    newimg[y_offset:y_offset + ht, x_offset:x_offset + wd] = img
    print (newimg.shape)
    # view new image
    cv2.imshow("Image padding", newimg)

    # <<< using cv2.copyMakeBorder>>
    '''
    src: It is the source image.
    top: It is the border width in number of pixels in top direction.
    bottom: It is the border width in number of pixels in bottom direction.
    left: It is the border width in number of pixels in left direction.
    right: It is the border width in number of pixels in right direction.
    borderType: It depicts what kind of border to be added. 
                It is defined by flags like cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc
    value: It is an optional parameter which depicts color of border if border type is cv2.BORDER_CONSTANT.
    '''
    black_color = (0, 0, 0)
    newimgA = cv2.copyMakeBorder(img.copy(), 20, 20, 35, 10, cv2.BORDER_CONSTANT, value=black_color)
    cv2.imshow("Image padding A", newimgA)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
