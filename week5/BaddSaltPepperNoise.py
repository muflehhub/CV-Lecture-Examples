
"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read an image add salt and pepper noise

"""
import cv2

import numpy as np




def addSaltAndPepperNoise(img,snr=0.9):
    """
    add solt and pepper noise
    # Specify the signal to noise ratio
    :param img:
    :param snr:
    :return:
    """
    print(snr)
    noiseimg=img.copy()


    number_of_noise_pixels = int((1-snr) * img.size)
    for i in range(number_of_noise_pixels):

        # Pick a random x coordinate
        randX=np.random.randint(0,img.shape[0])
        # Pick a random y coordinate
        randY=np.random.randint(0,img.shape[1])
        if img.ndim ==3:
            randch =np.random.randint(0,img.shape[2])
        ### randomly pick salt or pepper
        if np.random.randint(0,2)==0:
            if img.ndim==3:
                noiseimg[randX,randY,randch]=0 #0 is pepper noise
            else:
                noiseimg[randX, randY] = 0  # 0 is pepper noise
        else:
            if img.ndim == 3:
                noiseimg[randX,randY,randch]=255 #1 is salt particle noise
            else:
                noiseimg[randX, randY] = 255

    return noiseimg




if __name__ == '__main__':

    imgsrc = cv2.imread('./w5data/lena.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_2)
    # imgsrc = cv2.imread('./w5data/lena.jpg', cv2.IMREAD_REDUCED_COLOR_2)
    # imgsrc = cv2.imread('./w5data/ImageC.jpg', cv2.IMREAD_COLOR)
    # imgsrc = cv2.imread('./w5data/ImageA.jpg',cv2.IMREAD_COLOR)
    # imgsrc = cv2.imread('./w5data/ImageA.jpg', cv2.IMREAD_GRAYSCALE)

    for i in range(11):
        imgnoisey= addSaltAndPepperNoise(imgsrc,i/10.)
        cv2.imshow('SP%d-%i'%(100-i*10,i),imgnoisey)
        cv2.imwrite('./w5output/leangreaySP%d-%i.jpg'%(100-i*10,i), imgnoisey)

    cv2.imshow("original", imgsrc)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
