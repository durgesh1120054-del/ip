# Imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
img = cv2.imread('image.jpg', 0)

# Log Transformation
img_f = img.astype(np.float64)
c = 255 / np.log(1 + np.max(img_f))
log_transformed = c * np.log(1 + img_f)
log_transformed = np.array(log_transformed, dtype=np.uint8)

# Power-law (Gamma) Transformation
gamma = 0.5
gamma_corrected = np.array(255*(img/255)**gamma, dtype=np.uint8)

# Contrast Adjustment
alpha = 1.5  # Contrast
beta = 50    # Brightness
contrast_adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

# Display results
titles = ['Original', 'Log Transform', 'Gamma Correction', 'Contrast Adjusted']
images = [img, log_transformed, gamma_corrected, contrast_adjusted]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.show()
