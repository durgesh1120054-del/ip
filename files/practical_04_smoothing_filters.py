import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

# Gaussian smoothing
gaussian = cv2.GaussianBlur(img, (5,5), 0)

# Bilateral filtering
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(gaussian, cmap='gray')
plt.title('Gaussian Smoothing')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(bilateral, cmap='gray')
plt.title('Bilateral Smoothing')
plt.axis('off')

plt.show()
