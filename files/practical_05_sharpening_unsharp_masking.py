import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

# Sharpening
kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
sharpened = cv2.filter2D(img, -1, kernel)

# Unsharp Masking
blur = cv2.GaussianBlur(img, (9,9), 10.0)
unsharp = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(sharpened, cmap='gray')
plt.title('Sharpened')
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(unsharp, cmap='gray')
plt.title('Unsharp Masking')
plt.axis('off')

plt.show()
