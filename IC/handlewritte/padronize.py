import os,sys
import tensorflow as tf
import numpy as np


from PIL import Image, ImageChops, ImageDraw


def centering_img(img):

    width, height = img.size
    left,top,right,bottom = width, height, -1, -1
    imgpix = img.getdata()

    for y in range(height):
        yoffset = y*width
        for x in range(width):
            if imgpix[yoffset + x] < 255:
                # do not use GetPixel and SetPixel, it is so slow.
                    if x < left: left   = x
                    if y < top: top     = y
                    if x > right: right = x
                    if y > bottom: bottom = y   
                            
    shiftX = int((left + (right - left) / 2) - width / 2)
    shiftY = int((top + (bottom - top) / 2) - height / 2)

    return ImageChops.offset(img, -shiftX, -shiftY)

def image_reshape():
    img = Image.open("8.png").convert('L')
    img = centering_img(img)
    img.thumbnail((28,28))
    img = np.array(img, dtype=np.float32)
    img = 1 - np.array(img / 255)
    img = img.reshape(1, 784)

    return img