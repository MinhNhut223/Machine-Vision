import cv2                      #Sử dụng thư viện xử lý ảnh Opencv
from PIL import Image           #Thư viện xử lý ảnh Pillow hỗ trợ nhiều định dạng
import numpy as np              #Thư viện toán học, đặc biệt là tính toán ma trận
import matplotlib.pyplot as plt #Thu vien ve bieu do

#--------------------------------------------------------------------------------
#Thuật toán chuyển đổi ảnh màu RGB sang mức xám Grayscale dùng pp Luminance
#--------------------------------------------------------------------------------
def ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL):
    #Tạo một ảnh có cùng kích thước và mode với ảnh PIL
    #Ảnh này dùng để chứa kết quả chuyển đổi RGB sang Grayscale 
    average = Image.new(imgPIL.mode, imgPIL.size)

    #Lấy kích thước của ảnh từ imgPIL
    width = average.size[0]
    height = average.size[1]
    #Mỗi ảnh là một ma trận 2 chiều nên sẽ dùng 2 vòng for đọc hết các điểm ảnh (pixel)
    for x in range(width):
        for y in range(height):
            #Lấy giá trị điểm ảnh tại vị trí (x, y)
            R, G, B = imgPIL.getpixel((x, y))

            #Công thức chuyển đổi ảnh thành màu xám dùng Luminance
            gray = np.uint8(0.2126*R + 0.7152*G + 0.0722*B)

            #Gán giá trị mức xám vừa tính cho ảnh xám 
            average.putpixel((x, y), (gray, gray, gray))
    return average 
#--------------------------------------------------------------------------------
#End: ChuyenDoiAnhMauRGBSangAnhXamLuminance(HinhRGB)
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#Tính histogram của ảnh xám
#--------------------------------------------------------------------------------
def TinhHistogram(HinhXamPIL):
    #Mỗi pixel có giá trị từ 0-255, nên phải khai báo 1 mảng có 256 phần tử
    #để chứa số đếm của các pixel có cùng giá trị
    his = np.zeros(256)

    #Kích thước ảnh
    w = HinhXamPIL.size[0]
    h = HinhXamPIL.size[1]
    for x in range(w):
        for y in range(h):
            #Lấy giá trị xám tại điểm (x, y)
            gR, gG, gB = HinhXamPIL.getpixel((x, y))

            #Giá trị Gray tính ra cũng chính là phần tử thứ Gray trong mảng his
            #đã khai báo ở trên, sẽ tăng số đếm của phần tử thứ Gray lên 1
            #Lay 1 trong 3 gia tri
            his[gR] += 1
    
    return his
#--------------------------------------------------------------------------------
#End: TinhHistogram(HinhXamPIL):
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#Vẽ biểu đồ Histogram dùng thư viện matplotlib
#--------------------------------------------------------------------------------
def VeBieuDoHistogram(his):
    w = 5
    h = 4
    plt.figure('Bieu do histogram cua anh xam', figsize=(((w, h))), dpi=100)
    #Khai bao 1 mang gom 256 cho truc x
    trucX = np.zeros(256)
    trucX = np.linspace(0, 256, 256)
    plt.plot(trucX, his, color='orange')
    plt.title('Bieu do histogram')
    plt.xlabel('Gia tri muc xam')
    plt.ylabel('So diem cung gia tri muc xam')
    plt.show()
#--------------------------------------------------------------------------------
#End: def VeBieuDoHistogram()
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#                       Chay chuong trinh chinh
#--------------------------------------------------------------------------------
#Khai bao duong dan file hinh
filehinh = r'bird_small.jpg'

#Doc anh dung thu vien PIL
imgPIL = Image.open(filehinh)

#Chuyen sang anh muc xam
HinhXamPIL = ChuyenDoiAnhMauRGBSangAnhXamLuminance(imgPIL)

#Tinh histogram
his = TinhHistogram(HinhXamPIL)

#Chuyen anh PIL sang OpenCv de hien thi bang thu vien cv2
HinhXamCV = np.array(HinhXamPIL)
cv2.imshow('Anh muc xam', HinhXamCV)

#Hien thi bieu do histogram
VeBieuDoHistogram(his)

#Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ
cv2.destroyAllWindows()

#--------------------------------------------------------------------------------
#                       End: Chuong trinh chinh
#--------------------------------------------------------------------------------