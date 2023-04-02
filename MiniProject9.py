import cv2
from PIL import Image
import numpy as np

hinhgoc = r'lena_colorjpg.jpg'
img = cv2.imread(hinhgoc, cv2.IMREAD_COLOR)
imgPIL = Image.open(hinhgoc)
width = imgPIL.size[0]
height = imgPIL.size[1]

Ximg = Image.new(imgPIL.mode, imgPIL.size)
Yimg = Image.new(imgPIL.mode, imgPIL.size)
Zimg = Image.new(imgPIL.mode, imgPIL.size)
XYZimg = Image.new(imgPIL.mode, imgPIL.size)

for x in range(width):
    for y in range(height):
        R, G, B = imgPIL.getpixel((x,y))
        
        X = np.uint8(0.4124564*R + 0.3575761*G + 0.1804375*B)
        Y = np.uint8(0.2126729*R + 0.7151522*G + 0.0721750*B)
        Z = np.uint8(0.0193339*R + 0.1191920*G + 0.9503041*B)

        Ximg.putpixel((x,y),(X, X, X))
        Yimg.putpixel((x,y),(Y, Y, Y))
        Zimg.putpixel((x,y),(Z, Z, Z))
        XYZimg.putpixel((x,y),(X, Y, Z))
        
KX = np.array(Ximg)
KY = np.array(Yimg)
KZ = np.array(Zimg)
HXYZ = np.array(XYZimg)

cv2.imshow('Hinh goc', img)
cv2.imshow('Kenh X', KX)
cv2.imshow('Kenh Y', KY)
cv2.imshow('Kenh Z', KZ)
cv2.imshow('Hinh XYZ', HXYZ)

cv2.waitKey(0)
cv2.destroyAllWindows()