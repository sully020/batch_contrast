import contrast_calculator as cc
import cv2 as cv

def print_image():
    img = cc.load_image("sample.jpg")
    print(img)


def print_gray():
    img = cc.load_image("sample.jpg")
    img = cc.convert_gray(img)
    print(img)

print_image()
print_gray()

