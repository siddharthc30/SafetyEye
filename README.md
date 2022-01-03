# SafetyEye

A computer vision based object detection application that helps to monitor and detect social distancing in public places.


## Summary of Contents

<details open="open">
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#problem-addressed">Problem Addressed</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#run-it">Run it</a></li>
      </ul>
    </li>
    <li><a href="#example">Example</a></li>
    <li><a href="#new">New!</a></li>
    <li><a href="#coming-up">Coming up</a></li>
    
  </ol>
</details>

## About The Project

### Built With
1. Python3
2. Opencv
3. cv2's DNN module

## Problem Addressed


## Getting Started
### Prerequisites
To install the required prerequisite modules, just run
``` pip install requirements.txt```
<br>
Next, download the weights of yolov3 network from [here](href="https://pjreddie.com/media/files/yolov3.weights) and copy-paste the file into this cloned directory


### Run it
After all the required files and modules are downloaded. Run the command 
<br>
```python3 app.py```
<br>
- Then a pop-up with the first frame of the test video appears.
- Here, you have to select four dots on the frame such that when a pair of two dots is connected to from a line, then atleast two lines have to be parallel, i.e when four points are connected, they have to be a trapezium or a parallelogram or atleast a rectangle.
- Later, you have to select two dots along a straight line (preferable), to find out the minimum distance to be maintained by the people in the video. 

All these steps are demonstrated below in Example section

## Example

## New!
This application has an inbuilt camera caliberation function, using which we can set the minimum distance between people in the video to classify them whether they are socially distanced or not. This application also has a perspective tranformation of the people so that the distance between people will be independent of the orientation of camera.

## Coming up
### Automate the process of camera calibration.
Instead of the user entering the minimum distance required to be maintained, the future goal of this application is to automate this process and smartly find out the minimum distance using an algorithm, which would inturn reduce the effort of user entering the points to calculate the distance.


