## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from ap_projection_ratios import *
from ap_settings import *
from ui_ready import *

class ProjectionSet(Frame):
	def __init__(self, parent, padx, post_info, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		## build & configure options
		self.settings = APSettings()
		self.post_info = post_info
		self.ui_ready = UIReady()

		self.columnconfigure(0, minsize = 260)
		self.columnconfigure(1, minsize = 260)
		self.options = [] ## empty list
		self.build_options() ## add items
		self.selection = StringVar() ## instantiate associated variable
		self.selection.trace_add("write", self.set_projection) ## same as binding a callback
		## instantiate menu & set default (arg #3)
		self.label = Label(self, text = "Projection Size")
		self.option_menu = OptionMenu(self, self.selection, self.options[2], *self.options)
		self.label.grid(column = 0, row = 0, sticky = E, padx = padx)
		self.option_menu.grid(column = 1, row = 0, sticky = W, padx = padx)
		
	def build_options(self):
		for ratio, properties in projection_ratios.items():
			option = ratio
			self.options.append(option)
		
	def set_projection(self, *args):
		if self.ui_ready.ui_ready == False:
			ic(self.ui_ready.ui_ready)
			return
			
		self.settings.projection = self.selection.get()
		self.post_info()

## testing
def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.settings = APSettings()
		projection_set = ProjectionSet(self, 10, self.post_info_dummy)
		projection_set.pack(ipadx = 20, ipady = 10)

	def post_info_dummy(self):
		print("filling info")
		
if __name__ == "__main__":
	main()
