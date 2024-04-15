'''
vdo_monkey_frame.py
Logic that goes between video data and view
'''
## figure out why this frame is too wide
from ap_image_collection import *
from ap_settings import *
from ap_screen_aspect_ratios import *

from vdo_vw_set_monkey_frame import *
from vdo_vw_canvas import *
from vdo_vw_controls import *

class VideoMonkeyFrame(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent)
		## data classes (decide which [if any] methods need to be passed to these)
		ap_image_collection = APImageCollection

		# layout
		## set the row and column minimum sizes
		for row in range(13):
			self.grid_rowconfigure(row, minsize = 72)
		
		for column in range(10):
			self.grid_columnconfigure(column, minsize = 128)
			
		## view classes (decide which [if any] methods need to be passed to these)
		video_settings_frame = VideoSettingsFrame(self)
		video_canvas = VideoCanvas(self)
		video_controls = VideoControlsFrame(self)

		video_settings_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 10, sticky = (N, E, W, S))
		video_canvas.grid(row = 2, column = 0, rowspan = 10, columnspan = 10, sticky = (N, E, W, S))
		video_controls.grid(row = 12, column = 0, columnspan = 10, sticky = (N, E, W, S))

	## go-between methods
	def show_next_frame(self):
		pass

## testing
if __name__ == "__main__":
	width = 10 * 128
	height = 13 * 72
	print("width: ", width, ", height: ", height)
	window = Tk()
	window.configure(width = width, height = height)
	videomonkeyframe = VideoMonkeyFrame(window)
	videomonkeyframe.grid()
	window.mainloop()
