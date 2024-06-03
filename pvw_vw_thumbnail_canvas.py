'''
ThumbnailCanvas
Displays a TKImage selected in the Treeview (and stored in APImageCollection)
as a thumbnail. 
'''

from tkinter import *
from tkinter.ttk import *

## local
from ap_image_collection import APImageCollection
from PIL import Image, ImageTk

class ThumbnailCanvas(Canvas):

	colour = "gray"
	
	def __init__(self, parent):
		## attributes
		self.thumbnail_image = None
		self.pillow_thumbnail_image = None
		self.ratio_flag = ""
		self.thumb_width = 0 ## used during calculation of size
		self.thumb_height = 0 ## used during calculation of size
		self.pillars = 0
		self.letters = 0
		self.target_width = 384
		self.target_height = 216
		## configure
		super().__init__(parent, width = self.target_width, height = self.target_height, bg = self.colour)
		self.parent = parent
		self.image_collection = APImageCollection.get_instance()
		self.config(width = self.target_width, height = self.target_height)
		## population
		self.grid()

	'''
	Calculate the size of the thumbnail based on whether it's
	in letterbox or pillarbox. The final image will fit on the 
	thumbnail canvas, but will retain it's original aspect ratio.
	The thumbnail canvas has a 16:9 ratio, but these calculations
	will resize any other aspect ratio to fit either the full height
	in pillarbox mode or the full width in letterbox.
	See preview_thumbnail() below for more info.
	'''
	def set_thumbnail_size(self, image_width, image_height):
		if self.ratio_flag == "letterbox":
			self.thumb_width = self.target_width
			divisor = width / self.target_width ## always assume we're downsizing
			self.thumb_height = int(image_height / divisor)
		elif self.ratio_flag == "pillarbox":
			self.thumb_height = self.target_height
			divisor = image_height / self.target_height
			self.thumb_width = int(image_width / divisor)
		else:
			## ic()
			pass
		
		## ic(self.thumb_width, self.thumb_height)

	def set_image_placement(self):
		if self.thumb_height == self.target_height: ## pillarbox mode
			self.pillars = (self.target_width - self.thumb_width) / 2
			self.letters = 0
		elif self.thumb_width == self.target_width: ## letterbox mode
			self.letters = (self.target_height - self.thumb_height) / 2
			self.pillars = 0
		
		## ic(self.pillars, self.letters)

	def preview_thumbnail(self, image_number):
		## ic(image_number)
		
		## In the collection, find the image we want to thumbnail.
		image = self.image_collection.images[image_number]
		## ic(image.full_path)
		
		## get the width and height of the image
		image_width, image_height = image.dimensions
		## ic(image_width, image_height)
		## get the ratio flag
		self.ratio_flag = image.ratio_flag
		## ic(self.ratio_flag)
		
		##- resize the image to fit within a 384x216 (thumbnail size) canvas
		self.set_thumbnail_size(image_width, image_height)
		## set placement of the image within the black background
		self.set_image_placement()
		##- overlay image onto black rectangle for pillarbox or letterbox effect
		## ic(self.thumb_width, self.thumb_height)
		self.pillow_thumbnail_image = image.pillow_image.resize((self.thumb_width, self.thumb_height))
		## ic(self.pillow_thumbnail_image)
		self.thumbnail_image = ImageTk.PhotoImage(self.pillow_thumbnail_image)
		## ic(self.thumbnail_image)
		self.create_rectangle(0, 0, 384, 216, fill = "black")
		self.create_image(self.pillars, self.letters, anchor = 'nw', image = self.thumbnail_image)

		
## testing
if __name__ == "__main__":
	image_collection = APImageCollection()
	window = Tk()
	window.configure(width = 1280, height = 840)
	thumb = ThumbnailCanvas(window)
	thumb.pack()
	window.mainloop()
