from tkinter import *
from tkinter.ttk import *

## locals
from ap_screen_resolutions import *


class ResolutionSet(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		
		## build and configure options for OptionMenu
		self.options: list = []
		self.build_options()
		self.selection = StringVar()
		#self.selection.set(self.options[6])
		self.selection.trace('w', self.show)
		## instantiate OptionMenu & set default (arg #3)
		self.option_menu = OptionMenu(parent, self.selection, self.options[2], *self.options)

		self.label = Label(parent, text = "Resolution")
		## assign setter and getter

	def build_options(self):
		for ratio, properties in screen_resolutions.items():
			#ic("ratio: ", ratio, ", properties: ", properties)
			option = ratio + " (" + str(properties["width"]) + "x" + str(properties["height"]) + ")"
			self.options.append(option)

	def update(self, value):
		self.selection.set(value)
		
	def show(self, *args):
		## get projection  
		print(self.selection.get())
	
