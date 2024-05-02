## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from pvw_mim_frame import *
from vdo_mim_frame import *
from ui_ready import *

class MainFrame(Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid() ## place the MainFrame in the window
		self.ui_ready = UIReady()
		# populate
		video_mim_frame = VideoMiMFrame(self)
		preview_mim_frame = PreviewMiMFrame(self)
		
		# layout
		## set the row and column minimum sizes
		for row in range(13):
			self.grid_rowconfigure(row, minsize = 72)
		
		for column in range(13):
			self.grid_columnconfigure(column, minsize = 128)
			
		## insert frames for each window area
		preview_mim_frame.grid(row = 0, column = 0, rowspan = 13, columnspan = 3, sticky = (N, E, W, S))
		video_mim_frame.grid(row = 0, column = 3, rowspan = 13, columnspan = 10, sticky = (N, E, W, S))
		self.ui_ready.set()
		

## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 950)
	mainframe = MainFrame(window)
	mainframe.grid()
	window.mainloop()
