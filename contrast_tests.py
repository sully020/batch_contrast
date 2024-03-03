import contrast_calculator as cc
from time import time

def print_sample_dat():
    img = cc.load_image("images/sample.jpg")
    print(img)

def print_solid_dat():
    img = cc.load_image("images/solid.jpg")
    print(img)

def test_range():
    img = cc.load_image("images/sample.jpg")
    print(cc.calc_range(img))
    img = cc.load_image("images/solid.jpg")
    print(cc.calc_range(img))

def test_sd():
    img = cc.load_image("images/solid.jpg")
    print(cc.calc_by_sd(img))
    img = cc.load_image("images/sample.jpg")
    print(cc.calc_by_sd(img))

def compare_diff_images():
    sample = cc.load_image("images/sample.jpg")
    sam_vals = cc.calc_range(sample)
    solid = cc.load_image("images/solid.jpg")
    sol_vals = cc.calc_range(solid)

    assert(sam_vals != sol_vals)

def time_iter_dir():
    dir = input('Please enter directory name/path: ')
    start = (time() * 1000) // 1
    cc.iter_dir(dir)
    end = (time() * 1000) // 1
    print(str(end - start) + "ms")

#print_sample_dat()
#print_solid_dat()

#test_range()
#test_sd()

#compare_diff_images()
time_iter_dir()