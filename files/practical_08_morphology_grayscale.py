import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

kernel = np.ones((5,5), np.uint8)

# Dilation & Erosion
dilated_gray = cv2.dilate(img, kernel, iterations=1)
eroded_gray = cv2.erode(img, kernel, iterations=1)

# Opening & Closing
opening_gray = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing_gray = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

titles = ['Original', 'Dilation', 'Erosion', 'Opening', 'Closing']
images = [img, dilated_gray, eroded_gray, opening_gray, closing_gray]

for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()
