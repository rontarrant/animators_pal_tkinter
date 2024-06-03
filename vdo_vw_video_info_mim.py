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
from ap_screen_resolutions import *
from vdo_vw_set_banner_label import *
from vdo_vw_set_resolution import *
from vdo_vw_set_projection import *
from vdo_vw_set_pillar_displacement import *
from vdo_vw_set_letterbox_displacement import *
from vdo_vw_set_image_size_original import *
from ui_ready import *

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class VideoImageInfoSet(Frame):
	def __init__(self, parent, *args, **kwargs):
		self.padx = 1
		self.padx_east = 5
		self.padx_west = 7
		self.settings = APSettings.get_instance()
		self.ui_ready = UIReady.get_instance()
		
		super().__init__(parent)
		
		self.columnconfigure(0, minsize = 520)
		self.configure(borderwidth = 1)
		self.grid()
		## populate
		#self.video_settings_banner = BannerLabel(self)
		self.resolution_set = ResolutionSet(self, self.padx, self.post_info)
		self.projection_set = ProjectionSet(self, self.padx, self.post_info)
		self.pillar_set = PillarDisplacementSet(self, self.padx, self.padx_west)
		self.letterbox_set = LetterboxDisplacementSet(self, self.padx, self.padx_west)
		self.image_size_set = ImageSizeSet(self, self.padx, self.padx_west)
		
		self.populate_grid()
	
	def populate_grid(self):
		## set up a grid
		## populate
		#self.video_settings_banner.grid(column = 0, row = 0, pady = 5)
		self.resolution_set.grid(column = 0, row = 1)
		self.projection_set.grid(column = 0, row = 2)
		self.pillar_set.grid(column = 0, row = 3)
		self.letterbox_set.grid(column = 0, row = 4)
		self.image_size_set.grid(column = 0, row = 5)
		self.after(0, self.go_time)
		
	def go_time(self):
		self.ui_ready.ui_ready = True

	def post_info(self):
		## look up width & height using resolution in screen_resolutions
		## look up projection using resolution in screen_resolutions
		## ic(self.settings.resolution, self.settings.projection)
		resolution = screen_resolutions[self.settings.resolution]
		projection_dictionary = {self.settings.projection: resolution[self.settings.projection]}
		## ic(projection_dictionary)
		## if ClassicTV, set pillar_displacement to non-zero
		## else set letterbox_displacement to non-zero
		if list(projection_dictionary.keys())[0] == "ClassicTV (4:3)":
			self.settings.pillar_displacement = projection_dictionary[self.settings.projection]["displacement"]
			self.pillar_set.update(self.settings.pillar_displacement)
			self.settings.letterbox_displacement = 0
			self.letterbox_set.update(self.settings.letterbox_displacement)
			## ic(self.settings.pillar_displacement)
		else:
			self.settings.letterbox_displacement = projection_dictionary[self.settings.projection]["displacement"]
			self.letterbox_set.update(self.settings.letterbox_displacement)
			self.settings.pillar_displacement = 0
			self.pillar_set.update(self.settings.pillar_displacement)
			## ic(self.settings.letterbox_displacement)
		## look up original image width & height in:
		##	image_collection.images.width & image_collection.images.height
		## fill in image width & height settings

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

