'''
Video Controls
The usual controls for video... play, stop, pause, etc. 
'''

from tkinter import *
#from tkinter.ttk import *

## local
from fr_video_canvas import VideoCanvas

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class ImageButton(Button):
	## These can be class variables because only one
	## button image is swapped at a given instant in time
	## and button image refresh takes care of itself.
	unclicked_swap_image = None
	clicked_swap_image = None
	unclicked_image = None
	clicked_image = None
	swapable = False ## does the button have swap images
	swapped = False ## track the state of swapped/unswapped
	
	def __init__(self, parent, up_image, down_image, swap_on = None, swap_off = None, *args, **kwargs):
		### ic(up_image, down_image)
		if swap_on != None and swap_off != None:
			### ic(swap_on, swap_off)
			self.unclicked_swap_image = PhotoImage(file = swap_off)
			self.clicked_swap_image = PhotoImage(file = swap_on)
			self.unclicked_image = PhotoImage(file = up_image)
			self.clicked_image = PhotoImage(file = down_image)
			self.unclickedImage = PhotoImage(file = up_image)
			self.clickedImage = PhotoImage(file = down_image)
			self.swapable = True
		else:
			self.unclickedImage = PhotoImage(file = up_image)
			self.clickedImage = PhotoImage(file = down_image)
			self.swapable = False
			
		super().__init__(parent, *args, image = self.unclickedImage, **kwargs)
		self.toggleState = 1
		self.bind("<Button-1>", self.clickFunction)
			
	def swapable_image(self, event = None):
		self.swapable = True
		
	def clickFunction(self, event = None):
		ic()
		if self.swapable == True:
			if self.swapped == False: ## we're in an unswapped state; change to swapped state
				### ic("swapped = True... swapping images")
				self.swapped = True
				self.unclickedImage = self.unclicked_swap_image
				self.clickedImage = self.clicked_swap_image
			else:
				### ic("swapped = False")
				self.swapped = False
				self.unclickedImage = self.unclicked_image
				self.clickedImage = self.clicked_image
			
		if self.cget("state") != "disabled": #Ignore click if button is disabled
			self.toggleState *= -1
			
			if self.toggleState == -1:
				self.config(image = self.clickedImage)
			else:
				self.config(image = self.unclickedImage)

