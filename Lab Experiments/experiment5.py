import cv2
import numpy as np

img = cv2.imread("image4.png")

kernel = np.ones((5,5), np.uint8)

erode = cv2.erode(img, kernel, iterations=1)

cv2.imwrite("Experiment5 output.png", erode)

cv2.imshow("Eroded", erode)
cv2.waitKey(0)
cv2.destroyAllWindows()