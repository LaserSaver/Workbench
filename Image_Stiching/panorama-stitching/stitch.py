# USAGE
# python stitch.py --first images/bryce_left_01.png --second images/bryce_right_01.png 

# import the necessary packages
from pyimagesearch.panorama import Stitcher
import argparse
import imutils
import cv2

'''
NOTES:
	- You may pass it 2 or 4 images to stitch together
	
'''
def main():
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-1", "--first", required=True,
		help="path to the first image")
	ap.add_argument("-2", "--second", required=True,
		help="path to the second image")
	ap.add_argument("-3", "--third", required=False,
		help="path to the third image")
	ap.add_argument("-4", "--fourth", required=False,
		help="path to the fourth image")
	args = vars(ap.parse_args())
	
	imageA = cv2.imread(args["first"])
	imageB = cv2.imread(args["second"])
	
	
	result1 = stitch_images(imageA, imageB)
	#rotate resulting images
	rows,cols,_ = result1.shape
	M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
	result1 = cv2.warpAffine(result1,M,(cols,rows))
	
	if (args["third"] != None and args["fourth"] != None):
		imageC = cv2.imread(args["third"])
		imageD = cv2.imread(args["fourth"])
		result2 = stitch_images(imageC, imageD)
		
		
		
		result = stitch_images(result1, result2)
		
		#rotate back
		
		# save the image
		cv2.imwrite('result.jpg', result)
	else:
		# save the image
		cv2.imwrite('result1.jpg', result1)

def stitch_images(imageA, imageB):
	''' Stitches 2 images together
	
	Args:
	imageA: First image
	imageB: Second image
	
	Returns: 
	result: the images stitched together
	
	'''
	# load the two images and resize them to have a width of 400 pixels
	# (for faster processing)
	imageA = imutils.resize(imageA, width=400, height=400)
	imageB = imutils.resize(imageB, width=400, height=400)
	
	# stitch the images together to create a panorama
	stitcher = Stitcher()
	(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
	
	
	
	# show the images (commented out for using pi through ssh)
	#cv2.imshow("Image A", imageA)
	#cv2.imshow("Image B", imageB)
	#cv2.imshow("Keypoint Matches", vis)
	#cv2.imshow("Result", result)
	#cv2.waitKey(0)
	
	return result

if __name__ == "__main__":
	main()
