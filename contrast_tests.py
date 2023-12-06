import contrast_calculator as cc
import cv2 as cv

def print_image():
    img = cc.load_image("sample.jpg")
    print(img)

print_image()

