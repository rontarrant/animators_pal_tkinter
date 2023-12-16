## TO DO
## - find or create a titlebar icon
## - add titlebar icon code

## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter import ttk

## local
from filemenu import *
from settingsmenu import *
from helpmenu import *

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	windowing_system = None
	title_text = "Animator's Pal"
	min_width = 1280
	min_height = 720
	_menubar = None
	_image_files = None

	def __init__(self, *args, **kwargs):
		working_dir = os.path.abspath(os.path.dirname(sys.argv[0]))

		super().__init__(*args, **kwargs)

		## ATTRIBUTE stuff
		self.windowing_system = self.tk.call('tk', 'windowingsystem')
		self.option_add('*tearOff', FALSE) ## Must be set before menus are built
		self.title("Animator's Pal")

		## POPULATION stuff
		self._menubar = Menubar(self)
		self.canvas = Canvas(self)

		## CONFIGURE window stuff
		self.config(width = self.min_width, height = self.min_height)
		self.title(self.title_text)
		self.config(menu = self._menubar)

		## titlebar icon
		photo = PhotoImage(file = os.path.join(working_dir, "images/bobby_bowtie_icon60x.png"))
		self.iconphoto(True, photo)

class Menubar(Menu):
	file_menu = None
	settings_menu = None
	help_menu = None

	def __init__(self, window):
		super().__init__(window)
		## ATTRIBUTE stuff
		self.file_menu = FileMenu(self, window)
		self.settings_menu = SettingsMenu(self, window)
		self.help_menu = HelpMenu(self)

		## POPULATE
		self.add_cascade(menu = self.file_menu, label = self.file_menu.label_text)
		self.add_cascade(menu = self.settings_menu, label = self.settings_menu.label_text)
		self.add_cascade(menu = self.help_menu, label = self.help_menu.label_text)

if __name__ == "__main__":
	main()
