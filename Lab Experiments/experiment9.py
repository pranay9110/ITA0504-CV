import cv2

img = cv2.imread("image8.png")

clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
counter = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite("Experiment9 Clockwise output.png", clockwise)
cv2.imwrite("Experiment9 CounterClockwise output.png", counter)

cv2.imshow("Clockwise", clockwise)
cv2.imshow("Counter Clockwise", counter)
cv2.waitKey(0)
cv2.destroyAllWindows()