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
import os
import cv2
import sys ## for testing only
from PIL import Image, ImageTk
from tkinter import Tk ## This must be limited so we don't replace PIL's Image class
from tkinter import Canvas

## local
from screen_aspect_ratios import *

## ice cream


class APImage():
	def __init__(self, full_path_and_file):
		## instance variables
		## store file name and path
		self.file_name = os.path.split(full_path_and_file)[1]
		self.path = os.path.split(full_path_and_file)[0]
		## image data types
		self.pillow_image = Image.open(os.path.join(self.path, self.file_name))
		self.cv_image_data = cv2.imread(os.path.join(self.path, self.file_name))
		self._tk_image_data = ImageTk.PhotoImage(self.pillow_image)
		## image specifications
		shape = self.cv_image_data.shape
		self.width = shape[1]
		self.height = shape[0]
		self._ratio_flag = ""
		self.set_ratio()
		## ic(self.width, self.height, self._ratio_flag)
	
	@property
	def tk_image_data(self):
		return self._tk_image_data
	
	@tk_image_data.setter
	def tk_image_data(self, value):
		if value.any():
			self._tk_image_data = value
		
	@property
	def cv_image_data(self):
		return self._cv_image_data
		
	@cv_image_data.setter
	def cv_image_data(self, value):
		if value.any():
			self._cv_image_data = value

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
	image_file_name = "D:/Documents/Programming/PythonCode/tkinter/animators_pal/research/image_sequence/Lisa_Turnaround_1920x1080_0000.png"
	my_ap_image = APImage(image_file_name)
	
	## ic(my_ap_image.file_name)
	## ic(my_ap_image.path)
	## ic(my_ap_image.width, my_ap_image.height)
	#my_ap_image.convert_cv_to_tk()
	## ic(my_ap_image.tk_image_data.width(), my_ap_image.tk_image_data.height())
	## ic(type(my_ap_image.tk_image_data))
	canvas.create_image(0, 0, anchor = "nw", image = my_ap_image.tk_image_data)
	window.mainloop()
