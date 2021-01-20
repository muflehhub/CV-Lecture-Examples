"""
Created by Dr. Mufleh Al-Shatnawi
Copyright (c) 2021 Dr. Mufleh Al-Shatnawi. All rights reserved.

Read and display video
"""

import cv2
import numpy as np

if __name__ == '__main__':
  # Create a VideoCapture object and read from input file
  # If the input is the camera, pass 0 instead of the video file name
  cap = cv2.VideoCapture('./w2data/chaplin.mp4')
  # cap = cv2.VideoCapture('./w2data/Woman.avi')
  ### read your camera
  # cap = cv2.VideoCapture(0)

  # Check if camera opened successfully
  if (cap.isOpened()== False):
    print("Error opening video stream or file")

  # Read until video is completed
  while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

      # Display the resulting frame
      cv2.imshow('Frame',frame)

      # Press Q on keyboard to  exit
      if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    # Break the loop
    else:
      break

  # When everything done, release the video capture object
  cap.release()

  # Closes all the frames
  cv2.destroyAllWindows()
