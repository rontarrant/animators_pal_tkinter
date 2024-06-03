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

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class APImage():
	def __init__(self, full_path_and_file):
		## instance variables
		self._pillow_image = None
		self._tk_image = None
		self._cv_image = None
		self._file_name = ""
		self._path = ""
		## store file name and path
		self.file_name = os.path.split(full_path_and_file)[1]
		self.path = os.path.split(full_path_and_file)[0]
		## image data types
		self.pillow_image = Image.open(os.path.join(self.path, self.file_name))
		self.cv_image = cv2.imread(os.path.join(self.path, self.file_name))
		self.tk_image = ImageTk.PhotoImage(self.pillow_image.resize((1280, 720)))
		## image specifications
		shape = self.cv_image.shape
		self.width = shape[1]
		self.height = shape[0]
		self.ratio_flag = ""
		self.set_ratio()
		## ic(self.width, self.height, self._ratio_flag)
	
	@property
	def pillow_image(self):
		return self._pillow_image
	
	@pillow_image.setter
	def pillow_image(self, value):
		if value:
			self._pillow_image = value
		
	@property
	def tk_image(self):
		return self._tk_image
	
	@tk_image.setter
	def tk_image(self, value):
		## we don't use any() here because a TKImage isn't a data array
		if value:
			self._tk_image = value
		
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
	## ic(my_ap_image.tk_image.width(), my_ap_image.tk_image.height())
	## ic(type(my_ap_image.tk_image))
	canvas.create_image(0, 0, anchor = "nw", image = my_ap_image.tk_image)
	window.mainloop()
