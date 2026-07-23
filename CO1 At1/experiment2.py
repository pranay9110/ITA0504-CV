import cv2

# Read the image
img = cv2.imread("image2.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Blurred Image", blur)

    # Save blurred image
    cv2.imwrite("blur_image2.png", blur)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()