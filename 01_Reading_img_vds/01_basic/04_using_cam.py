import cv2 as cv  # Import the OpenCV library

# Initialize the video capture object with the inbuilt camera (0 is the default camera)
capture = cv.VideoCapture(0)

# Loop to continuously capture and display video frames
while True:
    # Read a frame from the camera
    istrue, frame = capture.read()
    
    # Display the current frame in a window named "camera"
    cv.imshow("camera", frame)
    
    # Check if the 'd' key was pressed (0xFF ensures compatibility with different systems)
    if cv.waitKey(20) & 0xFF == ord("d"):
        # Break the loop if 'd' key is pressed
        break

# Release the video capture object
capture.release()

# Close all OpenCV windows
cv.destroyAllWindows()
