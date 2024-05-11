'''
vdo_mim_frame.py
Logic that goes between video data and view
'''
## figure out why this frame is too wide
from ap_image_collection import *
from ap_settings import *

from vdo_vw_set_mim_frame import *
from vdo_vw_canvas import *
from vdo_vw_controls import *

class VideoMiMFrame(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent)
		## data classes (decide which [if any] methods need to be passed to these)
		ap_image_collection = APImageCollection.get_instance()
		self.settings = APSettings.get_instance()
		
		## playback_control() arguments
		PLAY = 1
		HALT = 0
		self.action_mode = None ## default
		self.play_direction = self.settings.direction
		self.current_button = None

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
		self.video_controls = VideoControlsFrame(self)

		self.video_settings_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 10, sticky = (N, E, W, S))
		self.video_canvas.grid(row = 2, column = 0, rowspan = 10, columnspan = 10, sticky = (N, E, W, S))
		self.video_controls.grid(row = 12, column = 0, columnspan = 10, sticky = (N, E, W, S))

	## where the action is
	## mode (PLAY, HALT)
	def playback_control(self, mode, direction, button, frame_number):
		self.video_canvas.show_next_frame(frame_number)

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
