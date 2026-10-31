import cv2
import matplotlib.pyplot as plt

img = cv2.imread('noisy_image.jpg', 0)

# Linear smoothing
linear_smooth = cv2.blur(img, (5,5))

# Non-linear smoothing
nonlinear_smooth = cv2.medianBlur(img, 5)

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(linear_smooth, cmap='gray')
plt.title('Linear Smoothing')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(nonlinear_smooth, cmap='gray')
plt.title('Non-linear Smoothing')
plt.axis('off')

plt.show()
