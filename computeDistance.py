import cv2
import numpy as np
import math
import itertools

def ComputeDistance(points, M, thresh_distance):
	actual_points = []
	all_points = []
	
	for point in points:
		all_points.append([point, False])
		actual_points.append(point[0])
	
	actual_points = np.float32(actual_points)
	result = cv2.perspectiveTransform(actual_points[None, :, :], M)
	transformed = []

	for i in range(0,result.shape[1]):
		transformed.append(result[0][i])

	pairs = list(itertools.combinations(range(len(transformed)), 2)) #returns set of all possible combinations of size 2 in the array transformed

	for i,vec in enumerate(itertools.combinations(transformed, r=2)):
		if math.sqrt( (vec[0][0] - vec[1][0])**2 + (vec[0][1] - vec[1][1])**2 ) < thresh_distance:
			first = pairs[i][0]
			second = pairs[i][1]
			all_points[first][1] = True
			all_points[second][1] = True
	
	return all_points

	