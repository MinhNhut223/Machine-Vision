import cv2                      #Sử dụng thư viện xử lý ảnh Opencv
import numpy as np              #Thư viện toán học, đặc biệt là tính toán ma trận
import matplotlib.pyplot as plt #Thu vien ve bieu do

#Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread('bird_small.jpg', cv2.IMREAD_COLOR)

#Tính toán Histogram cho ảnh R G B
#Thư viện OpenCV cung cấp hàm calcHist để tính toán histogram và vẽ biểu đồ
#cho ảnh R G B
#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
#images: là ảnh gốc dạng uint8
#channels: Đây là chỉ số của kênh tính toán biểu đồ.Đối với hình ảnh màu, 
#có thể truyền [0], [1] hoặc [2] để tính toán biểu đồ của kênh màu R G B tương ứng.
#mask: Để tìm biểu đồ của hình ảnh đầy đủ, mask để ở chế độ None. Muốn tìm biểu đồ 
#của vùng ảnh cụ thể, phải tạo một mặt nạ hình ảnh cho vùng đó.
#histSize: thể hiện số lượng BIN. Giá trị 256 là ảnh có giá trị 0-255
#ranges: là phạm vi như đã nói, giá trị nằm trong khoảng [0, 256]
blue = cv2.calcHist([img], [0], None, [256], [0, 256])
red = cv2.calcHist([img], [1], None, [256], [0, 256])
green = cv2.calcHist([img], [2], None, [256], [0, 256])

#Hiển thị ảnh gốc
cv2.imshow('Anh goc', img)

#Vẽ biểu đồ Histogram dùng thư viện matplotlib
w = 5
h = 4
plt.figure('Bieu do histogram cua anh R G B', figsize=(((w, h))), dpi=100)
#Khai bao 1 mang gom 256 cho truc x
trucX = np.zeros(256)
trucX = np.linspace(0, 256, 256)
plt.plot(trucX, red, color='red')
plt.plot(trucX, green, color='green')
plt.plot(trucX, blue, color='blue')
plt.title('Bieu do histogram')
plt.xlabel('Gia tri R G B')
plt.ylabel('So diem cung gia tri R G B')
plt.show()

#Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ
cv2.destroyAllWindows()
