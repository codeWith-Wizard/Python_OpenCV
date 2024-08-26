import cv2 as cv  # Import the OpenCV library

# Read the image from the specified file path
# The path should be updated to the location of your image
img = cv.imread(r'01_Reading_img_vds\Images\01.jpg')

# Display the image in a window named "porsche"
# The window will show the image data
cv.imshow('porsche', img)

# Wait indefinitely for a key press
# The window will remain open until any key is pressed
cv.waitKey(0)

# After a key is pressed, the program will end and the window will close
