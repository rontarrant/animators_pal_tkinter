from tkinter import *
from tkinter.ttk import *
from tkinter import font

class BannerLabel(Label):
	def __init__(self, parent):
		super().__init__(parent)
		self.text = "Video & Image Info"
		self.display_font = font.Font(family = "System", size = 14, weight = "bold")
		self.config(text = self.text, font = self.display_font)
		
