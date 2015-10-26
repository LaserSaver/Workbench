import cv2

# Read a grayscale image
image = 'test.jpg'
im_gray = cv2.imread(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)

# convert grayscale image to binary (black or white)
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

thresh = 50
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]

# save to disk
cv2.imwrite('bw_'+image, im_bw)
