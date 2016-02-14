# USAGE
# python stitch.py --first images/bryce_left_01.png --second images/bryce_right_01.png 

# import the necessary packages
from pyimagesearch.panorama import Stitcher
import argparse
import imutils
import cv2

'''
NOTES:
	
	
'''
def main():
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-f", "--first", required=True,
		help="path to the first image")
	ap.add_argument("-s", "--second", required=True,
		help="path to the second image")
	args = vars(ap.parse_args())
	stitch_images(args["first"], args["second"])

def stitch_images(name1, name2):
	''' Stitches 2 images together
	
	Args:
	name1: Name of first image
	name2: Name of second image
	
	Returns: 
	None
	
	'''
	# load the two images and resize them to have a width of 400 pixels
	# (for faster processing)
	imageA = cv2.imread(name1)
	imageB = cv2.imread(name2)
	imageA = imutils.resize(imageA, width=400)
	imageB = imutils.resize(imageB, width=400)
	
	# stitch the images together to create a panorama
	stitcher = Stitcher()
	(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
	
	# save the image
	cv2.imwrite('result.jpg', result)
	
	# show the images
	cv2.imshow("Image A", imageA)
	cv2.imshow("Image B", imageB)
	cv2.imshow("Keypoint Matches", vis)
	cv2.imshow("Result", result)
	cv2.waitKey(0)

if __name__ == "__main__":
	main()
