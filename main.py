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
		working_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
		super().__init__(*args, **kwargs)

		## ATTRIBUTE stuff
		self.windowing_system = self.tk.call('tk', 'windowingsystem')
		self.option_add('*tearOff', FALSE) ## Must be set before menus are built
		self.title("Animator's Pal")

		## POPULATION stuff
		mainframe = MainFrame(self)
		'''
		## nametowidget() retrieves an object or method by reference. Here, it's used
		## to set up dependency injection (although, it's unclear if we're violating
		## other OOP principals by doing things this way).
		## In this instance, we reference two objects and a method:
		## - image_size_set,
		## - video_canvas, and
		## - build_new_image_list()
		## These are passed to the menu system so they can be used in menu_file.add_images().
		## The next two lines are here only so I don't forget how to list all children of abs
		## widget (which comes in handy when you're trying to remember the differences in 
		## how we programmers name things and how tkinter names them internally.)
		
		for child in self.nametowidget(".!mainframe.!videomimframe.!videosettingsframe.!videoimageinfoset.!imagesizeset").winfo_children():
			print(child)
		'''
		video_canvas = self.nametowidget(".!mainframe.!videomimframe").video_canvas
		image_size_set = self.nametowidget(".!mainframe.!videomimframe.!videosettingsframe.!videoimageinfoset.!imagesizeset")
		build_new_image_list = self.nametowidget(".!mainframe.!previewmimframe").build_new_image_list
		self._menubar = Menubar(self, video_canvas, image_size_set, build_new_image_list)

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
