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
from vdo_vw_set_banner_label import *
from vdo_vw_set_resolution import *
from vdo_vw_set_projection import *
from vdo_vw_set_pillar_displacement import *
from vdo_vw_set_letterbox_displacement import *
from vdo_vw_set_image_size_original import *
from ap_constants import *

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class VideoImageInfoSet(Frame):
	def __init__(self, parent, settings, *args, **kwargs):
		self.padx = 1
		self.padx_east = 5
		self.padx_west = 7
		
		super().__init__(parent, *args, **kwargs)
		self.configure(borderwidth = 2, relief = "ridge")
		## populate
		self.settings = settings
		self.video_settings_banner = BannerLabel(self)
		self.resolution_set = ResolutionSet(self)
		self.projection_set = ProjectionSet(self)
		self.pillar_set = PillarDisplacementSet(self)
		self.letterbox_set = LetterboxDisplacementSet(self)
		self.image_size_set = ImageSizeSet(self)
		
		self.populate_grid()
		## this may be the way to update settings from a file??
		self.update_display_resolution()
		self.update_display_projection()
	
	def populate_grid(self):
		## set up a grid
		self.columnconfigure(0, minsize = 260)
		self.columnconfigure(1, minsize = 260)
		## populate
		self.video_settings_banner.grid(column = 0, row = 0, columnspan = 2, pady = (15, 10))
		## column 0
		self.resolution_set.label.grid(column = 0, row = 1, sticky = E, padx = self.padx)
		self.projection_set.label.grid(column = 0, row = 2, sticky = E, padx = self.padx_east)
		self.pillar_set.label.grid(column = 0, row = 3, sticky = E, padx = self.padx)
		self.letterbox_set.label.grid(column = 0, row = 4, sticky = E, padx = self.padx)
		self.image_size_set.label.grid(column = 0, row = 5, sticky = E, padx = self.padx)
		## column 1
		self.resolution_set.option_menu.grid(column = 1, row = 1, sticky = W, padx = self.padx)
		self.projection_set.option_menu.grid(column = 1, row = 2, sticky = W, padx = self.padx)
		self.pillar_set.value_label.grid(column = 1, row = 3, sticky = W, padx = self.padx_west)
		self.letterbox_set.value_label.grid(column = 1, row = 4, sticky = W, padx = self.padx_west)
		self.image_size_set.value_label.grid(column = 1, row = 5, sticky = W, padx = self.padx_west)

	def recalculate_info(self):
		pass
		## call this after any change in the video settings
		## to update all video/image info fields
		## this is just so I have a change to commit
		
	def update_display_resolution(self):
		self.resolution_set.update(self.settings.resolution)
		self.recalculate_info()
		
	def update_resolution(self, value):
		self.resolution = value
		self.recalculate_info()
		
	def update_display_projection(self):
		self.projection_set.update(self.settings.projection)
		self.recalculate_info()
		
	def update_projection(self, value):
		self.projection = value
		self.recalculate_info()
		
	def update_pillar_displacement(self, value):
		self.pillar_displacement = value
		self.recalculate_info()
		
	def update_display_pillar_displacement(self):
		self.pillar_displacement_set.update(value)
		self.recalculate_info()
		
	def update_letterbox_displacement(self, value):
		self.letterbox_displacement = value
		self.recalculate_info()
		
	def update_display_letterbox_displacement(self):
		self.letterbox_displacement_set.update(value)
		self.recalculate_info()
		
	def update_image_size(self, value):
		self.image_size[0] = value[0]
		self.image_size[1] = value[1]
		self.recalculate_info()

	def update_display_image_size(self):
		self.image_size_set.update(self.image_size[0], self.image_size[1])
		self.recalculate_info()

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
			self.change_settings()
			info_widget_set = VideoImageInfoSet(self, self.settings)
			
			info_widget_set.pack(ipadx = 20, ipady = 10)

		def change_settings(self):
			self.settings.resolution = "8k"
			self.settings.projection = "ClassicTV"
			
	main()

