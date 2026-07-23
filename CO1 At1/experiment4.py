import cv2

img = cv2.imread("image4.png")

small = cv2.resize(img, (200,200))
large = cv2.resize(small, (600,600))

cv2.imshow("Original", img)
cv2.imshow("Low Resolution", large)

cv2.waitKey(0)
cv2.destroyAllWindows()