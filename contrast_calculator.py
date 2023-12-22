
""" 
Author: Christopher Sullivan
Version: 0.0.1

This script loads in image files and calculates their respective contrast ratios by first converting them to grayscale, 
then calculating contrast values through both luminescence range and standard luminescence deviation.
"""

import cv2 as cv
from numpy import std

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

def calc_by_range():
    img = load_image('solid.jpg')
    light_vals = find_intensities(img)
    contrast = (light_vals[1] - light_vals[0])
    return contrast

def calc_by_sd():
    img = load_image('sample.jpg')
    sd = std(img)
    sd = float("{:.2f}".format(sd))
    return sd