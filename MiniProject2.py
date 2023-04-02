import cv2
import numpy as np

#Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('lena_color.png', cv2.IMREAD_COLOR)

#Lay kich thuoc cua anh
height = len(img[0])
width = len(img[1])

#Khai bao 3 bien de chua 3 kenh hinh R G B
red = np.zeros((width, height, 3), np.uint8)
    #So 3 la 3 kenh R G B, moi kenh 8bit
green = np.zeros((width, height, 3), np.uint8)
blue = np.zeros((width, height, 3), np.uint8)

#Ban dau set zero cho tat ca diem anh co trong ca 3 kenh 
#trong moi hinh
red[:] = [0, 0, 0]
green[:] = [0, 0, 0]
blue[:] = [0, 0, 0]

#Moi hinh la 1 ma tran 2 chieu nen dung 2 vong for
for x in range(width):
    for y in range(height):
        #Lay gia tri diem anh tai vi tri (x, y)
        R = img[x, y, 2]
        G = img[x, y, 1]
        B = img[x, y, 0]

        #Thiet lap mau cho cac kenh
        red[x, y, 2] = R
        green[x, y, 1] = G
        blue[x, y, 0] = B

#Hiển thị dùng thư viện OpenCV
cv2.imshow('Hinh mau RGB goc', img)
cv2.imshow('Kenh RED', red)
cv2.imshow('Kenh GREEN', green)
cv2.imshow('Kenh BLUE', blue)

#Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giai phong bo nho da cap phat cho cac cua so hien thi hinh
cv2.destroyAllWindows()

