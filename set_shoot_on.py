from tkinter import *
from tkinter.ttk import *

class ShootOnSet(Labelframe):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		## attributes
		self.var = IntVar() ## used in preferences
		## population - spinbox
		self.config(text = "shoot on...")
		self.label = Label(self, text = "1's")
		self.spinbox = NumericSpinbox(self, self.var)
		self.button = Button(self, text = "Reset")
		## config
		self.button.config(command = self.reset)
		## layout
		self.label.pack()
		self.spinbox.pack()
		self.button.pack()
		## config
		self.var.set(1)
		
	def reset(self):
		self.spinbox.set(1)
		self.label.config(text = "1's")
		## # ic(str(self.spinbox.get()))
	
class NumericSpinbox(Spinbox):
	def __init__(self, parent, var):
		super().__init__(parent)
		# object attributes
		# configure
		self.config(from_ = 1, to = 10, increment = 1) # range and step
		self.config(textvariable = var)
		self.set(1)
		self.config(command = lambda: self.action(parent.label))
		self.config(state = "readonly")

	def action(self, label):
		label_text = str(self.get() + "'s")
		label.config(text = label_text)
		## # ic(self.get())
		
def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		on_shoot_set = ShootOnSet(self)
		on_shoot_set.pack(ipadx = 20, ipady = 10)

if __name__ == "__main__":
	main()
