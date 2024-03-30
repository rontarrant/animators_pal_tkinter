from tkinter import *
from tkinter.ttk import *

class DirectionRadioSet(Labelframe):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		## instance
		self.config(text = "direction")
		self.var = IntVar() ## used in preferences
		## child widgets
		radio1 = Radiobutton(self, text = "Forward", variable = self.var, value = 1)
		radio2 = Radiobutton(self, text = "Reverse", variable = self.var, value = -1)
		## create grid
		self.columnconfigure(0, weight = 1)
		self.rowconfigure(0, weight = 1)
		self.rowconfigure(1, weight = 1)
		## layout
		radio1.grid(row = 0, column = 0, sticky = "w", padx = 10)
		radio2.grid(row = 1, column = 0, sticky = "w", padx = 10)
		## configure children
		radio1.config(command = self.select)
		radio2.config(command = self.select)
		self.var.set(1)
	
	def select(self):
		# ic(self.var.get())
		pass

## testing
def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		direction_radio_set = DirectionRadioSet(self)
		direction_radio_set.pack(ipadx = 20, ipady = 10)

if __name__ == "__main__":
	main()
