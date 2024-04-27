## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from vdo_vw_set_fps_radio import FPSRadioSet
from vdo_vw_set_direction_radio import DirectionRadioSet
from vdo_vw_set_shoot_on import ShootOnSet
from ap_settings import *

class VideoSettingsFrame(Labelframe):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.config(text = "Video Output Settings")
		self.config(width = 1280, height = 144)
		settings = APSettings()
		self.grid_propagate(False)
		self.grid(sticky = (N, E, W, S))
		self.grid_columnconfigure(0, weight = 1)
		self.grid_columnconfigure(10, weight = 1)

		## children
		direction = DirectionRadioSet(self, settings.get_direction, settings.set_direction)
		separator1 = Separator(self, orient = VERTICAL)
		fps = FPSRadioSet(self, settings.get_fps, settings.set_fps)
		separator2 = Separator(self, orient = VERTICAL)
		separator3 = Separator(self, orient = VERTICAL)
		shoot_on = ShootOnSet(self, settings.get_shoot_on, settings.set_shoot_on)
		separator4 = Separator(self, orient = VERTICAL)
		## layout
		## because of a peculiarity in how padding works, to get the space
		## on the left to match that on the right, padx needs to be applied
		## to the first child widget as shown below. The value matches
		## the parent's xpad value above.
		direction.grid(row = 0, column = 1, padx = 2)
		separator1.grid(row = 0, column = 2, padx = 2)
		fps.grid(row = 0, column = 3, padx = 2)
		separator2.grid(row = 0, column = 4, padx = 2)
		shoot_on.grid(row = 0, column = 7, padx = 2)
		separator4.grid(row = 0, column = 8, padx = 2)
		
## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 840)
	video_settings = VideoSettingsFrame(window)
	video_settings.grid()
	window.mainloop()