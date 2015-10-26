import numpy as np
import cv2

image = 'bw_test.jpg'
im = cv2.imread(image)

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,50,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

areas = [cv2.contourArea(c) for c in contours]
max_index = np.argmax(areas)
cnt=contours[max_index]

# green box
# (x,y) is the starting coordinate of rectangle
# (w,h) is width hand height
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
print "Dimensions of green box (w,h): ({},{})".format(w,h)

# red box
# rect contains (x,y), (w,h), theta (angle of rotation)
rect = cv2.minAreaRect(cnt)
box = cv2.cv.BoxPoints(rect)
box = np.int0(box)

cv2.drawContours(im,[box],0,(0,0,255),2)
print "Dimensions of red box (w,h): {}".format(rect[1])

cv2.imwrite('rec_'+image, im)
cv2.imshow('im', im)
cv2.waitKey()
