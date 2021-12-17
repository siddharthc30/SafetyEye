import cv2
import numpy as np
import math
import itertools

def ComputeDistance(points, M, distance):
	act = []
	all = []
	for point in points:
		all.append([point, False])
		act.append(point[0])
	
	
	act = np.float32(act)
	result = cv2.perspectiveTransform(act[None, :, :], M)
	transformed = []
	for i in range(0,result.shape[1]):
		transformed.append(result[0][i])
	pairs = list(itertools.combinations(range(len(transformed)), 2))
	for i,vec in enumerate(itertools.combinations(transformed, r=2)):
		if math.sqrt( (vec[0][0] - vec[1][0])**2 + (vec[0][1] - vec[1][1])**2 ) < distance:
			first = pairs[i][0]
			second = pairs[i][1]
			all[first][1] = True
			all[second][1] = True
	
	return all