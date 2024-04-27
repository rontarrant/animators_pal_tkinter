## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from pvw_monkey_frame import *
from vdo_monkey_frame import *

class MainFrame(Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid() ## place the MainFrame in the window
		# populate
		video_monkey_frame = VideoMonkeyFrame(self)
		preview_monkey_frame = PreviewMonkeyFrame(self)
		
		# layout
		## set the row and column minimum sizes
		for row in range(13):
			self.grid_rowconfigure(row, minsize = 72)
		
		for column in range(13):
			self.grid_columnconfigure(column, minsize = 128)
			
		## insert frames for each window area
		preview_monkey_frame.grid(row = 0, column = 0, rowspan = 13, columnspan = 3, sticky = (N, E, W, S))
		video_monkey_frame.grid(row = 0, column = 3, rowspan = 13, columnspan = 10, sticky = (N, E, W, S))

## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 950)
	mainframe = MainFrame(window)
	mainframe.grid()
	window.mainloop()