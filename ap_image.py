'''
ap_image.py
A class containing an image read by opencv.
Properties are:
	- file name,
	- path,
	- image data,
	- dimensions, and
	-	a list of special effects that are to be applied
		to the image before rendering the final video.
		
Special FX may consist of:
	- resize (v. 2),
	- crop (v. 2),
	- denoise (v. 3),
	- flip horizontal (v. 3),
	- flip vertical (v. 2), and/or
	- inpaint (restore) (v. 2).
'''

'''
TODO:
	Somehow, the display_image isn't being resized to fit 1280x720.
	Start by printing the sizes at various stages.
'''
import os
import cv2
import sys ## for testing only
from PIL import Image, ImageTk
from tkinter import Tk ## This must be limited so we don't replace PIL's Image class
from tkinter import Canvas

## local

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class APImage():
	def __init__(self, full_path_and_file):
		## image data
		self._pillow_image = None
		self._display_image = None
		self._cv_image = None
		self.pillars = 0
		self.letters = 0
		self.canvas_width = 1280
		self.canvas_height = 720
		self.display_width = 0
		self.display_height = 0
		## storage data
		self._file_name = ""
		self._path = ""
		## store file name and path
		self.file_name = os.path.split(full_path_and_file)[1]
		self.path = os.path.split(full_path_and_file)[0]
		## internal image data types
		self.pillow_image = Image.open(os.path.join(self.path, self.file_name))
		self.cv_image = cv2.imread(os.path.join(self.path, self.file_name))
		## width, height, and width-to-height ratio (to determine letterbox or pillarbox)
		shape = self.cv_image.shape
		self.width = shape[1]
		self.height = shape[0]
		self.ratio_flag = ""
		self.set_ratio()
		## put the first image in the newly-loaded series on display in the player
		self.display_image = self.image_display()

	'''
	Calculate the size of the displayed image based on whether it's
	in letterbox or pillarbox. The final image will fit on the 
	display canvas, but will retain it's original aspect ratio.
	The display canvas has a 16:9 ratio, but these calculations
	will resize any other aspect ratio to fit either the full height
	in pillarbox mode or the full width in letterbox.
	See image_display() below for more info.
	'''
	def calculate_display_size(self, image_width, image_height):
		if self.ratio_flag == "letterbox":
			self.display_width = self.canvas_width
			divisor = image_width / self.canvas_width ## always assume we're downsizing
			self.display_height = int(image_height / divisor)
		elif self.ratio_flag == "pillarbox":
			self.display_height = self.canvas_height
			divisor = image_height / self.canvas_height
			self.display_width = int(image_width / divisor)
		else:
			## ic()
			pass

	def set_image_placement(self):
		if self.display_height == self.canvas_height: ## pillarbox mode
			self.pillars = (self.canvas_width - self.display_width) / 2
			self.letters = 0
		elif self.display_width == self.canvas_width: ## letterbox mode
			self.letters = (self.canvas_height - self.display_height) / 2
			self.pillars = 0

	def image_display(self):
		## get the original width and height of the image
		image_width, image_height = self.dimensions
		
		self.calculate_display_size(image_width, image_height)
		resized_original = self.pillow_image.resize((self.display_width, self.display_height))
		## set placement of the image within the black background
		self.set_image_placement()
		##- overlay image onto black rectangle for pillarbox or letterbox effect
		composite_image = Image.new("RGB", (self.canvas_width, self.canvas_height), color = 'black')
		composite_image.paste(resized_original, (int(self.pillars), int(self.letters)))
		self.display_image = ImageTk.PhotoImage(composite_image)

	@property
	def pillow_image(self):
		return self._pillow_image
	
	@pillow_image.setter
	def pillow_image(self, value):
		if value:
			self._pillow_image = value
		
	@property
	def display_image(self):
		return self._display_image
	
	@display_image.setter
	def display_image(self, value):
		## we don't use any() here because a TKImage isn't a data array
		if value:
			self._display_image = value
		
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
	def width(self):
		return self._width
		
	@width.setter
	def width(self, value):
		if type(value) == int:
			self._width = value
			
	@property
	def dimensions(self):
		return (self.width, self.height)
	
	## ratio_flag
	## can be either "pillarbox" or "letterbox"
	@property
	def ratio_flag(self):
		return self._ratio_flag
	
	@ratio_flag.setter
	def ratio_flag(self, value):
		if type(value) == str:
			self._ratio_flag = value
			
	def set_ratio(self):
		'''
		Given the width and height of the image, returns
		a flag indicating whether it should be letterboxed
		or pillarboxed.
		If the result of the test is 1.78 or less,
		we know the ratio is narrower than UHD (16:9), so
		the flag will be set to "pillarbox". If it's 1.781
		or more, the format wider than UHD, so it'll be set
		to "letterbox".
		'''
		##- subtract height from width:
		difference = self.width / self.height
		## ic("difference: ", difference)
		
		if difference < 1.78:
			self.ratio_flag = "pillarbox"
			## ic(self.ratio_flag)
		else:
			self.ratio_flag = "letterbox"
			## ic(self.ratio_flag)
		
		## ic(self.ratio_flag)

	def config_resolution(self):
		##- configure resolution (8k, 4k, 2k, HD, etc.)
		##	a) if pillar flag set, check height against available resolutions
		##		pick the one whose height is closest, but not more than the image
		if self.ratio_flag == "pillarbox":
			pass 
		##	b) if letter flag is set, check width against available resolutions
		##		pick the one whose width is closest, but not more than the image
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
	image_file_name = "D:/Documents/Programming/PythonCode/tkinter/animators_pal/image_sequence/Lisa_seq_01_0000.png"
	my_ap_image = APImage(image_file_name)
	
	## ic(my_ap_image.file_name)
	## ic(my_ap_image.path)
	## ic(my_ap_image.width, my_ap_image.height)
	#my_ap_image.convert_cv_to_tk()
	## ic(my_ap_image.display_image.width(), my_ap_image.display_image.height())
	## ic(type(my_ap_image.display_image))
	canvas.create_image(0, 0, anchor = "nw", image = my_ap_image.display_image)
	window.mainloop()
