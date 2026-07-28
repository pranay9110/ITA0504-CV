import cv2

img = cv2.imread("image.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("Experiment1 output.png", gray)

cv2.imshow("Gray Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()