#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:25:52 2023

@author: helenmiles
based on:
    https://docs.opencv.org/4.x/d9/dc8/tutorial_py_trackbar.html
    https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
"""

import cv2 as cv
import sys

cv.namedWindow('result')

# open the image in greyscale
filename = "" # ADD YOUR IMAGE NAME HERE!
img = cv.imread("./images/"+filename+".jpg", cv.IMREAD_GRAYSCALE)

# if the image is not loaded and the variable remains empty, give and error message
if img is None:
    sys.exit("Could not read the image.")
    
#create trackbars
def nothing(x):
    pass

# create trackbars for modding threshold values
cv.createTrackbar('Lower Threshold','result',0,255,nothing)
cv.createTrackbar('Higher Threshold','result',0,255,nothing)

result = img
while(1):
    cv.imshow('result',result)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    # read the trackbars into the canny fucntion
    thres1 = cv.getTrackbarPos('Lower Threshold','result')
    thres2 = cv.getTrackbarPos('Higher Threshold','result')
    result = cv.Canny(img,thres1,thres2)
    
cv.destroyAllWindows()