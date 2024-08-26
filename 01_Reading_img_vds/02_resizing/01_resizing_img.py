import cv2 as cv 

img = cv.imread(r"01_Reading_img_vds\Images\08_4k.jpg")

cv.imshow("resized image of night sky", img)

def reScaleFrame(frame , scale = 0.75):
    width = int(frame.shape[1] * scale)
    
    
cv.waitKey(0)