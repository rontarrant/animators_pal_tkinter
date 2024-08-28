from tkinter import *
from tkinter.ttk import *

## locals
from ap_screen_resolutions import *
from ap_settings import *
from observer import Observable

class ResolutionSet(Frame, Observable):
	def __init__(self, parent, padx, *args, **kwargs):
		super().__init__(parent, **kwargs)
		self.ap_settings = APSettings()
		self.ap_settings.attach(self)
		self.columnconfigure(0, minsize = 260)
		self.columnconfigure(1, minsize = 260)

		## build and configure options for OptionMenu
		self.options: list = []
		self.ghost_options = {}
		self.build_options()
		self.selection = StringVar()

		## populate
		self.label = Label(self, text = "Resolution (Size)")
		## default: arg #3
		self.option_menu = OptionMenu(self, self.selection, self.options[2], *self.options)
		
		self.label.grid(column = 0, row = 1, sticky = E, padx = padx)
		self.option_menu.grid(column = 1, row = 1, sticky = W, padx = padx)
		self.selection.set(self.ap_settings.resolution)

		## attach callback
		self.selection.trace('w', self.update)

	def build_options(self):
		for ratio, properties in screen_resolutions.items():
			option = ratio
			self.options.append(option)
			## we need a way to find the short version (ie. "8k") in screen_resolutions.
			## Therefore, we build a dictionary using the long form as a key
			## and short form as value and then use the short form as a key in screen_resolutions.
			self.ghost_options[option] = ratio
			#self.ghost_options.append(ghost_option)
			## ic("option: ", option)
			## ic("ghost_option: ", self.ghost_options)

	def update(self, *args):
		self.ap_settings.resolution = self.selection.get()

## testing
def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ap_settings = APSettings()
		resolution_set = ResolutionSet(self, 10, self.post_info_dummy)
		resolution_set.pack(ipadx = 20, ipady = 10)

	def post_info_dummy(self):
		print("filling info")
		
if __name__ == "__main__":
	main()
