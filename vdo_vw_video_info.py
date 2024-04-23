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
from tkinter import font

## local
from ap_projection_ratios import *
from ap_screen_resolutions import *

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class VideoImageInfoSet(Frame):
		
	def __init__(self, parent, format_getter, format_setter,
								frame_size_getter, frame_size_setter,
								image_size_getter, image_size_setter,
								pillar_displacement_getter, pillar_displacement_setter,
								letterbox_displacement_getter, letterbox_displacement_setter,
								*args, **kwargs):
		## init
		super().__init__(parent, *args, **kwargs)
		self.configure(borderwidth = 2, relief = "ridge")
		
		self.padx = 20
		self.padx_east = 20
		self.padx_west = 27

		self.instantiate_children()
		self.populate_grid()

	def instantiate_children(self):
		## populate
		self.video_settings_banner = BannerLabel(self)
		self.resolution_set = ResolutionSet(self)
		self.aspect_ratio_set = AspectRatioSet(self)
		self.pillar_set = PillarDisplacementSet(self)
		self.letterbox_set = LetterboxSet(self)
		self.image_size_set = ImageSizeSet(self)

	def populate_grid(self):
		## set up a grid
		self.columnconfigure(0, minsize = 260)
		self.columnconfigure(1, minsize = 260)
		## populate
		self.video_settings_banner.grid(column = 0, row = 0, columnspan = 2, pady = (15, 10))
		## column 0
		self.resolution_set.label.grid(column = 0, row = 1, sticky = E, padx = self.padx)
		self.aspect_ratio_set.label.grid(column = 0, row = 2, sticky = E, padx = self.padx_east)
		self.pillar_set.label.grid(column = 0, row = 3, sticky = E, padx = self.padx)
		self.letterbox_set.label.grid(column = 0, row = 4, sticky = E, padx = self.padx)
		self.image_size_set.label.grid(column = 0, row = 5, sticky = E, padx = self.padx)
		## column 1
		self.resolution_set.option_menu.grid(column = 1, row = 1, sticky = W, padx = self.padx)
		self.aspect_ratio_set.option_menu.grid(column = 1, row = 2, sticky = W, padx = self.padx)
		self.pillar_set.value_label.grid(column = 1, row = 3, sticky = W, padx = self.padx_west)
		self.letterbox_set.value_label.grid(column = 1, row = 4, sticky = W, padx = self.padx_west)
		self.image_size_set.value_label.grid(column = 1, row = 5, sticky = W, padx = self.padx_west)

class BannerLabel(Label):
	def __init__(self, parent):
		super().__init__(parent)
		self.text = "Video & Image Info"
		self.display_font = font.Font(family = "System", size = 14, weight = "bold")
		self.config(text = self.text, font = self.display_font)
		
class ResolutionSet(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		## these resolutions all have a 16:9 ratio
		self.options = ["8k", "6k", "5k", "4k", "3k", "2k", "1080p", "720p"]
		self.selection = StringVar()
		self.option_menu = OptionMenu(parent, self.selection, *self.options)
		self.selection.trace('w', self.show)

		self.label = Label(parent, text = "Resolution")

	def show(self, *args):
		print(self.selection.get())
	
	def get(self):
		return self.resolution
	
	def set(self, value):
		self.resolution = value
	
class AspectRatioSet(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.options = ["Classic TV (4:3)", "IMAX (22:16)", "HDTV (16:9)", 
							"Vistavision (37:20)", "CinemaScope (21:9)", 
							"Anamorphic Widescreen (239:100)", "MGM 65 (69:25)"]
		
		self.label = Label(parent, text = "Aspect Ratio")
		
		self.selection = StringVar(parent)
		self.option_menu = OptionMenu(parent, self.selection, *self.options)
		self.selection.trace('w', self.show)
		
	def show(self, *args):
		print(self.selection.get())

class PillarDisplacementSet(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.label = Label(parent, text = "Pillar Displacement")
		self.value_label = Label(parent, text = "0")
		self.width = IntVar()
	
	def get(self):
		return self.width.get()
		
	def set(self, value):
		self.width.set(value)

class LetterboxSet(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		
		self.label = Label(parent, text = "Letterbox Displacement")
		self.value_label = Label(parent, text = "0")
		self.height = IntVar()

	def get(self):
		return self.height.get()
		
	def set(self, value):
		self.height.set(value)


class ImageSizeSet(Frame):
	width  = 0
	height = 0
	
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		self.label = Label(parent, text = "Image Size")
		self.value_label = Label(parent, text = "1920 x 1080")
		
	def set(self, width, height):
		self.width = size[0]
		self.height = size[1]
	
	def get(self):
		return self.width, self.height

## testing
if __name__ == "__main__":
	def main():
		window = Window()
		window.mainloop()

	class Window(Tk):
		def __init__(self, *args, **kwargs):
			## properties
			self.format = "8k"
			self.frame_size = [7680, 4320]
			self.image_size = []
			self.pillar_displacement = 0
			self.letterbox_displacment = 0
			
			## init
			super().__init__(*args, **kwargs)
			
			## populate
			info_widget_set = VideoImageInfoSet(self, self.format_getter, self.format_setter,
									self.frame_size_getter, self.frame_size_setter,
									self.image_size_getter, self.image_size_setter,
									self.pillar_displacement_getter, self.pillar_displacement_setter,
									self.letterbox_displacement_getter, self.letterbox_displacement_setter)
									
			info_widget_set.pack(ipadx = 20, ipady = 10)

		def format_getter(self):
			print("self.format: ", self.format)
			return self.format
			
		def format_setter(self, value):
			self.format = value
			print("self.format: ", self.format)

		def frame_size_getter(self):
			print("self.frame_size: ", self.frame_size)
			return self.frame_size
			
		def frame_size_setter(self, value):
			self.frame_size = value
			print("self.frame_size: ", self.frame_size)

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

