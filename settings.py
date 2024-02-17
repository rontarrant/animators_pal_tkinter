## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from fps_radio_set import FPSRadioSet
from direction_radio_set import DirectionRadioSet
from shoot_on_set import ShootOnSet
from frame_hold_set import FrameHoldSet
from preferences import Preferences

class SettingsLabelFrame(Labelframe):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.config(text = "Video Output Settings")
		self.grid(sticky = (N, E, W, S))
		self.grid_columnconfigure(0, weight = 1)
		self.grid_columnconfigure(10, weight = 1)

		## children
		self.direction = DirectionRadioSet(self)
		separator1 = Separator(self, orient = VERTICAL)
		self.fps = FPSRadioSet(self)
		separator2 = Separator(self, orient = VERTICAL)
		separator3 = Separator(self, orient = VERTICAL)
		self.shoot_on = ShootOnSet(self)
		separator4 = Separator(self, orient = VERTICAL)
		self.hold_first = FrameHoldSet(self, "first frame hold")
		self.hold_last = FrameHoldSet(self, "last frame hold")
		## layout
		## because of a peculiarity in how padding works, to get the space
		## on the left to match that on the right, padx needs to be applied
		## to the first child widget as shown below. The value matches
		## the parent's xpad value above.
		self.direction.grid(row = 0, column = 1, padx = 2)
		separator1.grid(row = 0, column = 2, padx = 2)
		self.fps.grid(row = 0, column = 3, padx = 2)
		separator2.grid(row = 0, column = 4, padx = 2)
		self.hold_first.grid(row = 0, column = 5, padx = 2)
		separator3.grid(row = 0, column = 6, padx = 2)
		self.shoot_on.grid(row = 0, column = 7, padx = 2)
		separator4.grid(row = 0, column = 8, padx = 2)
		self.hold_last.grid(row = 0, column = 9, padx = 2)
		self.prefs = Preferences()
		self.prefs.assign_widget_variables(self.direction.var,
										self.fps.var,
										self.hold_first.checked_on,
										self.hold_first.spinvalue,
										self.shoot_on.var,
										self.hold_last.checked_on,
										self.hold_last.spinvalue)
		## testing
		#'''
		#button = Button(text = "Update", command = lambda: print(self.prefs))
		#button = Button(text = "Update", command = self.show_preferences)
		#button.grid()
		#'''
		
	def show_preferences(self):
		print("\nPreferences:")
		print("direction - ", self.prefs.direction.get())
		print("frames per second - ", self.prefs.fps.get())
		print("hold_first checked - ", self.prefs.hold_first.get())
		print("hold first frame for - ", self.prefs.hold_first_for.get())
		print("shoot on - ", self.prefs.shoot_on.get())
		print("hold last checked - ", self.prefs.hold_last.get())
		print("hold last frame for - ", self.prefs.hold_last_for.get())
		print("Stored in window: \n", self.parent.image_files)
		print("Stored in prefs: \n", self.prefs.image_file_name_list)
		print("")


## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 840)
	video_settings = SettingsLabelFrame(window)
	video_settings.grid()
	window.mainloop()
