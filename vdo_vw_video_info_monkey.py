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
	def __init__(self, parent,	resolution,	projection,
					image_size,	displacement, *args, **kwargs):
		## init
		super().__init__(parent, *args, **kwargs)
		self.configure(borderwidth = 2, relief = "ridge")
		
		self.padx = 1
		self.padx_east = 5
		self.padx_west = 7
		## setters and getters
		self.resolution = resolution
		self.projection = projection
		self.image_size = image_size
		self.displacement = displacement
		
		self.populate()
	
	def populate(self):
		## populate
		self.video_settings_banner = BannerLabel(self)
		self.resolution_set = ResolutionSet(self)
		self.projection_set = ProjectionSet(self)
		self.pillar_set = PillarDisplacementSet(self)
		self.letterbox_set = LetterboxDisplacementSet(self)
		self.image_size_set = ImageSizeOriginalSet(self)
		
		self.populate_grid()

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
		
	def update_resolution(self, value):
		## update the setting, then
		self.recalculate_info()
		
	def update_projection(self, value):
		## update the setting, then
		self.recalculate_info()
		
	def update_pillar_displacement(self):
		## update the setting, then
		self.recalculate_info()
		
	def update_letterbox_displacement(self):
		## update the setting, then
		self.recalculate_info()
	
	def update_image_size(self):
		## update the setting, then
		self.recalculate_info()

## testing
if __name__ == "__main__":
	def main():
		window = Window()
		window.mainloop()

	class Window(Tk):
		_resolution: str = "1080p"
		_resolution_default: str = "1080p"
		_projection: str = "HDTV"
		_projection_default: str = "HDTV"
		_displacement: int = 0
		_displacement_direction = AP_NEUTRAL
		_image_size: list = [1920, 1080]
		_image_width_default: list = [1920, 1080]
	
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			
			## populate
			info_widget_set = VideoImageInfoSet(self, self.resolution,
									self.projection, self.displacement,
									self.image_size)
									
			info_widget_set.pack(ipadx = 20, ipady = 10)

		@property
		def resolution(self):
			print("self._resolution: ", self._resolution)
			return self._resolution
		
		@resolution.setter
		def resolution(self, value):
			self._resolution = value
			print("self._resolution: ", self._resolution)

		@property
		def projection(self):
			print("self._projection: ", self._projection)
			return self._projection
		
		@projection.setter
		def projection(self, value):
			self._projection = value
			print("self._projection: ", self._projection)

		@property
		def displacement(self):
			print("self._displacement: ", self._displacement)
			return self._displacement
		
		@displacement.setter
		def displacement(self, value):
			self._displacement = value
			print("self._displacement: ", self._displacement)
		
		@property
		def image_size(self):
			print("self._image_size: ", self._image_size)
			return self._image_size
		
		@image_size.setter
		def image_size(self, value):
			self._image_size[0] = value[0]
			self._image_size[1] = value[1]
			print("self._image_size: ", self._image_size)

	main()

