'''
vdo_mim_frame.py
Logic that goes between video data and view
'''
## figure out why this frame is too wide
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
		## Not sure which of these are needed locally
		self.loop_state = self.flags.LOOP_OFF
		self.delay = self.fps2ms(self.settings.fps)
		ic(self.delay, self.settings.fps)
		self.mode = None ## default
		self.play_direction = self.settings.direction
		self.current_button = None
		self.current_frame = 0 ## default: first frame
		self.reverse_button_pressed = False

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
		self.video_controls = VideoControlsFrame(self, self.playback_control, self.reverse_button_pressed)

		self.video_settings_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 10, sticky = (N, E, W, S))
		self.video_canvas.grid(row = 2, column = 0, rowspan = 10, columnspan = 10, sticky = (N, E, W, S))
		self.video_controls.grid(row = 12, column = 0, columnspan = 10, sticky = (N, E, W, S))

	## where the action is
	## mode (PLAY, HALT)
	def playback_control(self, button_id, direction, mode):
		first_frame = 0 ## always the same, but for clarity, let's give it a name
		last_frame = len(self.ap_image_collection.images) - 1
		self.video_canvas.show_next_frame((self.current_frame) % len(self.ap_image_collection.images))
		
		match button_id:
			case self.flags.LOOP_ID: ## swap loop state
				match self.loop_state:
					case self.flags.LOOP_ON:
						## set self.loop_state = off
						self.loop_state = self.flags.LOOP_OFF
						ic("loop is OFF")
					case self.flags.LOOP_OFF:
						## set self.loop_state = on
						self.loop_state = self.flags.LOOP_ON
						ic("loop is ON")
			case _: ## all other buttons besides Loop Button
				match mode:
					case self.flags.MODE_PLAY:
						match direction:
							case self.flags.DIRECTION_FORWARD:
								match self.loop_state:
									case self.flags.LOOP_ON:
										if self.current_frame == last_frame:
											ic()
											self.current_frame = 0
											self.winfo_toplevel().after(self.delay, self.playback_control, button_id, direction, mode)
										else:
											ic()
											self.current_frame += 1
											self.winfo_toplevel().after(self.delay, self.playback_control, button_id, direction, mode)
									case self.flags.LOOP_OFF:
										if self.current_frame == last_frame:
											mode = APVideoFlags.MODE_HALT
											self.current_frame = 0
											## switch button image back to Forward Play
											## switch callback
											self.video_controls.forward_play_stop()
										else:
											self.current_frame += 1
											self.winfo_toplevel().after(self.delay, self.playback_control, button_id, direction, mode)
							case self.flags.DIRECTION_REVERSE:
								ic(self.flags.reverse_button_pressed)
								
								if self.flags.reverse_button_pressed == True:
									self.current_frame = last_frame
									self.flags.reverse_button_pressed = False
								
								ic(self.reverse_button_pressed)
								
								match self.loop_state:
									case self.flags.LOOP_ON:
										if self.current_frame == first_frame:
											ic()
											self.current_frame = last_frame
											self.winfo_toplevel().after(self.delay, self.playback_control, button_id, direction, mode)
										else:
											ic()
											self.current_frame -= 1
											self.winfo_toplevel().after(self.delay, self.playback_control, button_id, direction, mode)
									case self.flags.LOOP_OFF:
										if self.current_frame == first_frame:
											ic()
											mode = APVideoFlags.MODE_HALT
											self.current_frame = last_frame
											## switch button image back to Reverse Play
											## switch callback
											self.video_controls.reverse_play_stop()
										else:
											ic()
											self.winfo_toplevel().after(self.delay, self.playback_control, button_id, direction, mode)
											self.current_frame -= 1
					case self.flags.MODE_HALT:
						match button_id: ## FORWARD_PAUSE, REVERSE_PAUSE, FORWARD_STOP, REVERSE_STOP, GOTO_END, GOTO_START
							case self.flags.FORWARD_PAUSE_ID:
								## change forward button image from Pause to Play
								ic()
							case self.flags.REVERSE_PAUSE_ID:
								## change reverse button image from Pause to Play
								ic()
							case self.flags.FORWARD_STOP_ID:
								## change forward button image from Pause to Play
								## reset to first frame in the collection
								self.current_frame = 0
								ic()
							case self.flags.REVERSE_STOP_ID:
								## change reverse button image from Pause to Play
								## reset to last image in the collection
								self.current_frame = len(self.ap_image_collection.images) - 1
								ic()
							case self.flags.GOTO_END_ID:
								## reset to last image in the collection
								self.current_frame = len(self.ap_image_collection.images) - 1
								ic()
							case self.flags.GOTO_START_ID:
								## reset to first frame in the collection
								self.current_frame = 0
								ic()
								
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
