import cv2
import numpy as np

#Reading in image
img = cv2.imread('lines.png')

#Initializing color gray
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Detecting edges in image using canny function
edges = cv2.Canny(gray,100,200,apertureSize = 3)

#Finding line segements using HoughLinesP
lines = cv2.HoughLinesP(edges, 1, np.pi/2, 6, None, 50, 10);

#Drawing detected lines
for line in lines[0]:
    pt1 = (line[0],line[1])
    pt2 = (line[2],line[3])
    cv2.line(img, pt1, pt2, (0,0,255), 2)

#Displaying results
cv2.imshow('im',img)
cv2.waitKey()