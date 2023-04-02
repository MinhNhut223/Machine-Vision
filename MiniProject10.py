import cv2
from PIL import Image
import numpy as np

hinhgoc = r'lena_colorjpg.jpg'
img = cv2.imread(hinhgoc, cv2.IMREAD_COLOR)
imgPIL = Image.open(hinhgoc)
width = imgPIL.size[0]
height = imgPIL.size[1]

Yimg = Image.new(imgPIL.mode, imgPIL.size)
Cbimg = Image.new(imgPIL.mode, imgPIL.size)
Crimg = Image.new(imgPIL.mode, imgPIL.size)
YCbCrimg = Image.new(imgPIL.mode, imgPIL.size)

for x in range(width):
    for y in range(height):
        R, G, B = imgPIL.getpixel((x,y))
        
        Y = np.uint8(16 + (65.738*R)/256 + (129.057*G)/256 + (25.064*B)/256)
        CB = np.uint8(128 - (37.945*R)/256 - (74.494*G)/256 + (112.439*B)/256)
        CR = np.uint8(128 + (112.439*R)/256 - (94.154*G)/256 - (18.285*B)/256)

        Yimg.putpixel((x,y),(Y, Y, Y))
        Cbimg.putpixel((x,y),(CB, CB, CB))
        Crimg.putpixel((x,y),(CR, CR, CR))
        YCbCrimg.putpixel((x,y),(Y, CB, CR))
        
KY = np.array(Yimg)
KCB = np.array(Cbimg)
KCR = np.array(Crimg)
HYCbCr = np.array(YCbCrimg)

cv2.imshow('Hinh goc', img)
cv2.imshow('Kenh Y', KY)
cv2.imshow('Kenh Cb', KCB)
cv2.imshow('Kenh Cr', KCR)
cv2.imshow('Hinh YCbCr', HYCbCr)

cv2.waitKey(0)
cv2.destroyAllWindows()