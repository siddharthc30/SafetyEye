#importing the required modules
import cv2
import numpy as np
import time
import argparse
from computeDistance import ComputeDistance
from bird_eye_transform import calibrate, transform


# CLI support
parser = argparse.ArgumentParser()
parser.add_argument('--path', help = 'Enter the path of Video', required = True)
args = parser.parse_args()
path = args.path


#Caliberating and defining the threshold distance
[Transformation_matrix, transformed_points, threshold_distance, points] = calibrate(path)


#defining the pretrained yolo model along with weights
net = cv2.dnn.readNet("/home/siddharthc30/yolov3.weights", "yolov3.cfg") # reading a deep learning network from the given config files
classes = []
layer_names =[] # all the layer names of the yolo network

with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()] #stores all the unconnected output layers


#load input video stream
cap = cv2.VideoCapture(path) 
 

#initialize the writer for writing the output video to a file
writer = None
(W, H) = (None, None) #height and width of the frames of video


while True:
    ret , frame= cap.read()
    if W is None or H is None:
        (H, W) = frame.shape[:2]

    # Detecting objects
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False) #stroing a blob of preprocessed frames
    net.setInput(blob) #sets the input to the network as blob


    #run forward pass of the network to compute the outputs of the layers listed in output_layers
    outs = net.forward(output_layers) #returns an ndarray(bx, by, bh, bw, pc, c)
    
    # initialize our lists of detected bounding boxes, confidences, and class IDs, respectively
    boxes = []
    confidences = []
    class_ids = []

    # loop over each of the layer outputs
    for out in outs:
        # loop over each of the detections
        for detection in out:
            # extract the class ID and confidence 
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # filter out weak predictions
            if confidence > 0.7:
                center_x = int(detection[0] * W)
                center_y = int(detection[1] * H)

                #width and height
                w = int(detection[2] * W)
                h = int(detection[3] * H)

                # Rectangle coordinates top left
                x = int(center_x - (w / 2))
                y = int(center_y - (h / 2))
  
                # update our list of bounding box coordinates, confidences, and class IDs
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)


    # apply non-maxima suppression to suppress weak, overlapping bounding boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.2) # saves the array of indices of best boxes in the frame


    #detecting persons and saving the midpoint of ground co-ordinates into an array
    projected = [] # 2-d array that stores coordinates of the projected point on ground and the 


    if len(indexes) > 0:
        # loop over the indexes we are keeping
        for i in indexes.flatten():
            # extract the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            label = str(classes[class_ids[i]])

            if label == 'person':
                #p=p+1
                projected.append([[x + w//2, y + h], boxes[i]])
                classify = ComputeDistance(projected, Transformation_matrix, threshold_distance)
                
                for bx in classify:
                    box = bx[0][1]
                    (x, y) = (box[0], box[1])
                    (w, h) = (box[2], box[3])

                    #If True then Red boxes
                    if(bx[1] == True):
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,255), 2)
                    else:
                        #Green boxes
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)
                
            else:
                continue

        
        if writer is None:
            # initialize our video writer
            fourcc = cv2.VideoWriter_fourcc(*"MJPG")
            writer = cv2.VideoWriter("out.avi", fourcc, 30,(frame.shape[1], frame.shape[0]))

    cv2.imshow("Frame", frame)
    writer.write(frame)
    if cv2.waitKey(1) == 27:
        cap.release()
        writer.release()
        break


cv2.destroyAllWindows()