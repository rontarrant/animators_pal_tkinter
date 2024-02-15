from tkinter import *
from tkinter.ttk import *

class FPSRadioSet(Labelframe):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		## attributes
		self.config(text = "fps")
		self.var = IntVar() ## used in preferences
		## child widgets
		radio1 = Radiobutton(self, text = "18 fps", variable = self.var, value = 18)
		radio2 = Radiobutton(self, text = "24 fps", variable = self.var, value = 24)
		radio3 = Radiobutton(self, text = "30 fps", variable = self.var, value = 30)
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
		radio1.config(command = lambda: self.select(parent))
		radio2.config(command = lambda: self.select(parent))
		radio3.config(command = lambda: self.select(parent))
		## default
		self.var.set(24)
	
	def select(self, parent):
		print("fps: ", self.var.get())

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		fps_radio_set = FPSRadioSet(self)
		fps_radio_set.pack(ipadx = 20, ipady = 10)

if __name__ == "__main__":
	main()