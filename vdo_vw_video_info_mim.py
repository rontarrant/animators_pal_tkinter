## vdo_vw_video_info.py
'''
TODO:
- get image width and height
- find closest fit resolution (always 16:9) based on image size
- set resolution
- find closest fit aspect ratio based on image size
- set aspect ratio
- calculate pillar size
- calculate letterbox size
'''

## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from ap_settings import *
from ap_constants import *
from ap_screen_resolutions import screen_resolutions
from vdo_vw_set_resolution import ResolutionSet
from vdo_vw_set_projection import ProjectionSet
from vdo_vw_set_pillarbox_offset import PillarDisplacementSet
from vdo_vw_set_letterbox_offset import LetterDisplacementSet
from vdo_vw_set_image_size import *
from ui_ready import *

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class VideoImageInfoSet(Frame, Observer):
	def __init__(self, parent, video_canvas, *args, **kwargs):
		self.padx = 1
		self.padx_east = 5
		self.padx_west = 7
		self.settings = APSettings()
		
		super().__init__(parent)
		
		self.columnconfigure(0, minsize = 520)
		self.configure(borderwidth = 1)
		self.grid()
		## CHILDREN
		self.resolution_set = ResolutionSet(self, self.padx, self.update)
		self.projection_set = ProjectionSet(self, self.padx, self.update, video_canvas)
		self.pillarbox_displacement_set = PillarDisplacementSet(self, self.padx, self.padx_west)
		self.letterbox_set = LetterDisplacementSet(self, self.padx, self.padx_west)
		self.image_size_set = ImageSizeSet(self, self.padx, self.padx_west)
		
		## Register for ui_ready
		self.ui_ready_instance = UIReady()
		self.ui_ready_instance.attach(self)
		self.ui_ready_instance.attach(self.resolution_set)
		self.ui_ready_instance.attach(self.projection_set)

		self.populate_grid()
	
	def populate_grid(self):
		## set up a grid
		## populate
		self.resolution_set.grid(column = 0, row = 1)
		self.projection_set.grid(column = 0, row = 2)
		self.pillarbox_displacement_set.grid(column = 0, row = 3)
		self.letterbox_set.grid(column = 0, row = 4)
		self.image_size_set.grid(column = 0, row = 5)
	
	def update(self):
		## look up width & height using resolution in screen_resolutions
		resolution = screen_resolutions[self.settings.resolution]
		## look up projection using resolution in screen_resolutions
		projection_dictionary = {self.settings.projection: resolution[self.settings.projection]}
		
		## if projection is ClassicTV, set pillarbox_offset to non-zero
		if list(projection_dictionary.keys())[0] == "ClassicTV":
			self.settings.pillarbox_offset = projection_dictionary[self.settings.projection]["h_offset"]
			#self.pillarbox_displacement_set.update(self.settings.pillarbox_offset)
			self.settings.letterbox_offset = 0
			self.letterbox_set.update(self.settings.letterbox_offset)
		else: ## else set letterbox_offset to non-zero
			self.settings.letterbox_offset = projection_dictionary[self.settings.projection]["v_offset"]
			self.letterbox_set.update(self.settings.letterbox_offset)
			self.settings.pillarbox_offset = 0
			#self.pillarbox_displacement_set.update(self.settings.pillarbox_offset)
			
		##ic(self.settings.resolution, self.settings.projection, resolution[self.settings.projection])

## testing
if __name__ == "__main__":
	def main():
		window = Window()
		window.mainloop()

	class Window(Tk):
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			
			## populate
			self.settings = APSettings()
			#self.change_settings()
			info_widget_set = VideoImageInfoSet(self)

		def change_settings(self):
			self.settings.resolution = "8k"
			self.settings.projection = "ClassicTV"
			
	main()

