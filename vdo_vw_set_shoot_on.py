from tkinter import *
from tkinter.ttk import *

## local
from ap_settings import *

class ShootOnSet(Labelframe):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		## attributes
		self.settings = APSettings.get_instance()
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
		self.var.set(self.settings.shoot_on)
		
	def reset(self):
		#print("reset")
		self.spinbox.set(1)
		self.label.config(text = "1's")
		self.var.set(1)
		## ic(str(self.spinbox.get()))
	
class NumericSpinbox(Spinbox):
	def __init__(self, parent, var):
		super().__init__(parent)
		# object attributes
		self.parent = parent
		self.settings = APSettings()
		# configure
		self.config(from_ = 1, to = 9, increment = 1) # range and step
		self.config(textvariable = var)
		self.set(1)
		self.config(command = lambda: self.action(parent.label))
		self.config(state = "readonly")

	def action(self, label):
		label_text = str(self.get() + "'s")
		label.config(text = label_text)
		self.settings.shoot_on = self.parent.var.get()
		## ic(self.get())

## testing
def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		self.var = 1
		super().__init__(*args, **kwargs)
		on_shoot_set = ShootOnSet(self)
		on_shoot_set.pack(ipadx = 20, ipady = 10)

	def getter(self):
		print("self.var: ", self.var)
		return self.var
		
	def setter(self, value):
		self.var = value
		print("self.var: ", self.var)
		
if __name__ == "__main__":
	main()
