'''
File responsible for webcam feed
'''

import cv2 as cv

# accessing webcam feed with opencv library
# cv.VideoCapture allows us to read webcam video as seperate image frames
class Webcam:
    def __init__(self):
        self.webcam = cv.VideoCapture(0) # 0  indicates that default camera should be used
        
