## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from mainframe import *
from menu import *
from ui_ready import *
from observer import Observer

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

def main():
	window = Window()
	window.mainloop()

class Window(Tk, Observer):
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
		# Get the UIReady instance and initialize it
		self.ui_ready_instance = UIReady()
		self.ui_ready_instance.initialize(self)

		# Attach Settings as an observer
		self.ap_settings = APSettings()
		self.ui_ready_instance.attach(self.ap_settings)

		## open the window in the same position it was last closed
		self.load_window_position()
		self.protocol("WM_DELETE_WINDOW", self.on_close)

		## ATTRIBUTE stuff
		self.windowing_system = self.tk.call('tk', 'windowingsystem')
		self.option_add('*tearOff', FALSE) ## Must be set before menus are built
		self.title("Animator's Pal")

		## POPULATION stuff
		mainframe = MainFrame(self)
		
		video_canvas = self.nametowidget(".!mainframe.!videomimframe").video_canvas
		image_size_set = mainframe.image_size_set
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
		
		## UI READY
		## Make sure the UI is ready before trying to restore saved settings into
		## UI elements.
		self.after(100, self.ui_ready_instance.check_ui_ready)
		
		## Checking that the UI is ready ends up with the root window
		## being pushed behind whatever other application windows are
		## on screen. This brings it to the front.
		self.lift()

		
	def update(self):
		self.ap_settings.load_settings()
		## update the UI from ap_settings
		
	def save_all_settings(self):
		x = self.winfo_x()
		y = self.winfo_y()
		self.ap_settings.window_position = {'x': x, 'y': y}
		self.ap_settings.save_settings()
	
	def load_window_position(self):
		pos = self.ap_settings.window_position
		self.geometry(f"+{pos['x']}+{pos['y']}")

	def on_close(self):
		self.save_all_settings()
		self.destroy()

if __name__ == "__main__":
	main()
