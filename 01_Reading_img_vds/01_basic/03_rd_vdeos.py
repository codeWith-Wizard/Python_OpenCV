import cv2 as cv  # Import the OpenCV library

# Initialize the video capture object with a video file path
# Use an integer (0, 1, 2, ...) for webcam or desktop camera
# Provide a file path for a video file
capture = cv.VideoCapture(r"01_Reading_img_vds\Videos\forest-river-moewalls-com.mp4")

# Loop to continuously capture and display video frames
while True:
    # Read a frame from the video file
    # Returns two values: isTrue (if frame was successfully read) and frame (the actual frame data)
    isTrue, frame = capture.read()
    
    # Display the current frame in a window named "video"
    cv.imshow("video", frame)
    
    # Check if the 'd' key was pressed (0xFF ensures compatibility with different systems)
    if cv.waitKey(20) & 0xFF == ord('d'):
        # Break the loop if 'd' key is pressed
        break

# Release the video capture object
capture.release()

# Close all OpenCV windows
cv.destroyAllWindows()

   
