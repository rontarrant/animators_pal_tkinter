'''
Video Canvas
Displays a flipbook of TKImages collected in a APImageCollection. 
'''

from tkinter import *
from tkinter.ttk import *

## local
from image_collection import APImageCollection
from image_ap import APImage

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class VideoCanvas(Canvas):
	## constants
	REVERSE = -1 ## play backwards
	FORWARD = 1 ## play forward
	PAUSE = 2
	STOP = 0 ## halt playback and goto start frame
	LOOP_ON = True
	LOOP_OFF = False
	status = [STOP, LOOP_OFF] ## default
	## defaults
	frame_num = 0
	looping_status = LOOP_OFF
	fps: int = 24 ## can also be 18, 25, or 30
	delay: int = 0
	shoot_on: int = 1 ## 1's, 2's, 3's up to 9's
	width: int = 1280 ## default: HD
	height: int = 720 ## default: HD
	colour = "Black"
	direction: int = 1 ## default: forward (-1 = reverse)
	first_frame_hold: int = 1 ## valid: 1 to 90
	last_frame_hold: int = 1 ## valid: 1 to 90
	image_collection = APImageCollection()
	last_button = None ## which button was last pressed (let's us restore the
							 ## default image if loop is turned off)

	def __init__(self, parent):
		self.parent = parent
		## instantiation
		super().__init__(parent)
		## configure
		self.config(bg = self.colour, width = self.width, height = self.height)
		self.delay = self.fps2ms(self.fps)

	'''
	Recursive... takes the next frame as its argument.
	When called with 0, starts with the first frame.
	- LOOP_ON = True ## looping is on
	- LOOP_OFF = False ## looping is off
	The variable 'status' is a tuple:
	- status[0] = direction of play
		- FORWARD = 1 ## play forward
		- REVERSE = -1 ## play backwards
	- status[1] = looping on or off
	Because only playback is time-critical, all other actions
	are handled directly by the button callbacks.
	'''
	def fps2ms(self, fps):
		value = int(round(1000 / fps))
		
		return value

	def show_next_frame(self, frame_num):
		match self.status:
			case (self.FORWARD, self.LOOP_OFF):
				self.delete("all")

				if frame_num == len(self.image_collection.images) - 1: ## If we hit the last frame, stop and rewind to frame 001
					self.status[0] = self.STOP
					self.frame_num = frame_num ## remember the last frame displayed (NOTE: may want to jump back to the beginning)
					self.last_button.change_button_image()
					## need to switch the callback from pause_callback() to play_callback()
					self.last_button = None
					self.show_next_frame(frame_num)
					ic("we're done: ", frame_num, self.frame_num, self.status)
				else:                                                  ## otherwise, go to the next frame
					self.create_image(0, 0, anchor = "nw", image = self.image_collection.images[frame_num].tk_image) 
					self.winfo_toplevel().after(self.delay, self.show_next_frame, (frame_num + 1) % len(self.image_collection.images))
					ic("go to next frame: ", frame_num, self.frame_num, self.status)
					
			case (self.REVERSE, self.LOOP_OFF):
				self.delete("all") 
				
				if frame_num == 0:
					self.status[0] = self.STOP
					self.frame_num = frame_num ## remember the last frame displayed
					self.last_button.change_button_image()
					self.show_next_frame(frame_num)
				else:
					self.create_image(0, 0, anchor = "nw", image = self.image_collection.images[frame_num].tk_image) 
					self.winfo_toplevel().after(self.delay, self.show_next_frame, (frame_num - 1) % len(self.image_collection.images))
				
				if frame_num == 0:
					# ic("beginning of images")
					self.status[0] = self.STOP
									
			case (self.FORWARD, self.LOOP_ON):

				self.delete("all") 
				self.create_image(0, 0, anchor = "nw", image = self.image_collection.images[frame_num].tk_image) 
				self.winfo_toplevel().after(self.delay, self.show_next_frame, (frame_num + 1) % len(self.image_collection.images))
				self.last_button.change_button_image()
				# ic()
				
			case (self.REVERSE, self.LOOP_ON):
				self.delete("all") 
				self.create_image(0, 0, anchor = "nw", image = self.image_collection.images[frame_num].tk_image) 
				self.winfo_toplevel().after(self.delay, self.show_next_frame, (frame_num - 1) % len(self.image_collection.images))
				self.last_button.change_button_image()
				# ic()
			
			case (self.PAUSE, self.LOOP_OFF):
				# ic()
				pass
				
			case (self.PAUSE, self.LOOP_ON):
				# ic()
				pass
				
			case _:
				ic("catchall: ", self.status, self.frame_num, frame_num)
				self.delete("all") 
				self.create_image(0, 0, anchor = "nw", image = self.image_collection.images[frame_num].tk_image)

		ic(frame_num, self.frame_num, self.last_button, self.status)

	 
## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 806)
	mainframe = Frame(window)
	mainframe.grid()
	vcanvas = VideoCanvas(mainframe)
	vcanvas.grid(row = 0)
	window.mainloop()
