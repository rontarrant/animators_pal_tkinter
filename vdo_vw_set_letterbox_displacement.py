## tkinter
from tkinter import *
from tkinter.ttk import *

## local

class LetterboxDisplacementSet(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		
		self.label = Label(parent, text = "Letterbox Displacement")
		self.value_label = Label(parent, text = "0")
		self.height = IntVar()

	def get(self):
		return self.height.get()
		
	def set(self, value):
		self.height.set(value)