class VideoControlsFrame(Frame):
	colour = "CadetBlue1"
	goto_start_button = None
	step_backward_button = None
	play_button = None
	play_reverse_button = None
	stop_button = None
	step_forward_button = None
	goto_end_button = None
	loop_button = None
	
	## The button callbacks are passed a pointer to the VideoCanvas
	## so the buttons can act directly on the VideoCanvas for
	## stopping, playing, reversing, pausing, etc.
	def __init__(self, parent, canvas):
		super().__init__(parent)
		## instance variables
		self.parent = parent
		self.configure(width = 1280, height = 72)
		self.grid(sticky = (N, E, W, S))
		self.grid_columnconfigure(0, weight = 1)
		self.grid_columnconfigure(9, weight = 1)
		## so we can pass the canvas object into the button callbacks
		## BUTTON IMAGES
		# goto start
		self.goto_start_button = ImageButton(self, "images/goto_start_up.png", "images/goto_start_down.png")
		# step backward
		self.step_backward_button = ImageButton(self, "images/step_backward_up.png", "images/step_backward_down.png")
		# play reverse/pause button
		pause_image_up = "images/pause_up.png"
		pause_image_down = "images/pause_down.png"
		play_reverse_image_up = "images/play_reverse_up.png"
		play_reverse_image_down = "images/play_reverse_down.png"
		self.play_reverse_button = ImageButton(self, play_reverse_image_up, play_reverse_image_down, swap_on = pause_image_up, swap_off = pause_image_down)
		# stop
		self.stop_button = ImageButton(self, "images/stop_up.png", "images/stop_down.png")
		# play forward/pause button
		play_image_up = "images/play_up.png"
		play_image_down = "images/play_down.png"
		self.play_button = ImageButton(self, play_image_up, play_image_down, swap_on = pause_image_up, swap_off = pause_image_down)
		# step forward
		self.step_forward_button = ImageButton(self, "images/step_forward_up.png", "images/step_forward_down.png")
		# goto end
		self.goto_end_button = ImageButton(self, "images/goto_end_up.png", "images/goto_end_down.png")
		# loop on/off
		loop_image_up = "images/loop_off_up.png"
		loop_image_down = "images/loop_off_down.png"
		loop_image_swap_up = "images/loop_on_up.png"
		loop_image_swap_down = "images/loop_on_down.png"
		self.loop_button = ImageButton(self, loop_image_up, loop_image_down, swap_on = loop_image_swap_up, swap_off = loop_image_swap_down)
		
		## LAYOUT
		self.goto_start_button.grid(row = 0, column = 1, padx = 5)
		self.step_backward_button.grid(row = 0, column = 2, padx = 5)
		self.play_reverse_button.grid(row = 0, column = 3, padx = 5)
		self.stop_button.grid(row = 0, column = 4, padx = 5)
		self.play_button.grid(row = 0, column = 5, padx = 5)
		self.step_forward_button.grid(row = 0, column = 6, padx = 5)
		self.goto_end_button.grid(row = 0, column = 7, padx = 5)
		self.loop_button.grid(row = 0, column = 8, padx = 5)
		
		## BUTTON BINDINGS
		self.goto_start_button.bind("<Button-1>", lambda event: self.goto_start_callback(canvas))
		self.step_backward_button.bind("<Button-1>", lambda event: self.step_backward_callback(canvas))
		self.play_reverse_button.bind("<Button-1>", lambda event: self.play_reverse_pause_callback(canvas), add = "+")
		self.stop_button.bind("<Button-1>", lambda event: self.stop_callback(canvas))
		self.play_button.bind("<Button-1>", lambda event: self.play_pause_callback(canvas), add = "+")
		self.step_forward_button.bind("<Button-1>", lambda event: self.step_forward_callback(canvas))
		self.goto_end_button.bind("<Button-1>", lambda event: self.goto_end_callback(canvas))
		self.loop_button.bind("<Button-1>", lambda event: self.loop_switch(canvas), add = "+")

	def goto_start_callback(self, canvas, *args, **kwargs): ## goes to first frame
		ic()
		canvas.status[0] = canvas.STOP
		canvas.frame_num = 0
		canvas.show_next_frame()
		
	def step_backward_callback(self, canvas, *args, **kwargs): ## goes back one frame
		ic()
		canvas.status[0] = canvas.STOP
		
		if canvas.frame_num > 0:
			canvas.frame_num -= 1
			
		canvas.show_next_frame()

	def play_reverse_pause_callback(self, canvas, *args, **kwargs): ## plays video in reverse at normal speed; pauses at current frame
		ic()
		canvas.status[0] = canvas.REVERSE
		canvas.last_button = self.play_reverse_button
		canvas.show_next_frame()
	
	def stop_callback(self, canvas, *args, **kwargs): ## stops video, rewinds to first frame
		ic()
		## If the Pause button is visible, this should swap it back to the Play button.
		if self.play_button.swapped == True:
			self.play_button.clickFunction()
		elif self.play_reverse_button.swapped == True:
			self.play_reverse_button.clickFunction()
			
		canvas.status[0] = canvas.STOP
		canvas.frame_num = 0
		canvas.show_next_frame()
	
	def play_pause_callback(self, canvas, *args, **kwargs): ## plays video at normal speed; pauses at current frame
		canvas.status[0] = canvas.FORWARD
		canvas.last_button = self.play_button
		canvas.show_next_frame()
		ic(self.play_button)
	
	def step_forward_callback(self, canvas, *args, **kwargs): ## goes forward one frame
		ic()

		canvas.status[0] = canvas.STOP
		
		if canvas.frame_num < len(canvas.image_collection.images) - 1:
			canvas.frame_num += 1
			
		canvas.show_next_frame()
	
	def goto_end_callback(self, canvas, *args, **kwargs): ## goes to last frame
		ic()
		canvas.status[0] = canvas.STOP
		canvas.frame_num = len(canvas.image_collection.images) - 1
		canvas.show_next_frame()
	
	def loop_switch(self, canvas, *args, **kwargs): ## turns on/off looping
		ic("")
		canvas.status[1] = not self.status[1]
		print(args)

## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 840)
	video_canvas = VideoCanvas(window)
	video_controls = VideoControlsFrame(window, video_canvas)
	video_canvas.grid(row = 0)
	video_controls.grid(row = 1)
	window.mainloop()
