'''
File responsible for training the models 
'''

import numpy as np
from sklearn.svm import LinearSVC
import cv2
import PIL

class Model:
    def __init__(self):
        self.model = LinearSVC()

    def train_model(self, counters):
        img_list = np.array([])
        class_list = np.array([])
        for i in range(1, counters[0]):
            img = cv2.imread(f"1/frame{i}.jpg")[:,:,0]
            img = img.reshape(16950)
            img_list = np.append(img_list, [img])
            class_list = np.append(class_list, 1)