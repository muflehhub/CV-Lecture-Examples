"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and display new image with padding
by keeping the aspect ratio

based on https://jdhao.github.io/2017/11/06/resize-image-to-square-with-padding/


"""
import cv2

import numpy as np

if __name__ == '__main__':
    img = cv2.imread("./w3data/messi5.jpg", cv2.IMREAD_REDUCED_COLOR_2)
    print(img.shape)
    cv2.imshow('BGR image', img)
    desired_size = 250

    old_size = img.shape[:2]  # old_size is in (height, width) format

    ratio = float(desired_size) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])
    print (new_size)

    # new_size should be in (width, height) format
    img = cv2.resize(img, (new_size[1], new_size[0]))

    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)

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
    black_color = [0, 0, 0]
    newimgA = cv2.copyMakeBorder(img.copy(), top, bottom, left, right, cv2.BORDER_CONSTANT,
                                value=black_color)

    cv2.imshow("Image padding A", newimgA)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
