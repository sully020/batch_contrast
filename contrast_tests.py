import contrast_calculator as cc

def print_sample_dat():
    img = cc.load_image("images/sample.jpg")
    print(img)

def print_solid_dat():
    img = cc.load_image("images/solid.jpg")
    print(img)

def test_range():
    img = cc.load_image("images/sample.jpg")
    print(cc.calc_range(img))

def test_sd():
    img = cc.load_image("images/solid.jpg")
    print(cc.calc_by_sd(img))

def compare_diff_images():
    sample = cc.load_image("images/sample.jpg")
    sam_vals = cc.calc_range(sample)
    solid = cc.load_image("images/solid.jpg")
    sol_vals = cc.calc_range(solid)

    assert(sam_vals != sol_vals)

print_sample_dat()
print_solid_dat()

test_range()
test_sd()

compare_diff_images()