import cv2
import numpy as np

img_color = cv2.imread('shapes.jpg')
gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 50, 150)

# Hough Line Detection
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=50, maxLineGap=10)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img_color, (x1, y1), (x2, y2), (0,255,0), 2)

# Hough Circle Detection
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img_color, (i[0], i[1]), i[2], (255,0,0), 2)
        cv2.circle(img_color, (i[0], i[1]), 2, (0,0,255), 3)

cv2.imshow('Detected Shapes', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
