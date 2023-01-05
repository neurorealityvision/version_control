#Define Python Library
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#test function for make rgb of pixel with image
def rgb_of_pixel (img_path, x, y):
    im = Image.open(img_path).convert("RGB")
    r,g,b = im.getpixel((x,y))
    a = (r,g,b)
    return a

img = "dog.jpg"
print (rgb_of_pixel(img,10,10))

"""
# step-2 Define Image size - height, width and depth
# (rows, columns, dimensions) format
height, width, channel = 64, 64, 3

# step-3 Define Red,Green,Blue Color -for each- 0 to 255
red, green, blue = 0, 0, 0

# step-4 Generate RGB Numpy Array
arr = np.full((height, width, channel), [red, green, blue], dtype=('uint8'))

# step-5 Show inline Image Plot
plt.imshow(arr)

# step-6 Remove edge numbers from Image Plot
plt.axis('off')
"""