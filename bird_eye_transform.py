# importing required modules
import cv2
import numpy as np

#defining function for click event i.e marks a point on image with red
#where left mouse button is clicked
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y) #prints out the point for reference
        center = (x, y) #center of the dot i.e the point itself
        radius = 1 #radius of the dot
        cv2.circle(img, center, radius,(0,0,255), 5) #draws the dot on the image
        cv2.imshow('image', img)


if __name__ == "__main__":
    img = cv2.imread('bubblingFish.jpg')
    cv2.imshow('image',img)
    cv2.setMouseCallback('image',click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()