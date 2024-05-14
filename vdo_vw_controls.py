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
	## The button callbacks ID themselves
	## to the MiM and pass along the mode
	## that's associated with the calling button
	## callback. Except for LoopOn/LoopOff which
	## passes a dummy mode ignored by the MiM.
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
		self.play_forward_button = ImageButton(self, play_image_up, play_image_down, alt_image_down = pause_image_up, alt_image_up = pause_image_down)
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
		self.play_forward_button.grid(row = 0, column = 5, padx = 5)
		self.step_forward_button.grid(row = 0, column = 6, padx = 5)
		self.goto_end_button.grid(row = 0, column = 7, padx = 5)
		self.loop_button.grid(row = 0, column = 8, padx = 5)
		
		## BUTTON BINDINGS
		self.goto_start_button.config(command = self.goto_start_callback)
		self.step_backward_button.config(command = self.step_backward_callback)
		self.play_reverse_button.config(command = self.play_reverse_callback)
		self.stop_button.config(command =  self.stop_callback)
		self.play_forward_button.config(command =  self.play_forward_callback)
		self.step_forward_button.config(command =  self.step_forward_callback)
		self.goto_end_button.config(command =  self.goto_end_callback)
		self.loop_button.config(command =  self.loop_switch)

	def goto_start_callback(self): ## goes to first frame
		ic()
		
	def step_backward_callback(self): ## goes back one frame
		ic()

	def play_reverse_callback(self): ## plays video at normal speed; pauses at current frame
		ic("play")
	
	def pause_reverse_callback(self): ## plays video at normal speed; pauses at current frame
		ic("pause")
		
	def stop_callback(self): ## stops video, rewinds to first frame
		ic()
				
	def play_forward_callback(self): ## plays video at normal speed; pauses at current frame
		ic("play")
	
	def pause_forward_callback(self): ## plays video at normal speed; pauses at current frame
		ic("pause")

	def step_forward_callback(self): ## goes forward one frame
		ic()
		
	def goto_end_callback(self): ## goes to last frame
		ic()
	
	def loop_switch(self): ## turns on/off looping
		ic("")

## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 840)
	video_controls = VideoControlsFrame(window)
	video_controls.grid(row = 1)
	window.mainloop()
