'''
Video Canvas
Displays a flipbook of TKImages collected in a TKImageCollection. 
'''

from tkinter import *
from tkinter.ttk import *

## local
from image_collection import TKImageCollection
from image_ap import APImage

class ThumbnailFrame(Canvas):
	fps: int = 24 ## can also be 18, 25, or 30
	shoot_on: int = 1 ## 1's, 2's, 3's up to 9's
	width: int = 1280 ## default: HD
	height: int = 720 ## default: HD
	colour = "DarkOliveGreen3"
	direction: int = 1 ## default: forward (-1 = reverse)
	first_frame_hold: int = 1 ## anything from 1 to 90
	last_frame_hold: int = 1 ## anything from 1 to 90
	parent = None
	
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.image_collection = TKImageCollection()
		self.config(bg = self.colour, width = 384, height = 216)
	
	def show(self, image):
		pass
## testing
if __name__ == "__main__":
	image_collection = TKImageCollection()
	window = Tk()
	window.configure(width = 1280, height = 840)
	thumb = ThumbnailFrame(window, image_collection)
	thumb.pack()
	window.mainloop()