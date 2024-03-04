from tkinter import *
from tkinter.ttk import *

## local
class FrameHoldSet(Labelframe):
	def __init__(self, parent, name, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		## attributes
		self.checked_on = IntVar(value = 0) ## used in preferences
		self.spinvalue = IntVar(value = 1) ## used in preferences
		self.config(text = name)
		## population - checkbutton, spinbox
		self.checkbutton = Checkbutton(self, text = "check on")
		self.checkbutton.configure(onvalue = 1, offvalue = 0)
		self.checkbutton.configure(command = lambda: self.action(parent))
		self.checkbutton.config(state = NORMAL)
		self.checkbutton.config(variable = self.checked_on)
		
		self.spinbox = NumericSpinbox(self)
		self.spinbox.config(textvariable = self.spinvalue)
			
		self.checkbutton.pack()
		self.spinbox.pack()
		## default
	
	def action(self, parent):
		'''
		When the checkbutton becomes checked,
		set the spinbox appropriately.
		If the spinbox is set to 1, bump it to 2.
		If it's set to 2 or higher, leave it alone.
		When the checkbutton becomes unchecked,
		always set the spinbox to 1.
		'''
		if self.checked_on.get() == 1:
			if int(self.spinbox.get()) > 1:
				self.spinbox.set(self.spinbox.get())
			else:
				self.spinbox.set(1)
		else:
			self.spinbox.set(1)

		print(self.cget("text"), " state: ", self.checked_on.get())
		print("spinbox value: ", self.spinbox.get())
		
class NumericSpinbox(Spinbox):
	def __init__(self, parent):
		super().__init__(parent)
		# object attributes
		# configure
		self.config(from_ = 1, to = 90, increment = 1) # range and step
		self.set(1)
		self.config(command = lambda: self.action(parent.checked_on))

	def action(self, checked_on):
		if checked_on.get() == 0:
			self.set(1)
		
		print("checked_on: ", checked_on.get())
		print("spinbox value: ", self.get())

## for testing
def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		first_frame_hold_set = FrameHoldSet(self, "Last Frame Hold")
		first_frame_hold_set.pack(ipadx = 20, ipady = 10)

if __name__ == "__main__":
	main()
