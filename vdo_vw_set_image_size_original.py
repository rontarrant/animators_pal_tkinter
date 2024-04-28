## tkinter
from tkinter import *
from tkinter.ttk import *

class ImageSizeSet(Frame):
	width  = 0
	height = 0
	
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.label = Label(parent, text = "Original Image Size")
		self.value_label = Label(parent, text = "1920 x 1080")
		
	def update(self, width, height):
		self.text(str(width) + " x " + str(height))
