import cv2 as cv

img = cv.imread('Reading_img_vds/Images/01.jpg')   #used to convert pixels from the uimage to matrix data

cv.imshow('porsche' , img)  #to open the window and show the img 

cv.waitKey(0)  #waits in milliseconds for keyboard key to be pressed
