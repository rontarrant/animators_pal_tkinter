'''
cv_image.py
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

class CVImage():
	_file_name: str = []
	_path: str = [] ## file location
	_image_data = None
	_width: int = None
	_height: int = None
	_sfx: str = [] ## list of SFX to do before adding this image to video

	@property
	def image_data(self):
		return self._image_data
		
	@image_data.setter
	def image_data(self, value):
		if value.any():
			self._image_data = value

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
		self.file_name = os.path.split(full_path_and_file)[1]
		self.path = os.path.split(full_path_and_file)[0]
		self.image_data = cv2.imread(os.path.join(self.path, self.file_name))
		shape = self.image_data.shape
		self.width = shape[1]
		self.height = shape[0]
	
## testing
if __name__ == "__main__":
	image_file_name = "D:/Documents/Programming/PythonCode/tkinter/animators_pal/research/image_sequence/Lisa_Turnaround_1920x1080_0000.png"
	my_cv_image = CVImage(image_file_name)
	print("my_cv_image.file_name: ", my_cv_image.file_name)
	print("my_cv_image.path: ", my_cv_image.path)
	print("width: ", my_cv_image.width, ", height: ", my_cv_image.height)
	print("image_data: ", my_cv_image.image_data)
