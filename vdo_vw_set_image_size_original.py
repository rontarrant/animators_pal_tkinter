## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from ap_screen_resolutions import *
from ap_settings import *

class ImageSizeSet(Frame):
	def __init__(self, parent, padx, padx_west, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.ap_settings = APSettings()

		self.settings = APSettings.get_instance()
		self.columnconfigure(0, minsize = 260)
		self.columnconfigure(1, minsize = 260)

		self.label = Label(self, text = "Original Image Size")
		self.value_label = Label(self, text = str(self.ap_settings.image_width) + " x " + str(self.ap_settings.image_height))
		
		self.label.grid(row = 0, column = 0, sticky = E, padx = padx)
		self.value_label.grid(row = 0, column = 1, sticky = W, padx = padx_west)
	
	def update(self, width, height):
		ic()
		self.value_label.config(text = str(width) + " x " + str(height))

## testing
def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.settings = APSettings()
		image_size_set = ImageSizeSet(self, 10, 20)
		image_size_set.pack(ipadx = 20, ipady = 10)

if __name__ == "__main__":
	main()
