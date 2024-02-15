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
		self.direction.pack(side = 'left', padx = (20, 0))
		separator1.pack(side = 'left', padx = 5)
		self.fps.pack(side = 'left', padx = 5)
		separator2.pack(side = 'left', padx = 5)
		self.hold_first.pack(side = "left")
		separator3.pack(side = 'left', padx = 5)
		self.shoot_on.pack(side = 'left')
		separator4.pack(side = 'left', padx = 5)
		self.hold_last.pack(side = 'left')
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
		#button.pack()
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