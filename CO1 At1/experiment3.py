import cv2

# Read the image
img = cv2.imread("image3.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Edge Detection", edges)

    # Save edge image
    cv2.imwrite("edge_image3.png", edges)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()