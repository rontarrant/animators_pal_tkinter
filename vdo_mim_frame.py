'''
vdo_mim_frame.py
Logic that goes between video data and view
'''

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
		self.FIRST_FRAME = 0
		self.LAST_FRAME = -1 ## updated in all button callbacks in vdo_vw_controls.py
		self.current_frame = self.FIRST_FRAME
		self.bouncing = False
		self.bounce_direction = 1
		self.after_id = None
		
		# LAYOUT CONFIG
		## set row and column minimum sizes
		for row in range(13):
			self.grid_rowconfigure(row, minsize = 72)
		
		for column in range(10):
			self.grid_columnconfigure(column, minsize = 128)
		
		## CHILDREN
		self.video_settings_frame = VideoSettingsFrame(self)
		self.video_canvas = VideoCanvas(self)
		self.video_controls = VideoControlsFrame(self, self.playback_control, self.reset_last_frame, self.get_current_frame)
		
		## LAYOUT
		self.video_settings_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 10, sticky = (N, E, W, S))
		self.video_canvas.grid(row = 2, column = 0, rowspan = 10, columnspan = 10, sticky = (N, E, W, S))
		self.video_controls.grid(row = 12, column = 0, columnspan = 10, sticky = (N, E, W, S))
		
	def playback_control(self, button_id):
		## ic(self.video_controls.mode, self.current_frame, self.LAST_FRAME)
		match button_id:
			case self.flags.FORWARD_PLAY_ID:
				self.play_forward()
			case self.flags.FORWARD_PAUSE_ID:
				self.pause_forward()
			case self.flags.BOUNCE_PLAY_ID:
				self.toggle_bounce()
			case self.flags.BOUNCE_PAUSE_ID:
				self.toggle_bounce()
			case self.flags.REVERSE_STEP_ID:
				self.reverse_step()
			case self.flags.FORWARD_STEP_ID:
				self.forward_step()
			case self.flags.GOTO_START_ID:
				self.goto_start()
			case self.flags.GOTO_END_ID:
				self.goto_end()
			case self.flags.FORWARD_STOP_ID:
				self.stop_forward_play()
			case self.flags.BOUNCE_STOP_ID:
				self.toggle_bounce()

	def stop_forward_play(self):
		self.call_a_halt()
		## ic(self.current_frame)

	def goto_end(self):
		## reset to first frame in the collection
		self.current_frame = self.LAST_FRAME
		self.bounce_direction = -1
		self.video_canvas.show_next_frame(self.current_frame)
		#self.call_a_halt()	
		## ic()
		
	def goto_start(self):
		## reset to first frame in the collection
		self.current_frame = self.FIRST_FRAME
		self.video_canvas.show_next_frame(self.current_frame)
		self.bounce_direction = 1
		self.call_a_halt()	
		## ic(self.current_frame, self.video_controls.mode)
	
	def reverse_step(self):
		## ic(self.current_frame)
		match self.current_frame:
			case self.FIRST_FRAME:
				pass
			case _:
				self.current_frame -= 1
				self.video_canvas.show_next_frame(self.current_frame)

	def forward_step(self):
		## ic(self.current_frame)
		match self.current_frame:
			case self.LAST_FRAME:
				pass
			case _:
				self.current_frame += 1
				self.video_canvas.show_next_frame(self.current_frame)

	def play_forward(self):
		match self.current_frame:
			case self.LAST_FRAME:
				## switch button image back to Forward Play
				self.video_controls.forward_play_stop()
				self.call_a_halt()
				ic(self.current_frame, self.video_controls.mode)
			case _:
				self.current_frame += 1
				self.video_canvas.show_next_frame(self.current_frame)
				self.after_id = self.winfo_toplevel().after(self.settings.delay, self.play_forward)
				ic(self.current_frame, self.video_controls.mode)
				
		ic(self.current_frame)

	def toggle_bounce(self):
		## ic(self.video_controls.mode)
		self.bouncing = not self.bouncing
		
		if self.bouncing:
			## ic(self.video_controls.mode)
			self.play_bounce()
		else:
			if self.after_id:
				## ic(self.video_controls.mode)
				self.winfo_toplevel().after_cancel(self.after_id)
				self.after_id = None
		
			self.video_controls.mode = self.flags.MODE_HALT
		
	def play_bounce(self):
		## ic(self.current_frame)

		match self.current_frame:
			case self.FIRST_FRAME:
				self.bounce_direction = 1
			case self.LAST_FRAME:
				self.bounce_direction = -1

		if self.bouncing:  # Bounce Play is on
			# flip the page
			self.video_canvas.show_next_frame(self.current_frame)
			# add 1 if playing forward, -1 if playing reverse
			self.current_frame += self.bounce_direction
			self.after_id = self.winfo_toplevel().after(self.settings.delay, self.play_bounce)  # Approximately 24 frames per second
			
		## ic(self.current_frame)

	def pause_forward(self):
		self.call_a_halt()
		
	def reset_last_frame(self):
		self.LAST_FRAME = len(self.ap_image_collection.images) - 1
		
	def call_a_halt(self):
		## track that we're not in bounce or forward mode
		## keeps the buttons from doing strange things
		self.video_controls.mode = self.flags.MODE_HALT
		
		## if we have an open after_id, kill it
		if self.after_id:
			self.winfo_toplevel().after_cancel(self.after_id)

	def get_current_frame(self):
		return self.current_frame
		
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
