'''
This file is responsible for the graphical user interface. This will be done with TKinter
'''

import tkinter as tk
import customtkinter as ctk
import cv2
import numpy as np
import os 
import PIL.Image, PIL.ImageTk
import webcam
import trainingmodel

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title = "Machine Learning Fitness Tracker"
        self.counters = [1, 1]
        self.movement_counter = 0
        self.lengthened = False
        self.contracted = False
        self.previous = 0
        self.enablemodel = False
        self.camera = webcam.Webcam()

        self.delay = 15
        self.window.attributes("-topmost", True)
        self.initialize_gui()
        self.update()

    def initialize_gui(self):
        self.canvas = tk.TkCanvas(self.window, width=self.webcam.width, height=self.webcam.height)
        self.canvas.pack()
        self.btn_toggle_counter = tk.TkButton(self.window, text='Toggle Counting', command='self.toggle_counting')
        self.btn_toggle_counter.pack(anchor=tk.CENTER, expand=True)

        self.model = trainingmodel.Model()

        self.btn_class_one = tk.TkButton(self.window, text='Extended', width=50, command=lambda: self.save_for_class(1))
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_one = tk.TkButton(self.window, text='Contracted',width=50, command=lambda: self.save_for_class(2))
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)

        self.btn_train = tk.TkButton(self.window, text='Train Model',width=50, command=lambda: self.model.train_model(self.counters))
        self.btn_train.pack(anchor=tk.CENTER, expand=True)

        self.btn_reset = tk.TkButton(self.window, text='Reset',width=50, command=self.reset)
        self.btn_reset.pack(anchor=tk.CENTER, expand=True)

        self.main_label = tk.TkLabel(self.window, text=f"{self.rep_counter}")
        self.main_label.config(font=('Arial', 24))
        self.main_label.pack(anchor=tk.CENTER, expand=True)

    def update(self):
        if self.enable_model:
            self.predict()
        if self.lengthened and self.contracted:
            self.lengthened, self.contracted = False, False
            self.rep_counter += 1
        self.main_label.config(text=f'{self.rep_counter}')
        ret, frame = self.webcam.individual_frames()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame), anchor=tk.NW)
            self.convas.create_image(0, 0, image=self.photo)

        self.window.after(self.delay, self.update)

    def predict(self):
        frame = self.webcam.get_frame()
        prediction = self.model.predict(frame)
        if prediction != self.previous:
            if prediction == 1:
                self.lengthened = True
                self.previous = 1
            if prediction == 2:
                self.contracted = True
                self.previous = 2

    def toggle_counting(self):
        self.enable_model = not self.enable_model

    def save_for_class(self, class_num):
        ret, frame = self.webcam.individual_frames()
        if not os.path.exists('1'):
            os.mkdir('1')
        if not os.path.exists('2'):
            os.mkdir('2')
        
        cv2.imwrite(f"{class_num}/frame{self.counters[class_num-1]}.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
        img = PIL.Image.open(f"{class_num}/frame{self.counters[class_num-1]}.jpg")
        img.thumbnail((150,150), PIL.Image.ANTIALIAS)
        img.save(f"{class_num}/frame{self.counters[class_num-1]}.jpg")
        self.counters[class_num-1] += 1

    def reset(self):
        self.movement_counter = 0

    def rep_counter(self):
        pass



