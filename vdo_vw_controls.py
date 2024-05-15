'''
Video Controls
The usual controls for video... play, stop, pause, etc. 
'''

from tkinter import *

## local
from vdo_vw_canvas import VideoCanvas
from vdo_vw_image_button import ImageButton
from ap_video_flags import *

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
	def __init__(self, parent, playback_control):
		super().__init__(parent)
		
		## instance variables
		self.parent = parent
		self.playback_control = playback_control
		self.flags = APVideoFlags()

		self.configure(width = 1280, height = 72)
		self.grid(sticky = (N, E, W, S))
		self.grid_columnconfigure(0, weight = 1)
		self.grid_columnconfigure(9, weight = 1)
		## BUTTON IMAGES
		# goto start button
		self.goto_start_button = ImageButton(self, "images/goto_start_up.png", "images/goto_start_down.png")
		
		# reverse_step button
		self.reverse_step_button = ImageButton(self, "images/reverse_step_up.png", "images/reverse_step_down.png")
		
		# reverse_play/reverse_pause button
		pause_image_up = "images/pause_up.png"
		pause_image_down = "images/pause_down.png"
		reverse_play_image_up = "images/reverse_play_up.png"
		reverse_play_image_down = "images/reverse_play_down.png"
		self.reverse_play_button = ImageButton(self, reverse_play_image_up, reverse_play_image_down, alt_image_down = pause_image_up, alt_image_up = pause_image_down)
		
		# stop button
		self.stop_button = ImageButton(self, "images/stop_up.png", "images/stop_down.png")
		
		# forward play/forward pause button
		forward_play_image_up = "images/forward_play_up.png"
		forward_play_image_down = "images/forward_play_down.png"
		self.forward_play_button = ImageButton(self, forward_play_image_up, forward_play_image_down, alt_image_down = pause_image_up, alt_image_up = pause_image_down)
		
		# forward step button
		self.forward_step_button = ImageButton(self, "images/forward_step_up.png", "images/forward_step_down.png")
		
		# goto end button
		self.goto_end_button = ImageButton(self, "images/goto_end_up.png", "images/goto_end_down.png")
		
		# loop on/off button
		loop_image_up = "images/loop_off_up.png"
		loop_image_down = "images/loop_off_down.png"
		loop_image_swap_up = "images/loop_on_up.png"
		loop_image_swap_down = "images/loop_on_down.png"
		self.loop_button = ImageButton(self, loop_image_up, loop_image_down, alt_image_down = loop_image_swap_up, alt_image_up = loop_image_swap_down)
		
		## LAYOUT
		self.goto_start_button.grid(row = 0, column = 1, padx = 5)
		self.reverse_step_button.grid(row = 0, column = 2, padx = 5)
		self.reverse_play_button.grid(row = 0, column = 3, padx = 5)
		self.stop_button.grid(row = 0, column = 4, padx = 5)
		self.forward_play_button.grid(row = 0, column = 5, padx = 5)
		self.forward_step_button.grid(row = 0, column = 6, padx = 5)
		self.goto_end_button.grid(row = 0, column = 7, padx = 5)
		self.loop_button.grid(row = 0, column = 8, padx = 5)
		
		## BUTTON BINDINGS
		self.goto_start_button.config(command = self.goto_start_callback)
		self.reverse_step_button.config(command = self.reverse_step_callback)
		self.reverse_play_button.config(command = self.reverse_play_callback)
		self.stop_button.config(command =  self.stop_callback)
		self.forward_play_button.config(command =  self.forward_play_callback)
		self.forward_step_button.config(command =  self.forward_step_callback)
		self.goto_end_button.config(command =  self.goto_end_callback)
		self.loop_button.config(command =  self.loop_switch)

	def goto_start_callback(self): ## goes to first frame
		ic()
		## button ID, direction, mode
		self.playback_control(APVideoFlags.GOTO_START_ID, APVideoFlags.DIRECTION_FORWARD, APVideoFlags.MODE_HALT)
		
	def reverse_step_callback(self): ## goes back one frame
		ic()
		## button ID, direction, mode
		self.playback_control(APVideoFlags.REVERSE_STEP_ID, APVideoFlags.DIRECTION_REVERSE, APVideoFlags.MODE_HALT)

	def reverse_play_callback(self): ## plays video at normal speed; pauses at current frame
		ic("play")
		## button ID, direction, mode
		self.playback_control(APVideoFlags.REVERSE_PLAY_ID, APVideoFlags.DIRECTION_REVERSE, APVideoFlags.MODE_PLAY)
		self.reverse_play_button.config(command = self.reverse_pause_callback)
	
	def reverse_pause_callback(self): ## plays video at normal speed; pauses at current frame
		ic("pause")
		## button ID, direction, mode
		self.playback_control(APVideoFlags.REVERSE_PAUSE_ID, APVideoFlags.DIRECTION_REVERSE, APVideoFlags.MODE_HALT)
		self.reverse_play_button.config(command = self.reverse_play_callback)
	
	def stop_callback(self): ## stops video, rewinds to first frame
		ic()
		## button ID, direction, mode
		self.playback_control(APVideoFlags.STOP_ID, APVideoFlags.DIRECTION_NONE, APVideoFlags.MODE_HALT)
				
	def forward_play_callback(self): ## plays video at normal speed; pauses at current frame
		ic("play")
		## button ID, direction, mode
		self.playback_control(APVideoFlags.FORWARD_PLAY_ID, APVideoFlags.DIRECTION_FORWARD, APVideoFlags.MODE_PLAY)
		self.forward_play_button.config(command =  self.forward_pause_callback)
	
	def forward_pause_callback(self): ## plays video at normal speed; pauses at current frame
		ic("pause")
		## button ID, direction, mode
		self.playback_control(APVideoFlags.FORWARD_PAUSE_ID, APVideoFlags.DIRECTION_FORWARD, APVideoFlags.MODE_HALT)
		self.forward_play_button.config(command =  self.forward_play_callback)

	def forward_step_callback(self): ## goes forward one frame
		ic()
		## button ID, direction, mode
		self.playback_control(APVideoFlags.FORWARD_STEP_ID, APVideoFlags.DIRECTION_FORWARD, APVideoFlags.MODE_HALT)
		
	def goto_end_callback(self): ## goes to last frame
		ic()
		## button ID, direction, mode
		self.playback_control(APVideoFlags.GOTO_END_ID, APVideoFlags.DIRECTION_FORWARD, APVideoFlags.MODE_HALT)
	
	def loop_switch(self): ## turns on/off looping
		ic("")
		## button ID, direction, mode
		self.playback_control(APVideoFlags.LOOP_ID, APVideoFlags.DIRECTION_NONE, APVideoFlags.MODE_NONE)

## testing
if __name__ == "__main__":
	loop = "off"

	def playback_dummy(button_id, direction, mode):
		global loop
		print("Button ID: ", button_id, ", direction: ", direction, ", mode: ", mode)
		
		if button_id == APVideoFlags.LOOP_ID:
			if loop == "off":
				loop = "on"
			elif loop == "on":
				loop = 'off'
			else:
				pass
		
		print("Looping is ", loop)
		
	window = Tk()
	window.configure(width = 1280, height = 840)
	video_controls = VideoControlsFrame(window, playback_dummy)
	video_controls.grid(row = 1)
	window.mainloop()
