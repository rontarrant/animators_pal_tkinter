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

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class VideoImageInfoSet(Frame):
	def __init__(self, parent,
								resolution_getter, resolution_setter,
								projection_getter, projection_setter,
								image_size_getter, image_size_setter,
								pillar_getter, pillar_setter,
								letterbox_getter, letterbox_setter,
								*args, **kwargs):
		## init
		super().__init__(parent, *args, **kwargs)
		self.configure(borderwidth = 2, relief = "ridge")
		
		self.padx = 1
		self.padx_east = 5
		self.padx_west = 7
		## setters and getters
		self.resolution_getter = resolution_getter
		self.resolution_setter = resolution_setter
		self.projection_getter = projection_getter
		self.projection_setter = projection_setter
		self.image_size_getter = image_size_getter
		self.image_size_setter = image_size_setter
		self.pillar_getter = pillar_getter
		self.pillar_setter = pillar_setter
		self.letterbox_getter = letterbox_getter
		self.letterbox_setter = letterbox_setter
		
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
	
	def update_original_image_size(self):
		## update the setting, then
		self.recalculate_info()

## testing
if __name__ == "__main__":
	def main():
		window = Window()
		window.mainloop()

	class Window(Tk):
		def __init__(self, *args, **kwargs):
			## properties
			self.format = "8k"
			self.projection = [7680, 4320]
			self.image_size = []
			self.pillar_displacement = 0
			self.letterbox_displacment = 0
			
			## init
			super().__init__(*args, **kwargs)
			
			## populate
			info_widget_set = VideoImageInfoSet(self,
									self.resolution_getter, self.resolution_setter,
									self.projection_getter, self.projection_setter,
									self.image_size_getter, self.image_size_setter,
									self.pillar_displacement_getter, self.pillar_displacement_setter,
									self.letterbox_displacement_getter, self.letterbox_displacement_setter)
									
			info_widget_set.pack(ipadx = 20, ipady = 10)

		def resolution_getter(self):
			print("self.format: ", self.format)
			return self.format
			
		def resolution_setter(self, value):
			self.format = value
			print("self.format: ", self.format)

		def projection_getter(self):
			print("self.projection: ", self.projection)
			return self.projection
			
		def projection_setter(self, value):
			self.projection = value
			print("self.projection: ", self.projection)

		def image_size_getter(self):
			print("self.image_size: ", self.image_size)
			return self.image_size
			
		def image_size_setter(self, value):
			self.image_size = value
			print("self.image_size: ", self.image_size)

		def pillar_displacement_getter(self):
			print("self.pillar_displacement: ", self.pillar_displacement)
			return self.pillar_displacement
			
		def pillar_displacement_setter(self, value):
			self.pillar_displacement = value
			print("self.pillar_displacement: ", self.pillar_displacement)

		def letterbox_displacement_getter(self):
			print("self.letterbox_displacement: ", self.letterbox_displacement)
			return self.letterbox_displacement
			
		def letterbox_displacement_setter(self, value):
			self.letterbox_displacement = value
			print("self.letterbox_displacement: ", self.letterbox_displacement)

	main()

