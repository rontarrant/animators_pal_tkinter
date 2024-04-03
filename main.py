## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from menu_file import *
from menu_help import *
from fr_settings import SettingsLabelFrame
from fr_video_canvas import VideoCanvas
from fr_thumbnail import ThumbnailFrame
from fr_video_controls import VideoControlsFrame
from fr_treeframe import TreeFrame
from ap_image_collection import APImageCollection

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
	project_name = None
	image_collection = APImageCollection()

	def __init__(self, *args, **kwargs):
		'''
		You'll notice that MainFrame is instantiated before the Menubar.
		This is because the menu system needs access to the video_canvas
		and the treeframe for communication purposes during runtime.
		These variables (video_canvas and treeframe) are injected
		into the Menubar which injects it into the File menu which passes
		them along to the add_images() method. There, they are used to
		push a list of file names into the Treeview and push the first
		image in the list onto the VideoCanvas.
		'''
		working_dir = os.path.abspath(os.path.dirname(sys.argv[0]))

		super().__init__(*args, **kwargs)

		## ATTRIBUTE stuff
		self.windowing_system = self.tk.call('tk', 'windowingsystem')
		self.option_add('*tearOff', FALSE) ## Must be set before menus are built
		self.title("Animator's Pal")

		## POPULATION stuff
		self._frame = MainFrame(self)
		show_next_frame = self.nametowidget(".!mainframe.!videocanvas").show_next_frame
		build_new_image_list = self.nametowidget(".!mainframe.!treeframe").build_new_image_list
		self._menubar = Menubar(self, show_next_frame, build_new_image_list)

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
		column_count = 4
		self.grid() ## place the MainFrame in the window
		# populate
		self.video_canvas = VideoCanvas(self) ## so a method can be passed to TreeFrame
		self.thumbnail_frame = ThumbnailFrame(self)
		self.tree_frame = TreeFrame(self, column_count, self.thumbnail_frame.preview_thumbnail)
		self.output_settings_frame = SettingsLabelFrame(self)
		self.video_controls_frame = VideoControlsFrame(self, self.video_canvas)

		# layout
		## set the row and column minimum sizes
		for row in range(13):
			self.grid_rowconfigure(row, minsize = 72)
		
		for column in range(13):
			self.grid_columnconfigure(column, minsize = 128)
			
		## insert frames for each window area
		self.tree_frame.grid(row = 0, column = 0, rowspan = 10, columnspan = 3, sticky = (N, E, W, S))
		self.output_settings_frame.grid(row = 0, column = 3, rowspan = 2, columnspan = 10, sticky = (N, E, W, S))
		self.thumbnail_frame.grid(row = 10, column = 0, rowspan = 3, columnspan = 3, sticky = (N, E, W, S))
		self.video_canvas.grid(row = 2, column = 3, rowspan = 10, columnspan = 10, sticky = (N, E, W, S))
		self.video_controls_frame.grid(row = 12, column = 3, columnspan = 10, sticky = (N, E, W, S))
		#self.show_frames()
	
	def show_frames(self):
		## # ic(self.winfo_children())
		pass
		
class Menubar(Menu):
	file_menu = None
	preferences_menu = None
	help_menu = None

	def __init__(self, window, show_next_frame, build_new_image_list):
		super().__init__(window)
		## ATTRIBUTE stuff
		self.file_menu = FileMenu(self, window, show_next_frame,build_new_image_list)
		self.help_menu = HelpMenu(self)

		## POPULATE
		self.add_cascade(menu = self.file_menu, label = self.file_menu.label_text)
		self.add_cascade(menu = self.help_menu, label = self.help_menu.label_text)
		
if __name__ == "__main__":
	main()
