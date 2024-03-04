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

class APImage():

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
	def dimensions(self):
		return (self._width, self._height)
	
	@dimensions.setter
	def dimensions(self, value):
		self._width = value[1]
		self._height = value[0]
		self._channels = value[2]

	def __init__(self, full_path_and_file):
		## instance variables
		_file_name: str = []
		_path: str = [] ## file location
		_cv_image_data = None
		_tk_image_data = None
		_width: int = None
		_height: int = None
		_sfx: str = [] ## list of SFX to do before adding this image to video
		## set up
		self.file_name = os.path.split(full_path_and_file)[1]
		self.path = os.path.split(full_path_and_file)[0]
		self.cv_image_data = cv2.imread(os.path.join(self.path, self.file_name))
		shape = self.cv_image_data.shape
		self.width = shape[1]
		self.height = shape[0]
	
	def convert_cv_to_tk(self):
		## reverse order of colour channels
		blue, green, red = cv2.split(self._cv_image_data) 
		image_rgb = cv2.merge((red, green, blue))
		pillow_image_data = Image.fromarray(image_rgb)
		## and convert to TkImage
		self._tk_image_data = ImageTk.PhotoImage(pillow_image_data)
		
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
	
	print("my_ap_image.file_name: ", my_ap_image.file_name)
	print("my_ap_image.path: ", my_ap_image.path)
	print("width: ", my_ap_image.width, ", height: ", my_ap_image.height)
	my_ap_image.convert_cv_to_tk()
	print("tk_image_data size: ", my_ap_image.tk_image_data.width(), ", ", my_ap_image.tk_image_data.height())
	print("my_ap_image.tk_image_data type: ", type(my_ap_image.tk_image_data))
	canvas.create_image(0, 0, anchor = "nw", image = my_ap_image.tk_image_data)
	window.mainloop()
