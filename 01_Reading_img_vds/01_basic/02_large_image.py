import cv2 as cv  # Import the OpenCV library

# Read the image from the specified file path
# The path should be updated to where your image is stored
img = cv.imread(r"01_Reading_img_vds\Images\08_4k.jpg")

# Display the image in a window named "night sky"
# Note: If the image dimensions are larger than the screen, only a portion may be visible
cv.imshow("night sky", img)

# Wait indefinitely for a key press
# This keeps the window open until any key is pressed
cv.waitKey(0)

# Note: The window will close automatically when any key is pressed
