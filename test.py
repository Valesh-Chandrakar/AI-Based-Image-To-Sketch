
# Converting of image into sketch
import numpy as np
import imageio as codereader
import scipy.ndimage
import cv2 as codewriter

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5870,0.1140])  # used to convert 2d array in grayscale

def imgsk(front,back):
    final_sketch = front*255/(255-back) # formula to convert image to sketch
    #if the image is greater then 255 which i don't think is possible but still if it is there will convert
    final_sketch[final_sketch>255]=255
    final_sketch[back==255]=255
    return final_sketch.astype('uint8')

image1 = "pxfuel.jpg"  # from where i import file

imagereader = codereader.imread(image1) # img src

color = rgb2gray(imagereader) # convert image to black and white color by grayscale

v = 255-color

blur = scipy.ndimage.filters.gaussian_filter(v,sigma =10) # sigma is used for blurnes of img

a = imgsk(blur,color) # this func. convert img to sketch

#saving the result
codewriter.imwrite('new.jpg',a)































