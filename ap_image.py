import os
import cv2
import sys ## for testing only
import PIL.Image, PIL.ImageTk, PIL.ImageDraw
from tkinter import Tk
from tkinter import Canvas

## local
from ap_settings import APSettings
from ap_projection_ratios import projection_ratios
from ap_screen_resolutions import screen_resolutions
from checkerboard import Checkerboard

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class APImage():
	def __init__(self, full_path_and_file):
		## external
		self.ap_settings = APSettings.get_instance()
		## image data
		self._pillow_image = None
		self._image_4_display = None
		self._cv_image = None
		self.image_pillarboxing_width = 0
		self.image_letterboxing_height = 0
		self.projection_image_pillarboxing_width = 0
		self.projection_image_letterboxing_height = 0
		self.projection_width = 1280
		self.projection_height = 720
		self.image_display_width = 0
		self.image_display_height = 0
		
		## storage data
		self._file_name = ""
		self._path = ""

		## store file name and path
		self.file_name = os.path.split(full_path_and_file)[1]
		self.path = os.path.split(full_path_and_file)[0]
		
		## internal image data types
		self.pillow_image = PIL.Image.open(os.path.join(self.path, self.file_name))
		self.cv_image = cv2.imread(os.path.join(self.path, self.file_name))
		
		## width, height, and width-to-height ratio (to determine letterbox or pillarbox)
		shape = self.cv_image.shape
		self.image_width = shape[1]
		self.image_height = shape[0]
		self.ratio_flag = ""
		self.set_ratio()
		
		## put the first image in the newly-loaded series on display in the player
		self.image_4_display = self.build_image_4_display()

	'''
	calculate_image_display_size()
	Calculate the size of the displayed image based on whether it's
	in letterbox or pillarbox format. The final image will fit on the 
	display canvas, but will retain it's original aspect ratio.
	The display canvas has a 16:9 ratio, but these calculations
	will resize any other aspect ratio to fit either the full height
	in pillarbox mode or the full width in letterbox.
	See build_image_4_display() below for more info.
	'''
	def calculate_image_display_size(self):
		image_width, image_height = self.dimensions
		image_ratio = self.image_width / self.image_height
		projection_ratio = self.projection_width / self.projection_height

		if image_ratio > projection_ratio: ## image is wider than 16:9
			factor = self.image_width / self.projection_width
			image_display_width = int(self.image_width / factor)
			image_display_height = int(self.image_height / factor)
		elif image_ratio < projection_ratio: ## image is narrower than 16:9
			factor = self.image_height / self.projection_height
			image_display_width = int(self.image_width / factor)
			image_display_height = int(self.image_height / factor)
		else: ## image is exactly 16:9 (must be HDTV)
			factor = self.image_height / self.projection_height
			image_display_width = int(self.image_width / factor)
			image_display_height = int(self.image_height / factor)
			
		return (image_display_width, image_display_height)
		
	def build_image_4_display(self):
		## dimensions
		canvas_width = self.ap_settings.canvas_width
		canvas_height = self.ap_settings.canvas_height
		image_width, image_height = self.dimensions
		projection_index = self.ap_settings.projection
		resolution = screen_resolutions["720p"][projection_index]
		self.projection_width = resolution["projection width"]
		self.projection_height = resolution["projection height"]
		
		## offsets
		projection_h_offset = resolution["h_offset"]
		projection_v_offset = resolution["v_offset"]
		self.image_display_width, self.image_display_height = self.calculate_image_display_size()
		image_h_offset = int(projection_h_offset + ((self.projection_width - self.image_display_width) / 2))
		image_v_offset = int(projection_v_offset + ((self.projection_height - self.image_display_height) / 2))
		
		## the canvas background & image layers
		canvas_composite = PIL.Image.new("RGB", (canvas_width, canvas_height), color = 'black')
		checkerboard = Checkerboard(canvas_width, canvas_height, self.ap_settings.checkerboard_colours)
		projection_background = PIL.Image.new("RGB", (self.projection_width, self.projection_height), color = 'black')
		resized_original = self.pillow_image.resize((self.image_display_width, self.image_display_height))

		## combine layers on canvas
		canvas_composite.paste(checkerboard, (0, 0))
		canvas_composite.paste(projection_background, (int(projection_h_offset), int(projection_v_offset)))
		canvas_composite.paste(resized_original, (image_h_offset, image_v_offset))
		
		## make it easily accessible from elsewhere
		self.image_4_display = PIL.ImageTk.PhotoImage(canvas_composite)

	'''
	- get the original width and height of the image
	- get resolution from settings (8k, 4k, 2k, 1080p, 720p)
	- get the width and height of resolution from ap_screen_resolutions.py
	- get the projection ratio from settings
	- calculate the size of projection_ratio that will fit resolution
	- create a black rectangle
	- scale the image to fit projection_ratio
	- create composite image
	- add projection rectangle to composite
	- add image to composite
	- assign final composite to self.image_4_video
	'''
	def build_image_4_video(self):
		pass
		
	@property
	def pillow_image(self):
		return self._pillow_image
	
	@pillow_image.setter
	def pillow_image(self, value):
		if value:
			self._pillow_image = value
		
	@property
	def image_4_display(self):
		return self._image_4_display
	
	@image_4_display.setter
	def image_4_display(self, value):
		## we don't use any() here because a TKImage isn't a data array
		if value:
			self._image_4_display = value
		
	@property
	def cv_image(self):
		return self._cv_image
		
	@cv_image.setter
	def cv_image(self, value):
		## We use any() here because a CV image is a data array
		if value.any():
			self._cv_image = value

	@property
	def file_name(self):
		return self._file_name
		
	@file_name.setter
	def file_name(self, value):
		if type(value) == str:
			self._file_name = value
		else:
			pass ## error condition?

	@property
	def path(self):
		return self._path
		
	@path.setter
	def path(self, value):
		if type(value) == str:
			self._path = value
		else:
			pass ## error condition?

	@property
	def full_path(self):
		return self._path + "/" + self._file_name

	@property
	def dimensions(self):
		return (self.image_width, self.image_height)
	
	## ratio_flag
	## can be either "pillarbox" or "letterbox"
	@property
	def ratio_flag(self):
		return self._ratio_flag
	
	@ratio_flag.setter
	def ratio_flag(self, value):
		if type(value) == str:
			self._ratio_flag = value
			
	'''
	set_ratio()
	Given the width and height of the image, returns
	a flag indicating whether it should be letterboxed
	or pillarboxed.
	If the result of the test is 1.78 or less,
	we know the ratio is narrower than UHD (16:9), so
	the flag will be set to "pillarbox". If it's 1.781
	or more, the format is wider than UHD, so it'll be set
	to "letterbox".
	'''
	def set_ratio(self):
		##- subtract height from width:
		difference = self.image_width / self.image_height
		## ic("difference: ", difference)
		
		if difference < 1.78:
			self.ratio_flag = "pillarbox"
			## ic(self.ratio_flag)
		else:
			self.ratio_flag = "letterbox"
			## ic(self.ratio_flag)
		
		## ic(self.ratio_flag)

	def config_projection(self):
		if self.ratio_flag == "pillarbox":
			pass 
		pass

	def resize(self):
		pass
		
	def crop(self):
		pass
	
	def flip_horizontal(self):
		pass
	
	def flip_vertical(self):
		pass
	
	def denoise(self):
		pass
	
	def restore(self): ## inpaint
		pass
		
## testing
if __name__ == "__main__":
	window = Tk() ## this has to be here or PIL's TkImage won't work
	canvas = Canvas(window, width = 1920, height = 1080)
	canvas.pack()
	## load an image
	image_file_name = "D:/Documents/Programming/PythonCode/tkinter/animators_pal/images HD/Lisa_seq_01_0000.png"
	my_ap_image = APImage(image_file_name)
	
	## ic(my_ap_image.file_name)
	## ic(my_ap_image.path)
	## ic(my_ap_image.width, my_ap_image.height)
	#my_ap_image.convert_cv_to_tk()
	## ic(my_ap_image.image_4_display.width(), my_ap_image.image_4_display.height())
	## ic(type(my_ap_image.image_4_display))
	canvas.create_image(0, 0, anchor = "nw", image = my_ap_image.image_4_display)
	window.mainloop()
