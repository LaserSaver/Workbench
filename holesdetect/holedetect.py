import cv2
import numpy as np

#Reading in image
im = cv2.imread('holes.jpg')

#Initializing color gray
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#Creating a threshhold image with the gray color cut out
#returns two outputs, the 2nd one is the new image
gray=cv2.threshold(gray,20,255,cv2.THRESH_BINARY)[1]

#Displays the threshhold image
cv2.imshow('gray',gray)

#Find contours in the image with the gray removed
contours,hierarchy = cv2.findContours(gray,cv2.RETR_LIST ,cv2.CHAIN_APPROX_SIMPLE   )

#Draws the contours in the original image to show detection
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area<400:
        cv2.drawContours(im,[cnt],0,(255,0,0),2)

#Displays the modified original image with the contours colored
cv2.imshow('im',im)
cv2.waitKey()
