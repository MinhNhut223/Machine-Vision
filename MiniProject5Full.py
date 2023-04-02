import cv2                          #Sử dụng thư viện xử lý ảnh Opencv
from PIL import Image               #Thư viện xử lý ảnh Pillow hỗ trợ nhiều định dạng
import numpy as np                  #Thư viện toán học, đặc biệt là tính toán ma trận
import matplotlib.pyplot as plt     #Thu vien ve bieu do

#Hàm chuyển đổi ảnh màu sang ảnh xám dùng Lumunance
def chuyendoianhmauRGBsanganhxamluminance(imgPIL):
    luminance = Image.new(imgPIL.mode, imgPIL.size)
    width = luminance.size[0]
    height = luminance.size[1]
    
    for x in range(width):
        for y in range(height):
            R, G, B = imgPIL.getpixel((x, y))
            gray_luminance = np.uint8(0.2126 * R + 0.7152 * G + 0.0722 * B)

            luminance.putpixel((x, y), (gray_luminance, gray_luminance, gray_luminance))
            
    return luminance

#Tính histogram cho ảnh xám    
def tinhhistogram(hinhxampil):
    #khai báo 1 mảng có 256 phân tử để chứ số đếm của pixel
    hisxam = np.zeros(256)

    w = hinhxampil.size[0]
    h = hinhxampil.size[1]

    for x in range(w):
        for y in range(h):
            gray = hinhxampil.getpixel((x, y))
            #giá trị gray tính ra cũng chính là phần tử thứ gray trong 
            #mảng his đã khai báo ở trên, sẽ tăng phần tử thứ gray lên 1
            hisxam[gray] += 1
            
    return hisxam

#Tính histogram ảnh màu RGB
def tinhhistogram(imgPIL):
    hisRGB = np.zeros((256, 3))

    w = imgPIL.size[0]
    h = imgPIL.size[1]

    for x in range(w):
        for y in range(h):
            R, G, B = imgPIL.getpixel((x, y))

            hisRGB[R, 0] += 1
            hisRGB[G, 1] += 1
            hisRGB[B, 2] += 1
            
    return hisRGB

#Vẽ biểu đồ ảnh xám
def vebieudohisxam(hisxam):
    w = 5
    h = 4
    plt.figure('Biểu đồ Histogram ảnh xám', figsize=(w, h), dpi=100)
    trucX = np.linspace(0, 256, 256)
    plt.plot(trucX, hisxam, color='orange')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá trị mức xám')
    plt.ylabel('Số điểm cùng giá trị mức xám')
    plt.show()

#Vẽ biểu đồ ảnh màu
def vebieudohispixel(hisRGB):
    w = 5
    h = 4
    plt.figure('Biểu đồ Histogram ảnh RGB', figsize=(w, h), dpi=100)
    trucX = np.linspace(0, 256, 256)
    plt.plot(trucX, hisRGB[:, 0], color='r')
    plt.plot(trucX, hisRGB[:, 1], color='g')
    plt.plot(trucX, hisRGB[:, 2], color='b')
    plt.title('Biểu đồ Histogram')
    plt.xlabel('Giá trị pixel')
    plt.ylabel('Số điểm cùng giá trị pixel')
    plt.show()

#Khai bao duong dan file hinh
filehinh = r'bird_small.jpg'

#Đọc ảnh màu dùng thư viện PIL
#Ảnh PIL dùng để thực hiện các tác vụ xử lý và tính toán thay vì dùng OpenCV
imgPIL = Image.open(filehinh)

hinhxampil = chuyendoianhmauRGBsanganhxamluminance(imgPIL)
hisxam = tinhhistogram(hinhxampil)
hisRGB = tinhhistogram(imgPIL)

#chuyển ảnh PIL sang OPENCV để hiển thị bằng thư viện cv2
hinhxamCV = np.array(hinhxampil)
cv2.imshow('Ảnh mức xám', hinhxamCV)

vebieudohisxam(hisxam)
vebieudohispixel(hisRGB)

#Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giai phong bo nho da cap phat cho cac cua so hien thi hinh
cv2.destroyAllWindows()