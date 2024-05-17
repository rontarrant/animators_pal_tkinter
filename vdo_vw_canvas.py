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

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class VideoCanvas(Canvas):
	status = [AP_STOP, AP_LOOP_OFF] ## default
	## defaults
	frame_num = 0
	looping_status = AP_LOOP_OFF
	fps: int = 24 ## can also be 18, 25, or 30
	delay: int = 0
	shoot_on: int = 1 ## 1's, 2's, 3's up to 9's
	width: int = 1280 ## default: HD
	height: int = 720 ## default: HD
	colour = "Black"
	direction: int = 1 ## default: forward (-1 = reverse)
	first_frame_hold: int = 1 ## valid: 1 to 90
	last_frame_hold: int = 1 ## valid: 1 to 90
	last_button = None ## which button was last pressed (let's us restore the
							 ## default image if loop is turned off)

	def __init__(self, parent):
		self.parent = parent
		## instantiation
		super().__init__(parent)
		self.image_collection = APImageCollection.get_instance()
		## configure
		self.config(bg = self.colour, width = self.width, height = self.height)
		self.delay = self.fps2ms(self.fps)

	def fps2ms(self, fps):
		value = int(round(1000 / fps))
		
		return value

	def show_next_frame(self, frame_num):
		## When a frame is drawn, canvas adds it to a queue.
		## Each time a new frame is drawn, canvas draws every
		## frame in the queue before drawing the new frame.
		## The following line clears the queue so we get 
		## the fastest possible draw time for each frame.
		self.delete(ALL)
		self.create_image(0, 0, anchor = "nw", image = self.image_collection.images[frame_num].tk_image)
		'''
		Keep the following comment until the delay stuff is worked out.
		'''
		# self.winfo_toplevel().after(self.delay, self.show_next_frame, (frame_num + 1) % len(self.image_collection.images))

## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 806)
	mainframe = Frame(window)
	mainframe.grid()
	vcanvas = VideoCanvas(mainframe)
	vcanvas.grid(row = 0)
	window.mainloop()
