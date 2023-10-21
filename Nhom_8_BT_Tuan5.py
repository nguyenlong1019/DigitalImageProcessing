import cv2
import numpy as np

# Đọc ảnh gốc
image = cv2.imread('dragon_ai.png')

# Chuyển đổi ảnh thành ảnh grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tạo một ma trận ngẫu nhiên cùng kích thước với ảnh grayscale
random_matrix = np.random.randint(0, 256, gray_image.shape, dtype=np.uint8)

# Áp dụng phối màu ngẫu nhiên bằng cách cộng ảnh grayscale với ma trận ngẫu nhiên
dithered_image = cv2.add(gray_image, random_matrix)

# Hiển thị ảnh gốc và ảnh đã phối màu ngẫu nhiên
cv2.imshow('Original Image', image)
cv2.imshow('Dithered Image', dithered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
