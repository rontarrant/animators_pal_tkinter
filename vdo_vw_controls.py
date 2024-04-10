'''
Video Controls
The usual controls for video... play, stop, pause, etc. 
'''

from tkinter import *

## local
from vdo_vw_canvas import VideoCanvas
from vdo_vw_image_button import ImageButton

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

class VideoControlsFrame(Frame):
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
	def __init__(self, parent):
		super().__init__(parent)
		## instance variables
		self.parent = parent
		self.configure(width = 1280, height = 72)
		self.grid(sticky = (N, E, W, S))
		self.grid_columnconfigure(0, weight = 1)
		self.grid_columnconfigure(9, weight = 1)
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
		self.play_reverse_button = ImageButton(self, play_reverse_image_up, play_reverse_image_down, alt_image_down = pause_image_up, alt_image_up = pause_image_down)
		# stop
		self.stop_button = ImageButton(self, "images/stop_up.png", "images/stop_down.png")
		# play forward/pause button
		play_image_up = "images/play_up.png"
		play_image_down = "images/play_down.png"
		self.play_button = ImageButton(self, play_image_up, play_image_down, alt_image_down = pause_image_up, alt_image_up = pause_image_down)
		# step forward
		self.step_forward_button = ImageButton(self, "images/step_forward_up.png", "images/step_forward_down.png")
		# goto end
		self.goto_end_button = ImageButton(self, "images/goto_end_up.png", "images/goto_end_down.png")
		# loop on/off
		loop_image_up = "images/loop_off_up.png"
		loop_image_down = "images/loop_off_down.png"
		loop_image_swap_up = "images/loop_on_up.png"
		loop_image_swap_down = "images/loop_on_down.png"
		self.loop_button = ImageButton(self, loop_image_up, loop_image_down, alt_image_down = loop_image_swap_up, alt_image_up = loop_image_swap_down)
		
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
		self.goto_start_button.bind("<ButtonRelease-1>", lambda event: self.goto_start_callback(canvas))
		self.step_backward_button.bind("<ButtonRelease-1>", lambda event: self.step_backward_callback(canvas))
		self.play_reverse_button.bind("<ButtonRelease-1>", lambda event: self.play_reverse_pause_callback(canvas), add = "+")
		self.stop_button.bind("<ButtonRelease-1>", lambda event: self.stop_callback(canvas))
		self.play_button.bind("<ButtonRelease-1>", lambda event: self.play_callback(canvas), add = "+")
		self.step_forward_button.bind("<ButtonRelease-1>", lambda event: self.step_forward_callback(canvas))
		self.goto_end_button.bind("<ButtonRelease-1>", lambda event: self.goto_end_callback(canvas))
		self.loop_button.bind("<ButtonRelease-1>", lambda event: self.loop_switch(canvas), add = "+")

	def goto_start_callback(self, canvas, *args, **kwargs): ## goes to first frame
		## ic()
		canvas.status[0] = canvas.STOP
		canvas.frame_num = 0
		canvas.show_next_frame(canvas.frame_num)
		canvas.last_button = self.goto_start_button
		
	def step_backward_callback(self, canvas, *args, **kwargs): ## goes back one frame
		## ic()
		canvas.status[0] = canvas.STOP
		
		if canvas.frame_num > 0:
			canvas.frame_num -= 1
			
		canvas.show_next_frame(canvas.frame_num)
		canvas.last_button = step_backward_button

	def play_reverse_pause_callback(self, canvas, *args, **kwargs): ## plays video in reverse at normal speed; pauses at current frame
		## ic()
		canvas.status[0] = canvas.REVERSE
		canvas.last_button = self.play_reverse_button
		canvas.show_next_frame(canvas.frame_num)
	
	def stop_callback(self, canvas, *args, **kwargs): ## stops video, rewinds to first frame
		## ic()
		## If the Pause button is visible, this should swap it back to the Play button.
		if self.play_button.swapped == True:
			self.play_button.change_button_image()
		elif self.play_reverse_button.swapped == True:
			self.play_reverse_button.change_button_image()
			
		canvas.status[0] = canvas.STOP
		canvas.frame_num = 0
		canvas.show_next_frame(canvas.frame_num)
		canvas.last_button = self.stop_button
	
	def play_callback(self, canvas, *args, **kwargs): ## plays video at normal speed; pauses at current frame
		# ic("play")
		canvas.status[0] = canvas.FORWARD
		canvas.last_button = self.play_button
		self.play_button.bind("<ButtonRelease-1>", lambda event: self.pause_callback(canvas), add = "+")
		canvas.show_next_frame(canvas.frame_num)
		ic("play is over")
	
	def pause_callback(self, canvas, *args, **kwargs): ## plays video at normal speed; pauses at current frame
		# ic("pause")
		canvas.status[0] = canvas.PAUSE
		canvas.last_button = self.play_button
		self.play_button.bind("<ButtonRelease-1>", lambda event: self.play_callback(canvas), add = "+")
		canvas.show_next_frame(canvas.frame_num)

	def switch_play_callback(self):
		if self.play_button.bind("<ButtonRelease-1>", lambda event: self.pause_callback(canvas), add = "+") == True:
			self.play_button.bind("<ButtonRelease-1>", lambda event: self.play_callback(canvas), add = "+")
		else:
			self.play_button.bind("<ButtonRelease-1>", lambda event: self.pause_callback(canvas), add = "+")
			
	def step_forward_callback(self, canvas, *args, **kwargs): ## goes forward one frame
		## ic()

		canvas.status[0] = canvas.STOP
		
		if canvas.frame_num < len(canvas.image_collection.images) - 1:
			canvas.frame_num += 1
			
		canvas.show_next_frame(canvas.frame_num)
		canvas.last_button = self.step_forward_button
	
	def goto_end_callback(self, canvas, *args, **kwargs): ## goes to last frame
		## ic()
		canvas.status[0] = canvas.STOP
		canvas.frame_num = len(canvas.image_collection.images) - 1
		canvas.show_next_frame(canvas.frame_num)
		canvas.last_button = self.goto_end_button
	
	def loop_switch(self, canvas, *args, **kwargs): ## turns on/off looping
		## ic("")
		canvas.status[1] = not canvas.status[1]
		canvas.last_button = self.loop_button
		## ic(args)

## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 840)
	video_canvas = VideoCanvas(window)
	video_controls = VideoControlsFrame(window, video_canvas)
	video_canvas.grid(row = 0)
	video_controls.grid(row = 1)
	window.mainloop()
