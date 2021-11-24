# importing required modules
import cv2
import numpy as np

#defining function for click event i.e marks a point on image with red
#where left mouse button is clicked
points =[]

def click_event(event, x, y, flags, params):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y) #prints out the point for reference
        points.append([x,y])
        center = (x, y) #center of the dot i.e the point itself
        radius = 1 #radius of the dot
        cv2.circle(img, center, radius,(0,0,255), 5) #draws the dot on the image
        cv2.imshow('image', img)
        

def birds_eye_transform(img):
    pts1 = np.float32(points)
    transformed_points = [[0,0], [300,0], [0,300], [300,300]]
    pts2 = np.float32(transformed_points)
    transformation_matrix = cv2.getPerspectiveTransform(pts1, pts2)
    transformed = cv2.wrapPerspective(img, transformation_matrix, (300,300))
    cv2.imshow('birds eye view', transformed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    img = cv2.imread('hello.png')
    cv2.imshow('image',img)
    cv2.setMouseCallback('image',click_event)
    birds_eye_transform(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()