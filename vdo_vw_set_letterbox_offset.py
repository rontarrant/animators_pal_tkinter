## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from ap_screen_resolutions import *

class LetterboxDisplacementSet(Frame):
	def __init__(self, parent, padx, padx_west, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.columnconfigure(0, minsize = 260)
		self.columnconfigure(1, minsize = 260)

		self.label = Label(self, text = "Letterbox Displacement")
		self.value_label = Label(self, text = "0")
		self.height = IntVar()
		
		self.label.grid(row = 0, column = 0, sticky = E, padx = padx)
		self.value_label.grid(row = 0, column = 1, sticky = W, padx = padx_west)

	def update(self, value):
		self.value_label.config(text = value)

## testing
def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		letterbox_offset_set = LetterboxDisplacementSet(self, 10, 20)
		letterbox_offset_set.pack(ipadx = 20, ipady = 10)

if __name__ == "__main__":
	main()
