'''
Video Canvas
Displays a flipbook of TKImages collected in a APImageCollection. 
'''

from tkinter import *
from tkinter.ttk import *

## local
from ap_image_collection import APImageCollection
from ap_image import APImage
from ap_constants import *
from observer import Observer

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class VideoCanvas(Canvas, Observer):
	## defaults
	width: int = 1280 ## default: HD
	height: int = 720 ## default: HD
	colour = "Black"
	current_frame = 0

	def __init__(self, parent):
		self.parent = parent
		## instantiation
		super().__init__(parent)
		self.ap_image_collection = APImageCollection.get_instance()
		## configure
		self.config(bg = self.colour, width = self.width, height = self.height)

	def show_frame(self, frame_num):
		self.current_frame = frame_num
		##ic(frame_num, self.current_frame)
		'''
		When a frame is drawn, Canvas adds it to a queue.
		Each time a new frame is drawn, canvas draws every
		frame in the queue before drawing the new frame.
		This causes the player to get slower and slower
		because each time it adds a new frame to the queue
		(and subsequently redraws every frame in the queue)
		playback gets slower and slower until it turns into
		a slideshow.
		self.delete(ALL) clears the queue so we get 
		the fastest possible draw time for each frame.
		'''
		self.delete(ALL)
		self.create_image(0, 0, anchor = "nw", image = self.ap_image_collection.images[frame_num].image_4_display)

## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 806)
	mainframe = Frame(window)
	mainframe.grid()
	vcanvas = VideoCanvas(mainframe)
	vcanvas.grid(row = 0)
	window.mainloop()
