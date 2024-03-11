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

	colour = "black"
	
	def __init__(self, parent):
		## attributes
		self.thumbnail_image = None
		self.ratio_flag = ""
		self.new_width = 0
		self.new_height = 0
		self.target_width = 384
		self.target_height = 216
		## configure
		super().__init__(parent)
		self.parent = parent
		self.image_collection = TKImageCollection()
		## population
		self.config(bg = self.colour, width = self.target_width, height = self.target_height)
		self.canvas = Canvas(self, width = self.target_width, height = self.target_height)

	def set_ratio_type(self, width, height):
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
		difference = width / height
		print("difference: ", difference)
		
		if difference < 1.78:
			self.ratio_flag = "pillarbox"
			print("self.ratio_flag: ", self.ratio_flag)
		else:
			self.ratio_flag = "letterbox"
			print("self.ratio_flag: ", self.ratio_flag)
		
		return ratio_flag

	def set_final_image_size(self, image_width, image_height):
		if self.ratio_flag == "letterbox":
			self.new_width = self.target_width
			divisor = width / self.target_width ## always assume we're downsizing
			self.new_height = int(image_height / divisor)
		elif self.ratio_type == "pillarbox":
			self.new_height = self.target_height
			divisor = image_height / self.target_height
			self.new_width = int(image_width / divisor)
		else:
			pass
		
		print("self.new_width: ", self.new_width, ", self.new_height: ", self.new_height)

	def set_image_placement(self):
		if self.new_height == self.target_height: ## pillarbox mode
			self.pillars = (self.target_width - self.new_width) / 2
			self.letters = 0
		elif self.new_width == self.target_width: ## letterbox mode
			self.letters = (self.target_height - self.new_height) / 2
			self.pillars = 0
		
		print("image will be offset horizontally by: ", self.pillars, " pixels and vertically by ", self.letters, " pixels.")

	def resize_image_to_thumbnail(self):
		'''
		Somewhere before this point, we need to get the pillow image data
		from the APImage object so we can use it as the raw data to base
		the thumbnail on.
		'''
		newsize = (self.new_width, self.new_height)
		pillow_image_data = pillow_image_data.resize(newsize)
		
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
