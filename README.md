# SafetyEye

A computer vision based object detection command line application that helps to monitor and detect social distancing in public places.


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
    <li><a href="#results">Results</a></li>
    <li><a href="#new">New!</a></li>
    <li><a href="#coming-up">Coming up</a></li>
    
  </ol>
</details>

## About The Project
During the pandemic, there were guidelines passed by local government bodies that were to be followed on a personal basis in order to reduce the rise in COVID-19 cases, one of them was following social distancing in public places. Following social distancing is a difficult task for us, as it is something new to us and we have to be constantly monitored so that we follow this rule and reduce the risk of contracting the virus. If there were people appointed to monitor social distancing from the field, this job becomes not only tedious but also would put the respective person at risk of contracting the virus. In order to overcome this problem, we can automate this task and SafetyEye comes right into action. SafetyEye is a command-line application that detects and monitors social distancing using a state-of-the-art object detection model that is tuned to recognize human beings. When CCTV footage of a public place is fed to the application, it outputs a video with a graphical representation of people following social distancing or not. This helps in a way that a person can sit inside a cabin remotely and take a look into the situation for any further action. 


### Built With
1. Python3
2. Opencv
3. cv2's DNN Library

## Problem Addressed
Automation of social distance detection and monitoring.

## Getting Started
### Prerequisites
To install the required prerequisite modules, just run
``` pip install -r requirements.txt```
<br>
Next, download the weights of yolov3 network from [here](href="https://pjreddie.com/media/files/yolov3.weights) and copy-paste the file into this cloned directory


### Run it
After all the required files and modules are downloaded. Run the command 
<br>
```python3 app.py --path (path of the test video in double quotes)```
<br>
<br>
For example, ```python3 app.py --path "home/videos/testvideo.avi" ```
<br>
- Then a pop-up with the first frame of the test video appears.
- Here, you have to select four dots on the frame such that they form a rectangle.
- **Order of plotting points is important, and the order is, top-left, top-right, bottom-left and bottom-right**
- Later, you have to select two dots along a straight line (preferable), to find out the minimum distance to be maintained by the people in the video. 

All these steps are demonstrated below in Example section

## Example
Here is a demo on how to run the application,

## Results
This is the output of the application after running it on the sample video that is already in this repository.
<br>
![output](https://user-images.githubusercontent.com/53928899/148102127-7563d0c8-64ef-4c2f-817f-122cc6c3049d.gif)
<br>
<br>
Here, people bounded by green boxes are maintaining social distancing according to the threshold distance given by the user and the ones bounded by red boxes are not.
<br>
P.S: The complete output video is in file out.avi

## New!
This application has an inbuilt camera caliberation function, using which we can set the minimum distance between people in the video to classify them whether they are socially distanced or not. This application also has a perspective tranformation of the people so that the distance between people will be independent of the orientation of camera.

## Coming up
### Automate the process of camera calibration.
Instead of the user entering the minimum distance required to be maintained, the future goal of this application is to automate this process and smartly find out the minimum distance using an algorithm, which would inturn reduce the effort of user entering the points to calculate the distance.


