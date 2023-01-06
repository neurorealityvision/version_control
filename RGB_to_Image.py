#Define Python Library
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

#read the image file
im = Image.open('dog.jpg')
pix = np.array(im)
height = im.size[1]
width = im.size[0]
print("Size :", width ,"x", height)

#make 3-dimension RGB data
numpy_array = np.array(im, dtype="uint8")
print(numpy_array)
print("######################")

#convert 3-dimension RGB data into 1-dimension
flatten_numpy_array = np.ravel(numpy_array, order='C')
print(flatten_numpy_array)

#this is for test
#save txt file of rgb data of picture
#np.savetxt("dog_rgb_data", flatten_numpy_array)

#load txt data
loaded_array = np.loadtxt("dog_rgb_data",dtype='uint8')

#reshape flatten data into 3-dimension
print("######################")
reshaped_numpy_array = loaded_array.reshape(height,width,3)
print(reshaped_numpy_array)

image2 = Image.fromarray(reshaped_numpy_array, 'RGB')
image2.show()



