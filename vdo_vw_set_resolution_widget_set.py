## ResolutionWidgetSet

## tkinter
'''
TODO
- set size of widget set
'''
from tkinter import *
from tkinter.ttk import *

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class ResolutionWidgetSet(Frame):
	def __init__(self, parent, getter, setter, *args, **kwargs):
		super().__init__(parent, **kwargs)
		## population
		label = Label(text = "Resolution")
		options = ["8k", "6k", "5k", "4k", "3k", "2k", "1080p", "720p"]
		self.selection = StringVar(self)
		print(self.selection.get())
		option_menu = OptionMenu(self, self.selection, *options)
		
		## settings
		self.config(width = 200)
		self.pack_propagate()
		label.pack(side = LEFT, anchor = "e", padx = 5)
		option_menu.pack(side = LEFT, anchor = "w", padx = 5)
		self.selection.trace('w', self.show)
		self.selection.set(options[6])
		
	def show(self, *args):
		print(self.selection.get())

## testing
if __name__ == "__main__":
	class Window(Tk):
		def __init__(self, *args, **kwargs):
			self.var = "1080p"
			super().__init__(*args, **kwargs)
			widget_set = ResolutionWidgetSet(self, self, self.getter, self.setter)
			widget_set.pack()

		def getter(self):
			return self.var
		
		def setter(self, value):
			self.var = value

	def main():
		window = Window()
		window.mainloop()

	main()

