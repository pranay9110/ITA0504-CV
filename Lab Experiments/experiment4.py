import cv2
import numpy as np

img = cv2.imread("image3.png")

kernel = np.ones((5,5), np.uint8)

dilate = cv2.dilate(img, kernel, iterations=1)

cv2.imwrite("Experiment4 output.png", dilate)

cv2.imshow("Dilated", dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()