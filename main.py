## TO DO
## - find or create a titlebar icon
## - add titlebar icon code
from tkinter import *
from tkinter import ttk

## local
from filemenu import *
from settingsmenu import *

def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	windowing_system = None
	title_text = "Animator's Pal"
	min_width = 1280
	min_height = 720
	menubar = None
	
	def __init__(self):
		super().__init__()
		## attribute stuff
		self.windowing_system = self.tk.call('tk', 'windowingsystem')
		self.option_add('*tearOff', FALSE) ## Must be set before menus are built
		## population stuff
		self.menubar = Menubar(self)
		## configure stuff
		self.config(width = self.min_width, height = self.min_height)
		self.title(self.title_text)
		self.config(menu = self.menubar)
		
class Menubar(Menu):
	file_menu = None
	settings_menu = None
	
	def __init__(self, window):
		super().__init__(window)
		## attribute stuff
		self.file_menu = FileMenu(self)
		self.settings_menu = SettingsMenu(self)
		## populate
		self.add_cascade(menu = self.file_menu, label = self.file_menu.label_text)
		self.add_cascade(menu = self.settings_menu, label = self.settings_menu.label_text)

if __name__ == "__main__":
	main()
