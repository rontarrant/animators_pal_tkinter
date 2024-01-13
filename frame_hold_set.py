from tkinter import *
from tkinter.ttk import *

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		first_frame_hold_set = FrameHoldSet(self, "Last Frame Hold")
		first_frame_hold_set.pack(ipadx = 20, ipady = 10)

class FrameHoldSet(Labelframe):
	def __init__(self, parent, name, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		## attributes
		self.var = IntVar()
		self.config(text = name)
		## population - checkbutton, spinbox
		self.checkbutton = Checkbutton(self, text = "check on")
		self.checkbutton.configure(variable = self.var, onvalue = 1, offvalue = 0)
		self.checkbutton.configure(command = self.action)
		
		self.spinbox = NumericSpinbox(self)
		
		self.checkbutton.pack()
		self.spinbox.pack()
	
	def action(self):
		'''
		When the checkbutton becomes checked,
		set the spinbox appropriately.
		If the spinbox is set to 1, bump it to 2.
		If it's set to 2 or higher, leave it alone.
		When the checkbutton becomes unchecked,
		always set the spinbox to 1.
		'''
		if self.var.get() == 1:
			if int(self.spinbox.get()) > 1:
				self.spinbox.set(self.spinbox.get())
			else:
				self.spinbox.set(2)
		else:
			self.spinbox.set(1)

		print(self.checkbutton.cget("text"), self.var.get())
		self.hold_for()
	
	def hold_for(self):
		print("hold frame for: ", self.spinbox.get())

class NumericSpinbox(Spinbox):
	def __init__(self, frame):
		super().__init__(frame)
		# object attributes
		# configure
		self.config(from_ = 1, to = 90, increment = 1) # range and step
		self.set(1)
		self.config(command = self.action)

	def action(self):
		print(self.get())
if __name__ == "__main__":
	main()
