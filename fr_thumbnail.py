'''
Image Thumbnail
Displays a TKImages selected in the Treeview and stored in TKImageCollection. 
'''

from tkinter import *
from tkinter.ttk import *

## local
from image_collection import TKImageCollection
from image_ap import APImage

class ThumbnailFrame(Canvas):
	thumbnail_image = None
	colour = "DarkOliveGreen3"
	
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.image_collection = TKImageCollection()
		self.config(bg = self.colour, width = 384, height = 216)
	
	def show_image(self, image_number):
		print("showing image: ", image_number)
		## In the collection, find the image we want to thumbnail.
		image = self.image_collection.images[image_number]
		print("image to show: ", image.path + "/" + image.file_name)
		## get the width and height of the image
		width, height = image.dimensions
		print("width: ", width, ", height: ", height)
		## subtract height from width: 0 or -x = pillar, +x = letter
		## set pillar or letter flag
		## calculate resolution (8k, 4k, 2k, HD, etc.)
		## 	a) if pillar flag set, check height against available resolutions
		##			pick the one whose height is closest, but not more than the image
		##		b) if letter flag is set, check width against available resolutions
		##			pick the one whose width is closest, but not more than the image
		## resize the image to match selected resolution
		## create black rectangle of selected resolution
		## place black rectangle on canvas
		## overlay image onto black rectangle
		
		
## testing
if __name__ == "__main__":
	image_collection = TKImageCollection()
	window = Tk()
	window.configure(width = 1280, height = 840)
	thumb = ThumbnailFrame(window)
	thumb.pack()
	window.mainloop()
