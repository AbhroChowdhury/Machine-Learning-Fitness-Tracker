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

        self.btn_class_one = ctk.CTkButton(self.window, text='Toggle Counting', command='self.toggle_counting')
        self.btn_toggle_counter.pack(anchor=tk.CENTER, expand=True)

    def update(self):
        pass

    def toggle_counting(self):
        pass


