
""" 
Author: Christopher Sullivan
Version: 0.0.1

This script loads in image files and calculates their respective contrast ratios by first converting them to grayscale, 
then calculating contrast values through both luminescence range and standard luminescence deviation.
"""

import cv2 as cv

def load_image(filename):
    img = cv.imread(filename)
    return img

def convert_gray(img):
    img = cv.cvtColor(img, 7, img, 0) 
    return img

def find_intensities(img):
    min = img.min()
    max = img.max()
    return (min, max)
