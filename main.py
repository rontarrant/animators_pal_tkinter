## TO DO
## - find or create a titlebar icon
## - add titlebar icon code

## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from filemenu import *
from helpmenu import *
from preferences import Preferences
from fps_radio_set import FPSRadioSet
from direction_radio_set import DirectionRadioSet
from shoot_on_set import ShootOnSet
from frame_hold_set import FrameHoldSet

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	windowing_system = None
	title_text = "Animator's Pal"
	min_width = 1280
	min_height = 720
	_menubar = None
	_toolbar = None

	def __init__(self, *args, **kwargs):
		working_dir = os.path.abspath(os.path.dirname(sys.argv[0]))

		super().__init__(*args, **kwargs)

		## ATTRIBUTE stuff
		self.windowing_system = self.tk.call('tk', 'windowingsystem')
		self.option_add('*tearOff', FALSE) ## Must be set before menus are built
		self.title("Animator's Pal")

		## POPULATION stuff
		self._menubar = Menubar(self)
		self._toolbar = SettingsBar(self)
		self.canvas = Canvas(self)

		## CONFIGURE window stuff
		self.config(width = self.min_width, height = self.min_height)
		self.title(self.title_text)
		self.config(menu = self._menubar)
		self._toolbar.pack(side = 'left', padx = 20, pady = 20, ipadx = 10, ipady = 10)

		## titlebar icon
		photo = PhotoImage(file = os.path.join(working_dir, "images/bobby_bowtie_icon60x.png"))
		self.iconphoto(True, photo)

class Menubar(Menu):
	file_menu = None
	preferences_menu = None
	help_menu = None

	def __init__(self, window):
		super().__init__(window)
		## ATTRIBUTE stuff
		self.file_menu = FileMenu(self, window)
		self.help_menu = HelpMenu(self)

		## POPULATE
		self.add_cascade(menu = self.file_menu, label = self.file_menu.label_text)
		self.add_cascade(menu = self.help_menu, label = self.help_menu.label_text)

class SettingsBar(Labelframe):
	def __init__(self, parent):
		super().__init__(parent)
		self.config(text = "Preferences")
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
		button = Button(text = "Update", command = self.show_preferences)
		button.pack()
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
		print("")
		
if __name__ == "__main__":
	main()
