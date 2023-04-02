import cv2                  #Sử dụng thư viện xử lý ảnh Opencv
from PIL import Image       #Thư viện xử lý ảnh Pillow hỗ trợ nhiều định dạng
import numpy as np          #Thư viện toán học, đặc biệt là tính toán ma trận

#Khai báo đường dẫn file hình
filehinh = r'lena_colorjpg.jpg'

#Đọc ảnh màu dùng thư viện OpenCV
img = cv2.imread(filehinh, cv2.IMREAD_COLOR)

#Đọc ảnh màu dùng thư viện PIL
#Ảnh PIL dùng để thực hiện các tác vụ xử lý và tính toán thay vì OpenCV
imgPIL = Image.open(filehinh)

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

        #Công thức chuyển đổi ảnh thành màu xám dùng Lightness
        MIN = min(R, G, B)
        MAX = max(R, G, B)
        gray = np.uint8((MIN + MAX) / 2)

        #Gán giá trị mức xám vừa tính cho ảnh xám 
        average.putpixel((x, y), (gray, gray, gray))

#Chuyển ảnh từ PIL sang OpenCV để hiển thị bằng OpenCV
anhmucxam = np.array(average)

#Hiển thị ảnh dùng thư viện OpenCV
cv2.imshow('Anh mau RGB goc', img)
cv2.imshow('Anh muc xam Lightness', anhmucxam)

#Bấm phím bất kỳ để đóng cửa sổ hiển thị
cv2.waitKey(0)

#Giải phóng bộ nhớ đã cấp phát cho các cửa sổ
cv2.destroyAllWindows()