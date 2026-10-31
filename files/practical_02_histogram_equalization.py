import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

hist_eq = cv2.equalizeHist(img)

plt.subplot(1,2,1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(hist_eq, cmap='gray')
plt.title('Histogram Equalized')
plt.axis('off')

plt.show()
