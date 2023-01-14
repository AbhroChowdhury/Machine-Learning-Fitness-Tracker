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

class GUI:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title = "Machine Learning Fitness Tracker"
        self.counters = [1, 1]
        self.movement_counter = 0
        self.lengthened = False
        self.contracted = False
        self.previous = 0
        self.enablemodel = False
        self.camera = webcam.Webcam()
        self.initialize_gui()
        self.delay = 15
        self.update()
        self.window.attributes("-topmost", True)

    def initialize_gui(self):
        self.canvas = ctk.CTkCanvas(self.window, width=self.webcam.width, height=self.webcam.height)
        self.canvas.pack()
        self.btn_toggle_counter = ctk.CTkButton(self.window, text='Toggle Counting', command='self.toggle_counting')
        self.btn_toggle_counter.pack(anchor=tk.CENTER, expand=True)

        self.model = None

        self.btn_class_one = ctk.CTkButton(self.window, text='Extended', width=50, command=lambda: self.save_for_class(1))
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)

        self.btn_class_one = ctk.CTkButton(self.window, text='Contracted',width=50, command=lambda: self.save_for_class(2))
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)

        self.btn_train = ctk.CTkButton(self.window, text='Train Model',width=50, command=lambda: self.model.train_model(self.counters))
        self.btn_train.pack(anchor=tk.CENTER, expand=True)

        self.btn_reset = ctk.CTkButton(self.window, text='Reset',width=50, command=self.reset)
        self.btn_reset.pack(anchor=tk.CENTER, expand=True)

        self.main_label = ctk.CTkLabel(self.window, text=f"{self.rep_counter}")
        self.main_label.config(font=('Arial', 24))
        self.main_label.pack(anchor=tk.CENTER, expand=True)

    def update(self):
        pass

    def toggle_counting(self):
        

    def save_for_class(self, class_num):
        pass

    def reset(self):
        pass



