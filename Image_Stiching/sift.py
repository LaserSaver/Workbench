import cv2
import numpy as np
   
img = cv2.imread('games.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  
sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)
   
# This is the zeroed out mnumpy image
drawing = np.zeros(img.shape,np.uint8)

# This creates the uniq points 
#  with circles on the original image
output=cv2.drawKeypoints(gray,kp,drawing)
   
cv2.imwrite('sift_keypoints.jpg',output)

# Show the output image
cv2.imshow("Output", output)

cv2.waitKey(0)