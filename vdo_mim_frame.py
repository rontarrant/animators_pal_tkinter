'''
vdo_mim_frame.py
Logic that goes between video data and view
'''

###############################
## TODO
###############################
## - separate each button's logic into its own method
## - set up dependency injection for all methods
## - add an class instance variable to contain an after_ID
## - assign an after_ID to each call to after()
## - each call to Pause or Stop triggers a call to after_cancel()
## - change MODE_PLAY to MODE_FORWARD or MODE_REVERSE where appropriate

from ap_image_collection import *
from ap_settings import *
from ap_video_flags import *

from vdo_vw_set_mim_frame import *
from vdo_vw_canvas import *
from vdo_vw_controls import *

class VideoMiMFrame(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent)
		## external stuff needed for playback
		self.ap_image_collection = APImageCollection.get_instance()
		self.settings = APSettings.get_instance()
		self.flags = APVideoFlags.get_instance()
		
		## local playback criteria
		self.FIRST_FRAME = 0 ## always the same, but for clarity, let's give it a name
		self.LAST_FRAME = 0
		self.after_id = None
		
		## Not sure which of these are needed locally
		self.delay = self.fps2ms(self.settings.fps)
		## ic(self.delay, self.settings.fps)
		self.current_frame = 0 ## default: first frame
		self.mode = self.flags.MODE_HALT ## default
		self.loop_state = self.flags.LOOPING_OFF

		# layout
		## set the row and column minimum sizes
		for row in range(13):
			self.grid_rowconfigure(row, minsize = 72)
		
		for column in range(10):
			self.grid_columnconfigure(column, minsize = 128)
		
		## CHILDREN
		## view classes (decide which [if any] methods need to be passed to these)
		self.video_settings_frame = VideoSettingsFrame(self)
		self.video_canvas = VideoCanvas(self)
		self.video_controls = VideoControlsFrame(self, self.playback_control, self.update_last_frame)

		self.video_settings_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 10, sticky = (N, E, W, S))
		self.video_canvas.grid(row = 2, column = 0, rowspan = 10, columnspan = 10, sticky = (N, E, W, S))
		self.video_controls.grid(row = 12, column = 0, columnspan = 10, sticky = (N, E, W, S))
	'''
	def play_forward(self):
		## ic(self.flags.forward_button_pressed)
		match self.loop_state:
			case self.flags.LOOPING_ON:
				if self.current_frame == self.LAST_FRAME:
					## ic(mode)
					self.current_frame = 0
					self.after_id = self.winfo_toplevel().after(self.delay, self.playback_control, button_id, mode)
				else:
					## ic(mode)
					self.current_frame += 1
					self.after_id = self.winfo_toplevel().after(self.delay, self.playback_control, button_id, mode)
			case self.flags.LOOPING_OFF:
				match self.current_frame:
					case self.LAST_FRAME:
						mode = APVideoFlags.MODE_HALT
						self.current_frame = 0
						## switch button image back to Forward Play
						## switch callback
						self.video_controls.forward_play_stop()
					case _:
						self.current_frame += 1
						self.after_id = self.winfo_toplevel().after(self.delay, self.playback_control, button_id, mode)
	'''
	def update_last_frame(self):
		self.LAST_FRAME = len(self.ap_image_collection.images)
		
	## where the action is
	## mode (FORWARD, REVERSE, HALT)
	def playback_control(self, button_id, mode):
		self.video_canvas.show_next_frame((self.current_frame) % len(self.ap_image_collection.images))
		#ic(mode, self.loop_state)
		match button_id:
			case self.flags.LOOP_ID: ## swap loop state
				match self.loop_state:
					case self.flags.LOOPING_ON:
						## set self.loop_state = off
						self.loop_state = self.flags.LOOPING_OFF
						## ic("loop is OFF")
					case self.flags.LOOPING_OFF:
						## set self.loop_state = on
						self.loop_state = self.flags.LOOPING_ON
						## ic("loop is ON")
						
			case _: ## all other buttons besides Loop Button
				match mode:
					case self.flags.MODE_FORWARD:
						match self.loop_state:
							case self.flags.LOOPING_ON:
								match self.current_frame:
									case self.LAST_FRAME:
										ic(mode, button_id)
										self.current_frame = 0
										self.after_id = self.winfo_toplevel().after(self.delay, self.playback_control, button_id, mode)
									case _:
										ic(mode, button_id)
										self.current_frame += 1
										self.after_id = self.winfo_toplevel().after(self.delay, self.playback_control, button_id, mode)
							case self.flags.LOOPING_OFF:
								match self.current_frame:
									case self.LAST_FRAME:
										#ic(mode, button_id)
										mode = APVideoFlags.MODE_HALT
										self.current_frame = self.FIRST_FRAME
										## switch button image back to Forward Play
										## switch callback
										self.video_controls.forward_play_stop()
										self.call_a_halt()
									case _:
										self.current_frame += 1
										self.after_id = self.winfo_toplevel().after(self.delay, self.playback_control, button_id, mode)
					case self.flags.MODE_REVERSE:
						match self.loop_state:
							case self.flags.LOOPING_ON:
								match self.current_frame:
									case self.FIRST_FRAME:
										## ic(mode)
										self.current_frame = self.LAST_FRAME
										self.after_id = self.winfo_toplevel().after(self.delay, self.playback_control, button_id, mode)
									case _:
										## ic(mode)
										self.current_frame -= 1
										self.after_id = self.winfo_toplevel().after(self.delay, self.playback_control, button_id, mode)
							case self.flags.LOOPING_OFF:
								match self.current_frame:
									case self.FIRST_FRAME:
										## ic(mode)
										mode = APVideoFlags.MODE_HALT
										self.current_frame = self.LAST_FRAME
										## switch button image back to Reverse Play
										## switch callback
										self.video_controls.reverse_play_stop()
										self.call_a_halt()
									case _:
										self.current_frame -= 1
										self.after_id = self.winfo_toplevel().after(self.delay, self.playback_control, button_id, mode)
					case self.flags.MODE_HALT:
						match button_id: ## FORWARD_PAUSE, REVERSE_PAUSE, FORWARD_STOP, REVERSE_STOP, GOTO_END, GOTO_START
							case self.flags.FORWARD_STEP_ID:
								ic()
								self.call_a_halt()
									
								self.current_frame += 1
							case self.flags.REVERSE_STEP_ID:
								ic()
								self.call_a_halt()
									
								self.current_frame -= 1
							case self.flags.FORWARD_PAUSE_ID:
								## change forward button image from Pause to Play
								## ic(mode)
								self.call_a_halt()
									
							case self.flags.REVERSE_PAUSE_ID:
								## change reverse button image from Pause to Play
								## ic(mode)
								self.call_a_halt()
									
							case self.flags.FORWARD_STOP_ID:
								## change forward button image from Pause to Play
								## reset to first frame in the collection
								self.call_a_halt()
									
								self.current_frame = 0
								## ic(mode)
							case self.flags.REVERSE_STOP_ID:
								## change reverse button image from Pause to Play
								## reset to last image in the collection
								self.call_a_halt()
									
								self.current_frame = len(self.ap_image_collection.images) - 1
								## ic(mode)
							case self.flags.GOTO_END_ID:
								## reset to last image in the collection
								self.call_a_halt()
									
								self.current_frame = len(self.ap_image_collection.images) - 1
								## ic(mode)
							case self.flags.GOTO_START_ID:
								## reset to first frame in the collection
								self.call_a_halt()
									
								self.current_frame = 0
								## ic(mode)
							case self.flags.STOP_ID:
								## reset to first frame in the collection
								self.call_a_halt()
									
								## ic(mode)
								
	def call_a_halt(self):
		if self.after_id:
			self.winfo_toplevel().after_cancel(self.after_id)

	## THIS MAY NOT GO HERE
	def fps2ms(self, fps):
		value = int(round(1000 / fps))
		return value

## testing
if __name__ == "__main__":
	width = 10 * 128
	height = 13 * 72
	print("width: ", width, ", height: ", height)
	window = Tk()
	window.configure(width = width, height = height)
	videomimframe = VideoMiMFrame(window)
	videomimframe.grid()
	window.mainloop()
