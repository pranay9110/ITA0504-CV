import cv2

img = cv2.imread("image2.png")

edge = cv2.Canny(img, 100, 200)

cv2.imwrite("Experiment3 output.png", edge)

cv2.imshow("Canny", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()