'''
Image Thumbnail
Displays a TKImage selected in the Treeview (and stored in TKImageCollection)
as a thumbnail. 
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
		print("image to show: ", image.full_path)
		
		## get the width and height of the image
		width, height = image.dimensions
		print("width: ", width, ", height: ", height)
		## get the ratio flag
		ratio = image.ratio_flag
		print("ratio flag: ", ratio)
		
		##- resize the image to fit within a 384x216 (thumbnail size) canvas
		##- create black rectangle 384x216
		##- place black rectangle on canvas
		##- overlay image onto black rectangle for pillarbox or letterbox effect
		
## testing
if __name__ == "__main__":
	image_collection = TKImageCollection()
	window = Tk()
	window.configure(width = 1280, height = 840)
	thumb = ThumbnailFrame(window)
	thumb.pack()
	window.mainloop()
