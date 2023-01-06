'''
File responsible for webcam feed
'''

import cv2

# accessing webcam feed with opencv library
# cv.VideoCapture allows us to read webcam video as seperate image frames
class Webcam:
    def __init__(self):
        self.webcam = cv2.VideoCapture(0)     # 0 indicates that default webcam should be used
        if not self.webcam.isOpened():
            raise ValueError("No webcam has been detected")     # use isOpened returns False, then webcam is not detected
        self.width = (cv2.CAP_PROP_FRAME_WIDTH)     # get height and width
        self.height = (cv2.CAP_PROP_FRAME_HEIGHT)


    def individual_frames(self):
        pass
