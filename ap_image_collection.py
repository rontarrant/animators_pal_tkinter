'''
Image Collection - Model (as in Model, View, Controller or Model, View, Presenter)
The images in this collection are ready to animate and/or
render to a video file.
Images are loaded as OpenCV data, then converted to pillow
and tkinter (tk_image) formats. All three are persistent.
'''

from PIL import Image, ImageTk
from tkinter import Tk ## This must be limited so we don't replace PIL's Image class
from tkinter import Canvas

## local
from ap_image import APImage

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

## Because the image list is a class attribute
## this will be the same instance no matter where
## or how often it's instantiated throughout the
## other modules.
class APImageCollection():
	_images = [] ## a list of lists containing file name and data
	
	@property
	def images(self):
		return self._images
		
	def __init__(self):
		pass
		
	def add(self, image):
		## a list of dictionaries
		self._images.append(image)
	
	def list_image_types(self):
		# ic("tk: ", image.tk_image)
		# ic("pillow: ", image.pillow_image)
		# ic("cv: ", image.cv_image)
		pass
		
	def remove(self, image_name: str, data: ImageTk.PhotoImage):
		pass
	
	def sort(self):
		pass
	
	def reorder(self):
		pass
	
	def get_images(self):
		return self.images

	def show_list(self):
		for image in self._images.items():
			# ic(image)
			pass

## testing
if __name__ == "__main__":
	## initialize window and canvas
	window = Tk()
	canvas = Canvas(window, width = 1280, height = 720)
	canvas.pack()
	## initialize the collection
	image_collection = APImageCollection()
	
	for i in range(8):
		file_name = f"image_sequence/Lisa_seq_01_{i:04d}.png"
		image = APImage(file_name)
		## convert it...
		#image.convert_cv_to_tk()
		## add the image to the frame list
		image_collection.add(image)
		
	for j in image_collection.images:
		ic(j)
		pass