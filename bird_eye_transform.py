# importing required modules
import cv2
import numpy as np
import math

#defining function for click event i.e marks a point on image with red
#where left mouse button is clicked

points =[] #reference points for transformation
coor = [] #reference points to calculate distance and classify

#number of clicks
Click_number = 0 
img = None


def click_event(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDOWN:
		global Click_number
		global img

		if(Click_number < 4):
			print('Perspective Click ')
			print(x, ',', y) #prints out the point for reference
			points.append([x,y])
			center = (x, y) #center of the dot i.e the point itself
			radius = 1 #radius of the dot

			cv2.circle(img, center, radius,(0,0,255), 5) #draws the dot on the image
			cv2.imshow('image', img)
		
		else:
			print('Click for disance reference points')
			print(x, ',', y) #prints out the point for reference
			coor.append([x,y])
			center = (x, y) #center of the dot i.e the point itself
			radius = 1 #radius of the dot
			cv2.circle(img, center, radius,(255,0,0), 5) #draws the dot on the image
			cv2.imshow('image', img)
		Click_number+=1


def computeParams(img):
	pts1 = np.float32(points)
	transformed_points = [[0,0], [300,0], [0,300], [300,300]]
	pts2 = np.float32(transformed_points)
	transformation_matrix = cv2.getPerspectiveTransform(pts1, pts2)
	transformed = cv2.warpPerspective(img, transformation_matrix, (300,300))
	distV = np.float32(coor)
	result = transform(coor, transformation_matrix)
	print(result)

	one = result[0]
	two = result[1]

	distance = math.sqrt( (one[0] - two[0])**2 + (one[1] - two[1])**2 )#diff = one  - two
	print('Distance Limit in pixels ')
	print(distance)
	return [transformation_matrix, transformed, distance, points]


def transform(points, M):
	points = np.float32(points)
	result = cv2.perspectiveTransform(points[None, :, :], M)
	print(result.shape)
	ret = []
	
	for i in range(0,result.shape[1]):
		ret.append(result[0][i])
	return ret


def calibrate(vid):
	cap = cv2.VideoCapture(vid)
	if(cap.isOpened()):
		ret, frame = cap.read()
	else:
		print('No Frame')
	cap.release()
	global img
	img = frame
	cv2.imshow('image',img)
	cv2.setMouseCallback('image',click_event)
	cv2.waitKey(0)
	ret = computeParams(img)
	cv2.destroyAllWindows()
	return ret


if __name__ == "__main__":
	ret = calibrate('test.avi')