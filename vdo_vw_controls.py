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
	## to the MiM.
	def __init__(self, parent, playback_control, reset_last_frame):
		super().__init__(parent)
		
		## instance variables
		self.parent = parent
		self.playback_control = playback_control
		self.reset_last_frame = reset_last_frame
		
		self.flags = APVideoFlags.get_instance()
		self.mode = self.flags.MODE_HALT ## default

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
		bounce_play_image_up = "images/bounce_play_up.png"
		bounce_play_image_down = "images/bounce_play_down.png"
		self.bounce_play_button = ImageButton(self, bounce_play_image_up, bounce_play_image_down, alt_image_down = pause_image_up, alt_image_up = pause_image_down)
		
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
		## LAYOUT
		self.goto_start_button.grid(row = 0, column = 1, padx = 5)
		self.reverse_step_button.grid(row = 0, column = 2, padx = 5)
		self.bounce_play_button.grid(row = 0, column = 3, padx = 5)
		self.stop_button.grid(row = 0, column = 4, padx = 5)
		self.forward_play_button.grid(row = 0, column = 5, padx = 5)
		self.forward_step_button.grid(row = 0, column = 6, padx = 5)
		self.goto_end_button.grid(row = 0, column = 7, padx = 5)
		
		## BUTTON BINDINGS
		self.goto_start_button.config(command = self.goto_start_callback)
		self.reverse_step_button.config(command = self.reverse_step_callback)
		self.bounce_play_button.config(command = self.bounce_play_callback)
		self.stop_button.config(command =  self.stop_callback)
		self.forward_play_button.config(command =  self.forward_play_callback)
		self.forward_step_button.config(command =  self.forward_step_callback)
		self.goto_end_button.config(command =  self.goto_end_callback)

	def goto_start_callback(self): ## goes to first frame
		## ic()
		self.reset_last_frame()
		## button ID
		self.playback_control(self.flags.GOTO_START_ID)
		
	def reverse_step_callback(self): ## goes back one frame
		## ic()
		self.reset_last_frame()
		## button ID
		self.playback_control(self.flags.REVERSE_STEP_ID)

	def bounce_play_callback(self): ## plays video at normal speed; pauses at current frame
		self.mode = self.flags.MODE_BOUNCE
		##ic(self.mode)
		self.reset_last_frame()
		## button ID
		self.playback_control(self.flags.BOUNCE_PLAY_ID)

	def stop_callback(self): ## stops video, rewinds to first frame
		self.reset_last_frame()
		##ic(self.mode)
		match self.mode:
			case self.flags.MODE_FORWARD:
				self.reset_last_frame()
				self.forward_play_button.config(command = self.forward_play_callback)
				## switch image
				self.forward_play_button.change_button_image()
				self.playback_control(self.flags.FORWARD_STOP_ID)
			case self.flags.MODE_BOUNCE:
				##ic()
				self.playback_control(self.flags.BOUNCE_STOP_ID)
				self.bounce_play_button.change_button_image()
			
	def forward_play_stop(self):
		##ic()
		self.reset_last_frame()
		self.forward_play_button.config(command = self.forward_play_callback)
		## switch image
		self.forward_play_button.change_button_image()
		self.playback_control(self.flags.FORWARD_STOP_ID)
		
	def forward_play_callback(self): ## plays video at normal speed; pauses at current frame
		self.reset_last_frame()
		self.mode = self.flags.MODE_FORWARD
		##ic(self.mode)
		## button ID
		self.playback_control(self.flags.FORWARD_PLAY_ID)
		self.forward_play_button.config(command =  self.forward_pause_callback)
	
	def forward_pause_callback(self): ## plays video at normal speed; pauses at current frame
		## ic("pause")
		self.reset_last_frame()
		## button ID
		self.playback_control(self.flags.FORWARD_PAUSE_ID)
		## ic()
		self.forward_play_button.config(command = self.forward_play_callback)
		## ic()

	def forward_step_callback(self): ## goes forward one frame
		##ic()
		self.reset_last_frame()
		## button ID
		self.playback_control(self.flags.FORWARD_STEP_ID)
		
	def goto_end_callback(self): ## goes to last frame
		## ic()
		self.reset_last_frame()
		## button ID
		self.playback_control(self.flags.GOTO_END_ID)

	def loop_switch(self): ## turns on/off looping
		## ic("")
		self.reset_last_frame()
		## button ID
		self.playback_control(self.flags.LOOP_ID)

	
## testing
if __name__ == "__main__":
	loop = "off"

	def playback_dummy(button_id):
		global loop
		print("Button ID: ", button_id)
		
		if button_id == self.flags.LOOP_ID:
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
