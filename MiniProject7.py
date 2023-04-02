import cv2              #Thu vien xu ly anh OpenCV
from PIL import Image   #Thu vien xu ly anh Pillow
import numpy as np      #Thu vien toan hoc
import math

#Khai bao duong dan chua file hinh
filehinh = r'lena_colorjpg.jpg'

#Doc anh mau dung thu vien OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

#Doc anh mau dung thu vien Pillow
imgPIL = Image.open(filehinh)

#Tao anh co cung kich thuoc va mode voi anh PIL
Hue         = Image.new(imgPIL.mode, imgPIL.size)
Saturation  = Image.new(imgPIL.mode, imgPIL.size)
Intensity   = Image.new(imgPIL.mode, imgPIL.size)
HSIimg      = Image.new(imgPIL.mode, imgPIL.size)

#Lay kich thuoc anh
width = imgPIL.size[0]
height= imgPIL.size[1]

for x in range(width):
    for y in range(height):
        #Lay gia tri anh tai vi tri x y
        R, G, B = imgPIL.getpixel((x,y))
        MIN = min(R, G, B)
        SUM = (R + G + B)
        MAX = max(R, G, B)

        #Ap dung cong thuc
        #t1 la tu so
        t1 = ((R-G)+ (R-B))/2

        #t2 la mau so
        t2 = math.sqrt((R-G)*(R-G) + (R-B)*(G-B))

        #Ket qua tra ve cua Acos la radian
        theta = math.acos(t1/t2)

        #Cong thuc gia tri Hue
        H = 0
        if B<=G:
            H = theta
        else:
            #Do theta la radian nen dung Pi
            H = 2*math.pi - theta

        #Chuyen doi Radian sang Do
        H = np.uint8(H*180/math.pi)

        #Cong thuc tinh gia tri Saturation
        S = 1 - 3 * MIN/SUM
        S = np.uint8(S*255)

        #Cong thuc tinh gia tri Intensity
        I = SUM / 3
        I = np.uint8(I)

        Hue.putpixel((x,y),(H,H,H))
        Saturation.putpixel((x,y),(S,S,S))
        Intensity.putpixel((x,y),(I,I,I))
        HSIimg.putpixel((x,y),(I,S,H))

anhH = np.array(Hue)
anhS = np.array(Saturation)
anhI = np.array(Intensity)
anhHSI = np.array(HSIimg)

#Hien thi anh dung OpenCV
cv2.imshow('Anh Goc', img)
cv2.imshow('Kenh Hue', anhH)
cv2.imshow('Kenh Saturation', anhS)
cv2.imshow('Kenh Intensity', anhI)
cv2.imshow('Anh HSI', anhHSI)

cv2.waitKey(0)
cv2.destroyAllWindows()




