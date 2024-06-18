'''
menu.py
'''
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from menu_file import *
from menu_help import *

class Menubar(Menu):
	file_menu = None
	preferences_menu = None
	help_menu = None

	def __init__(self, window, video_canvas, image_size_set, build_new_image_list):
		super().__init__(window)
		## ATTRIBUTE stuff
		self.file_menu = FileMenu(self, window, video_canvas, image_size_set, build_new_image_list)
		self.help_menu = HelpMenu(self)

		## POPULATE
		self.add_cascade(menu = self.file_menu, label = self.file_menu.label_text)
		self.add_cascade(menu = self.help_menu, label = self.help_menu.label_text)
		