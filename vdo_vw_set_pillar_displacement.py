## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from ap_screen_resolutions import *
from ap_settings import *

class PillarDisplacementSet(Frame):
	def __init__(self, parent, padx, padx_west, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.settings = APSettings()
		self.columnconfigure(0, minsize = 260)
		self.columnconfigure(1, minsize = 260)
		
		self.label = Label(self, text = "Pillar Displacement")
		self.value_label = Label(self, text = "0")
		self.width = IntVar()
		
		self.label.grid(row = 0, column = 0, sticky = E, padx = padx)
		self.value_label.grid(row = 0, column = 1, sticky = W, padx = padx_west)
	
	def update(self, value):
		ic(value)
		self.value_label.config(text = value)

## testing
def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.settings = APSettings()
		pillar_displacement_set = PillarDisplacementSet(self, 10, 20)
		pillar_displacement_set.pack(ipadx = 20, ipady = 10)

if __name__ == "__main__":
	main()
