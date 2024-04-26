## tkinter
from tkinter import *
from tkinter.ttk import *

## local

class PillarDisplacementSet(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.label = Label(parent, text = "Pillar Displacement")
		self.value_label = Label(parent, text = "0")
		self.width = IntVar()
	
	def get(self):
		return self.width.get()
		
	def set(self, value):
		self.width.set(value)
