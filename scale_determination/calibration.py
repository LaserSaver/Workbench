import numpy as np
import cv2
import sys

image = sys.argv[1]
# user supplied know size of object
x = float(sys.argv[2])
y = float(sys.argv[3])

im = cv2.imread(image)

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,50,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]

# red box
# rect contains (x,y), (w,h), theta (angle of rotation)
rect = cv2.minAreaRect(cnt)
box = cv2.cv.BoxPoints(rect)
box = np.int0(box)
(w,h) = rect[1]  # dimensions in pixels

# size in pixels is proportional to real scale
# this scale times pixels can now determin scale
# as long as the camera is at a fixed height
horr_scale = x/w
vert_scale = y/h
print "horr_scale: {}".format(horr_scale)
print "vert_scale: {}".format(vert_scale)

cv2.drawContours(im,[box],0,(0,0,255),2)
print "Dimensions of red box (w,h): {}".format(rect[1])

cv2.imwrite('rec_'+image, im)
cv2.imshow('im', im)
cv2.waitKey()
