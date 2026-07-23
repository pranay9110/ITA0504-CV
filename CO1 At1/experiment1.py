import cv2

img = cv2.imread("image.png")   # Change to your actual file name

if img is None:
    print("Image not found!")
else:
    cv2.imshow("Original Image", img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)

    cv2.imwrite("gray_image.png", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()