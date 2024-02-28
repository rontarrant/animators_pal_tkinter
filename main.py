## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from filemenu import *
from helpmenu import *
from settings import SettingsLabelFrame
from video_canvas import VideoCanvas
from video_controls import VideoControlsFrame
from ap_image import APImage
from image_collection import TKImageCollection
from image_list import FileNamesFrame

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
	min_width = 1664
	min_height = 950
	_menubar = None
	_frame = None
	image_files = []

	def __init__(self, *args, **kwargs):
		working_dir = os.path.abspath(os.path.dirname(sys.argv[0]))

		super().__init__(*args, **kwargs)

		## ATTRIBUTE stuff
		self.windowing_system = self.tk.call('tk', 'windowingsystem')
		self.option_add('*tearOff', FALSE) ## Must be set before menus are built
		self.title("Animator's Pal")

		## POPULATION stuff
		self._menubar = Menubar(self)
		self._frame = MainFrame(self)

		## CONFIGURE window stuff
		self.config(width = self.min_width, height = self.min_height)
		self.minsize(self.min_width, self.min_height)
		self.title(self.title_text)
		self.config(menu = self._menubar)

		## titlebar icon
		photo = PhotoImage(file = os.path.join(working_dir, "images/bobby_bowtie_icon60x.png"))
		self.iconphoto(True, photo)

class MainFrame(Frame):
	def __init__(self, window):
		super().__init__(window)
		# configure
		self.grid() ## place the MainFrame in the window
		# populate
		image_list_frame = Frame(self, bg = 'peach puff')
		output_settings_frame = SettingsLabelFrame(self)
		image_thumbnail_frame = Frame(self, bg = 'lawn green')
		video_canvas_frame = VideoCanvas(self)
		video_controls_frame = VideoControlsFrame(self)
		
		# layout
		## set the row and column minimum sizes
		for row in range(13):
			self.grid_rowconfigure(row, minsize = 72)
		
		for column in range(13):
			self.grid_columnconfigure(column, minsize = 128)
			
		## insert frames for each window area
		image_list_frame.grid(row = 0, column = 0, rowspan = 10, columnspan = 3, sticky = (N, E, W, S))
		output_settings_frame.grid(row = 0, column = 3, rowspan = 2, columnspan = 10, sticky = (N, E, W, S))
		image_thumbnail_frame.grid(row = 10, column = 0, rowspan = 3, columnspan = 3, sticky = (N, E, W, S))
		video_canvas_frame.grid(row = 2, column = 3, rowspan = 10, columnspan = 10, sticky = (N, E, W, S))
		video_controls_frame.grid(row = 12, column = 3, columnspan = 10, sticky = (N, E, W, S))

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
		
if __name__ == "__main__":
	main()
