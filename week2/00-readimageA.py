"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image and display it
"""
import cv2

import numpy as np


if __name__ == '__main__':
    '''
    When image is read, it will be a stream of raw numbers, in the form of NumPy array.
    
    For a color image, the shape is a tuple of (rows, columns, # of channels). 
    For RGB color image, the number of channels is 3.
    
    When image is read as a stream of numbers, all the number are of type ‘unsigned int — 8 bits’.
    
    Length of image will return the first value in the tuple, 
    basically it represents the number of rows i.e., the height of the image.
    
    By default, imread returns an image in the BGR color format even if the file uses a
    grayscale format. BGR represents the same color model as red-green-blue (RGB), but the
    byte order is reversed.
    
    cv2.IMREAD_COLOR: This is the default option, providing a 3-channel BGR image
     with an 8-bit value (0-255) for each channel.
     
    cv2.IMREAD_GRAYSCALE: This provides an 8-bit grayscale image. 
    
    cv2.IMREAD_ANYCOLOR: This provides either an 8-bit-per-channel BGR image or 
    an 8-bit grayscale image, depending on the metadata in the file.

    cv2.IMREAD_UNCHANGED: This reads all of the image data, including the alpha or 
    transparency channel (if there is one) as a fourth channel.

    cv2.IMREAD_ANYDEPTH: This loads an image in grayscale at its original bit 
    depth. For example, it provides a 16-bit-per-channel grayscale image if the file
    represents an image in this format.
    cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR: This combination loads an 
    image in BGR color at its original bit depth.
    
    cv2.IMREAD_REDUCED_GRAYSCALE_2: This loads an image in grayscale at half 
    its original resolution. For example, if the file contains a 640 x 480 image, it is
    loaded as a 320 x 240 image.
    
    cv2.IMREAD_REDUCED_COLOR_2: This loads an image in 8-bit-per-channel BGR color at half its original resolution.
    cv2.IMREAD_REDUCED_GRAYSCALE_4: This loads an image in grayscale at onequarter of its original resolution.
    
    cv2.IMREAD_REDUCED_COLOR_4: This loads an image in 8-bit-per-channel color at one-quarter of its original resolution.
    
    cv2.IMREAD_REDUCED_GRAYSCALE_8: This loads an image in grayscale at oneeighth of its original resolution.
    
    cv2.IMREAD_REDUCED_COLOR_8: This loads an image in 8-bit-per-channel color at one-eighth of its original resolution.
    
    '''




    img = cv2.imread("./w2data/opencv-logo50.png", 1)
    cv2.imshow("Original Image",img)
    # Check for invalid input
    if img is None:  # Check for invalid input
        print("Could not open or find the image")

    print('Type of the image : ', type(img))
    '''
    dtype: This is the datatype of the array's elements. For an 8-bit-per-channel
    image, the datatype is numpy.uint8.
    '''
    print('Image datatype: ', img.dtype)
    print()
    '''
    shape: This is a tuple describing the shape of the array. For an image, it contains
    (in order) the height, width, and—if the image is in color—the number of
    channels. The length of the shape tuple is a useful way to determine whether an
    image is grayscale or color. For a grayscale image, we have len(shape) == 2,
    and for a color image, len(shape) == 3.


    The shape method of a numpy array object  can be used to
    find the number of rows ( height ),
     number of columns ( width ) and the number of channels of the image

    '''
    print('Shape of the image : {}'.format(img.shape))
    #
    print('Image Hight in pixels  (rows) {}'.format(img.shape[0]))
    print('Image Width in pixels (columns) {}'.format(img.shape[1]))
    print('Dimension of Image {}'.format(img.ndim))
    #
    print('number of rows - length of Image {}'.format(len(img)))
    print('number of columns - length of Image[0] {}'.format(len(img[0])))
    print('number of channels - length of Image[0][0] {}'.format(len(img[0][0])))
    #
    # '''
    # size: This is the number of elements in the array. In the case of a grayscale
    # image, this is the same as the number of pixels. In the case of a BGR image, it is
    # three times the number of pixels because each pixel is represented by three
    # elements (B, G, and R).
    # '''
    print('Image size {}'.format(img.size))
    #
    #
    #
    #
    # #####<<< copy the image >>>#########
    # ### Assigning the image stored in numpy array img to
    # ### another numpy array image_copy
    #
    image_copy = img.copy()
    cv2.imshow('Copy image', image_copy)
    #
    #
    ###<<<>>>###
    '''
    Data type conversion :
    It is very common to convert the image format from unsigned int
    to floating point so that precision is not lost during calculations.
    Sometimes, we convert back to unsigned int to display or write image.
    '''
    # Convert from uint8 to float32
    imgfloat = np.float32(img)
    print('Image datatype for imgfloat: ', imgfloat.dtype)
    # Convert from float32 to uint8
    imguint = np.uint8(imgfloat)
    print('Image datatype for imguint : ', imguint.dtype)
    # displays the image
    cv2.imshow("Image after type conversion", imguint)
    cv2.imshow('Original image', img)

    #
    #
    #
    #
    imggray = cv2.imread("./w2data/opencv-logo50.png", cv2.IMREAD_REDUCED_COLOR_8)
    cv2.imshow('Grayscale image', imggray)
    imggray1 = cv2.imread("./w2data/opencv-logo50.png", cv2.IMREAD_REDUCED_GRAYSCALE_2)
    cv2.imshow('Grayscale image1', imggray1)
    #
    #
    '''
    wait for keyboard key to be pressed 
    '''
    cv2.waitKey(0)
    cv2.destroyAllWindows()



"""
Here are the file formats that are currently supported:

    Windows bitmaps - *.bmp, *.dib
    JPEG files - *.jpeg, *.jpg, *.jpe
    JPEG 2000 files - *.jp2
    Portable Network Graphics - *.png
    Portable image format - *.pbm, *.pgm, *.ppm
    Sun rasters - *.sr, *.ras
    TIFF files - *.tiff, *.tif


"""