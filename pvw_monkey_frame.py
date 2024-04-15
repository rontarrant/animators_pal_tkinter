'''
pvw_monkey_frame.py
Logic that goes between the preview data and view
'''
from ap_image_collection import *
from ap_settings import *
from ap_screen_aspect_ratios import *

from pvw_vw_file_treeview import *
from pvw_vw_thumbnail_canvas import *

class PreviewMonkeyFrame(Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent)
		## data classes (decide which [if any] methods need to be passed to these)
		image_collection = APImageCollection
		column_count = 4 ## number of columns in the file Treeview

		# layout
		## set the row and column minimum sizes
		for row in range(13):
			self.grid_rowconfigure(row, minsize = 72)
		
		for column in range(3):
			self.grid_columnconfigure(column, minsize = 128)
		
		## view classes (decide which [if any] methods need to be passed to these)
		thumbnail_canvas = ThumbnailCanvas(self)
		file_treeview = FileTreeview(self, column_count, thumbnail_canvas)

		## insert frames for each window area
		file_treeview.grid(row = 0, column = 0, rowspan = 10, columnspan = 3, sticky = (N, E, W, S))
		thumbnail_canvas.grid(row = 10, column = 0, rowspan = 3, columnspan = 3, sticky = (N, E, W, S))

	## go-between methods
	def build_new_image_list(self):
		pass
	
	def preview_thumbnail(self):
		pass

## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 806)
	previewmonkeyframe = PreviewMonkeyFrame(window)
	previewmonkeyframe.grid()
	window.mainloop()
