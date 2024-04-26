## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from ap_projection_ratios import *

class ProjectionSet(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		## build & configure options
		self.options = [] ## empty list
		self.build_options() ## add items
		self.selection = StringVar(parent) ## instantiate associated variable
		self.selection.trace('w', self.show) ## same as binding a callback
		## instantiate menu & set default (arg #3)
		self.option_menu = OptionMenu(parent, self.selection, self.options[2], *self.options)
		
		self.label = Label(parent, text = "Projection Size")
		
	def build_options(self):
		for ratio, properties in projection_ratios.items():
			option = ratio + " (" + properties["ratio"] + ")"
			self.options.append(option)
		
	def show(self, *args):
		print(self.selection.get())
		
	def get(self):
		return self.selection.get()
		
	def set(self, value):
		pass

