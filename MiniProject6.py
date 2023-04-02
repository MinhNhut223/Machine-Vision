import cv2
from PIL import Image               #Thư viện xử lý ảnh Pillow hỗ trợ nhiều định dạng
import numpy as np

#Khai bao duong dan file hinh
filehinh = r'lena_colorjpg.jpg'

#Doc anh mau dung thu vien openCV
img = cv2.imread(filehinh,cv2.IMREAD_COLOR)

#Đọc ảnh màu dùng thư viện PIL
#Ảnh PIL dùng để thực hiện các tác vụ xử lý và tính toán thay vì dùng OpenCV
imgPIL = Image.open(filehinh)

#Tạo một ảnh có cùng mode và kích thước với ảnh PILimg
Cyan = Image.new(imgPIL.mode, imgPIL.size)
Magenta = Image.new(imgPIL.mode, imgPIL.size)
Yellow = Image.new(imgPIL.mode, imgPIL.size)
Black = Image.new(imgPIL.mode, imgPIL.size)

#Lay kich thuoc anh
w = imgPIL.size[0]
h = imgPIL.size[1]

#Mỗi ảnh là 1 ma trận nên dùng 2 lệnh for
for x in range(w):
    for y in range(h):
        #Lay gia tri diem anh tai vi tri (x, y)
        R, G, B = imgPIL.getpixel((x,y))
        #Tron cac kenh mau cho ra C M Y K
        #Màu Cyan (xanh dương) là kết hợp giữa G và B --> set R = 0
        Cyan.putpixel((x,y),(B,G,0))
        #Màu Magento (tim) là kết hợp giữa R và B --> set G = 0
        Magenta.putpixel((x,y),(B,0,R))
        #Màu Yellow (vang) là kết hợp giữa R và G --> set B = 0
        Yellow.putpixel((x,y),(0,G,R))
        #Màu Black là mấy MIN(R, G, B)
        k= min(R, G, B)
        Black.putpixel((x,y),(k, k, k))

#Chuyển ảnh từ PIL sang openCV
C = np.array(Cyan)
M = np.array(Magenta)
Y = np.array(Yellow)
K = np.array(Black)

#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh goc', img)
cv2.imshow('Anh kenh Cyan', C)
cv2.imshow('Anh kenh Magenta', M)
cv2.imshow('Anh kenh Yellow', Y)
cv2.imshow('Anh kenh Black', K)

#Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giai phong bo nho da cap phat cho cac cua so hien thi hinh
cv2.destroyAllWindows()

