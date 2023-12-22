import contrast_calculator as cc
import cv2 as cv

def print_image():
    img = cc.load_image("sample.jpg")
    print(img)

def print_gray():
    img = cc.load_image("sample.jpg")
    img = cc.convert_gray(img)
    print(img)

def find_sample_intens():
    img = cc.load_image("sample.jpg")
    print(cc.find_intensities(img))

def find_solid_intens():
    img = cc.load_image("solid.jpg")
    print(cc.find_intensities(img))


print_image()
print_gray()

find_sample_intens()
find_solid_intens()

