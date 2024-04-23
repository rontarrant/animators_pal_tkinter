from tkinter import *
from tkinter.ttk import *

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class FPSRadioSet(Labelframe):
	def __init__(self, parent, getter, setter, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		## attributes
		self.config(text = "fps")
		var = IntVar() ## used in preferences
		## child widgets
		radio1 = Radiobutton(self, text = "18 fps", variable = var, value = 18)
		radio2 = Radiobutton(self, text = "24 fps", variable = var, value = 24)
		radio3 = Radiobutton(self, text = "30 fps", variable = var, value = 30)
		## create grid
		self.columnconfigure(0, weight = 1)
		self.rowconfigure(0, weight = 1)
		self.rowconfigure(1, weight = 1)
		self.rowconfigure(2, weight = 1)
		## layout
		radio1.grid(row = 0, column = 0, sticky = "e", padx = 10)
		radio2.grid(row = 1, column = 0, sticky = "e", padx = 10)
		radio3.grid(row = 2, column = 0, sticky = "e", padx = 10)
		## configure children
		radio1.config(command = lambda: setter(var.get()))
		radio2.config(command = lambda: setter(var.get()))
		radio3.config(command = lambda: setter(var.get()))
		## default
		var.set(getter())
	
	def select(self, parent):
		# ic(self.var.get())
		pass

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		self.var = 24
		super().__init__(*args, **kwargs)
		fps_radio_set = FPSRadioSet(self, self.getter, self.setter)
		fps_radio_set.pack(ipadx = 20, ipady = 10)

	def getter(self):
		print("self.var: ", self.var)
		return self.var
		
	def setter(self, value):
		self.var = value
		print("self.var: ", self.var)

if __name__ == "__main__":
	main()
