#CV-Lecture-Examples
#Computer Vision Course Lecture Examples

This Repository contains python files for the lecture examples. 
# Course TimeTable
## Week2-Reading and writing Image Files and Video files (Cameras)
### Overview of Digital images in OpenCV-Python
### Read an image using OpenCV-Python
### Create your own image using OpenCV-Python
### Modify image pixels using OpenCV-Python
### Work with ROI: extract and add using OpenCV-Python
### Create your video from list of images using OpenCV-Python
### Resize video or images using OpenCV-Python

## Week3 - Digital Image Color Models and Converting between these color models
### Simple Digital Image Processing
### Simple Digital Image Enhancement in Spatial domain
### Intensity Transformations for digital images used Log Transformations 
### Intensity Transformations for digital images used Power Law Transformations (Gamma Correction)
### Digital Image Thresholding
- How to split the different color channels and view it OpenCV - Python (cv2.split(image))
- How to convert between color modes using OpenCV - Python (cv2.cvtColor)
- How to perform image cropping cropping using OpenCV - Python (Numpy slicing)
- How to perform image padding using OpenCV - Python (cv2.copyMakeBorder )
- How to perform image enhancement(or Intensity Transformations) in spatial domain using OpenCV - Python (cv2.addWeighted())
- How to perform Alpha blending for images using OpenCV - Python (cv2.addWeighted())
- How to perform a simple digital image thresholding using OpenCV - Python (cv2.threshold)

## Week4 - Introduction to Digital Image Histogram
### Define what is Image Contrast
### Define what is Image Brightness
### How to Find or Compute the Image Histogram
### Perform simple Histogram Sliding operation 
### What is the Probability Mass Function (PMF)of the Histogram 
### What is the Cumulative Distribution Function (CDF) of the Histogram
### Perform Histogram equalization for Greyscale or colored images
### Find 2D or  3D Image Histograms
- How to compute image histogram using nested for loop 
- How to compute image histogram using numpy.histogram 
- How to compute image 1D, 2D or 3D histogram using OpenCV - Python (cv2.calcHist)
- cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
- How to perform image histogram equalization using OpenCV - Python (cv2.equalizeHist)

## Week5 - Digital Image Noise and Filtering
### Adding Noise to Digital Image 
### Add Salt and Pepper Noise to grayscale and  color images 
### Add Gaussian Noise to image to grayscale or color images
### Digital image Filtering (Linear and nonlinear)
### Mean Filter, Average Filter, or Box Filter
### Gaussian Filtering
### Median Filtering
- How to add noise to image using OpenCV-Python
- How to apply mean/average/box filter using OpenCV-Python: imgdsc = cv2.blur(src=imgsrc,ksize=(3,3))
- How to apply Gaussian filter using OpenCV-Python: imgdsc = cv2.GaussianBlur(src=imgsrc,ksize=(3,3),sigmaX=0)
- How to apply Median filter using OpenCV-Python: imgdsc= cv2.medianBlur(src=imgsrc, ksize= 3)

## Week5 - Binary Images and  Morphological  processing
### Introduction to Binary images
### Image Thresholding
#### Simple thresholding
#### Adaptive Thresholding
### Morphological Operations/Transformations
#### Fit or Hit for Structure Element 
#### Dilation 
#### Erosion
#### Morphological operations: opening and closing
- How to apply OpenCV Image Thresholding using cv2.threshold(source, thresholdValue, maxVal, thresholdingTechnique)
- How to apply OpenCV Thresholding Techniques: cv2.THRESH_BINARY,cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC, cv2.THRESH_TOZERO and cv2.THRESH_TOZERO_INV
- How to apply OpenCV: Adaptive Thresholding using cv2.adaptiveThreshold(source, maxVal, adaptiveMethod, thresholdType, blocksize, constant)
- How to apply dilate operation using OpenCV-Python cv2.dilate
- How to apply erosion operation using OpenCV-Python cv2.erode
- How to apply Opening and Closing operations using OpenCV-Python: cv2.morphologyEx(imgsrc, cv2.MORPH_OPEN, kernel), cv2.morphologyEx(imgsrc, cv2.MORPH_CLOSE, kernel)











