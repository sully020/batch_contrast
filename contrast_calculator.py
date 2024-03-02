
""" 
Author: Christopher Sullivan
Version: 0.1.0

This script loads in image files and calculates their respective contrast ratios by first converting them to grayscale, 
then calculating contrast values through both luminescence range and standard luminescence deviation.
"""

import cv2 as cv
from numpy import std
from os import listdir


def convert_gray(img):
    img = cv.cvtColor(img, 7, img, 0) 
    return img

def load_image(filename):
    img = cv.imread(filename)
    img = convert_gray(img)
    return img

def calc_range(img):
    min = img.min()
    max = img.max()
    if min == 0:
        min += 1
    return (str(max) + ": " + str(min))

def calc_by_sd(img):
    sd = std(img)
    sd = float("{:.2f}".format(sd))
    return sd

def iter_dir():
    dir = input('Please enter directory name/path: ')
    for img in listdir(dir):
        fname = dir + '/' + img
        img_dat = load_image(fname)
        print("Contrast by Range - " + img + ": " + calc_range(img_dat))
        print("Contrast by Standard Deviation - " + img + ": " + str(calc_by_sd(img_dat)))
        print("----------------")

def main():
    iter_dir()

if __name__ == "__main__":
    main()


