import contrast_calculator as cc

def print_sample():
    img = cc.load_image("images/sample.jpg")
    img = cc.convert_gray(img)
    print(img)

def print_solid():
    img = cc.load_image("images/sample.jpg")
    img = cc.convert_gray(img)
    print(img)

def find_sample_intens():
    img = cc.load_image("images/sample.jpg")
    img = cc.convert_gray(img)
    print(cc.find_intensities(img))

def find_solid_intens():
    img = cc.load_image("images/solid.jpg")
    img = cc.convert_gray(img)
    print(cc.find_intensities(img))

def compare_outputs():
    sample = cc.load_image("images/sample.jpg")
    sample = cc.convert_gray(sample)
    sam_vals = cc.find_intensities(sample)
    solid = cc.load_image("images/solid.jpg")
    solid = cc.convert_gray(solid)
    sol_vals = cc.find_intensities(solid)

    assert(sam_vals != sol_vals)

print_sample()
print_solid()

find_sample_intens()
find_solid_intens()

compare_outputs()