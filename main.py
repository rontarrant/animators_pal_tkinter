## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from mainframe import *
from menu import *

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
		mainframe = MainFrame(self)
		show_next_frame = self.nametowidget(".!mainframe.!videomonkeyframe").show_next_frame
		build_new_image_list = self.nametowidget(".!mainframe.!previewmonkeyframe").build_new_image_list
		self._menubar = Menubar(self, show_next_frame, build_new_image_list)

		## CONFIGURE window stuff
		self.config(width = self.min_width, height = self.min_height)
		self.minsize(self.min_width, self.min_height)
		self.title(self.title_text)
		self.config(menu = self._menubar)

		## titlebar icon
		photo = PhotoImage(file = os.path.join(working_dir, "images/bobby_bowtie_icon60x.png"))
		self.iconphoto(True, photo)

if __name__ == "__main__":
	main()
