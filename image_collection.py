'''
Image Collection
The images (actually, image data) in this collection
is ready to animate and/or render to a video file.
'''

from PIL import Image, ImageTk
from tkinter import Tk ## This must be limited so we don't replace PIL's Image class
from tkinter import Canvas

## local
from image_ap import APImage

class TKImageCollection():
	_images = {} ## dictionary of CVImage data (NOT CVImage objects)
					## using the filenames as keys, the data as values
	
	@property
	def images(self):
		return self._images
		
	def __init__(self):
		pass
		
	def add(self, image_name: str, data: ImageTk.PhotoImage):
		self._images[image_name] = data
		
	def remove(self, image_name: str, data: ImageTk.PhotoImage):
		pass
	
	def sort(self):
		pass
	
	def reorder(self):
		pass
	
	def show_thumbnail(self):
		pass
	
	def show_list(self):
		pass

## testing
if __name__ == "__main__":
	## initialize window and canvas
	window = Tk()
	canvas = Canvas(window, width = 1280, height = 720)
	canvas.pack()
	## initialize the collection
	image_collection = TKImageCollection()
	images = {}
	
	for i in range(8):
		file_name = f"image_sequence/Lisa_seq_01_{i:04d}.png"
		image = APImage(file_name)
		## convert it...
		image.convert_cv_to_tk()
		## add the image to the frame list
		image_collection.add(file_name, image.tk_image_data)
		
	for j in image_collection.images:
		print(j)
	