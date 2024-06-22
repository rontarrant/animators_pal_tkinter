'''
pvw_mim_frame.py
Logic that goes between the preview data and view
'''
from ap_image_collection import *

from pvw_vw_file_treeview import *
from pvw_vw_thumbnail_canvas import *

class PreviewMiMFrame(Frame):
	def __init__(self, parent, image_size_set, *args, **kwargs):
		super().__init__(parent)
		## data classes (decide which [if any] methods need to be passed to these)
		column_count = 4 ## number of columns in the file Treeview

		# layout
		## set the row and column minimum sizes
		for row in range(13):
			self.grid_rowconfigure(row, minsize = 72)
		
		for column in range(3):
			self.grid_columnconfigure(column, minsize = 128)
		
		## view classes (decide which [if any] methods need to be passed to these)
		self.thumbnail_canvas = ThumbnailCanvas(self)
		self.file_treeview = FileTreeview(self, column_count, self.thumbnail_canvas.preview_thumbnail, image_size_set)

		## insert frames for each window area
		self.file_treeview.grid(row = 0, column = 0, rowspan = 10, columnspan = 3, sticky = (N, E, W, S))
		self.thumbnail_canvas.grid(row = 10, column = 0, rowspan = 3, columnspan = 3, sticky = (N, E, W, S))

	## go-between methods
	def build_new_image_list(self, new_file_count):
		self.file_treeview.build_new_image_list(new_file_count)

## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 806)
	previewmimframe = PreviewMiMFrame(window)
	previewmimframe.grid()
	window.mainloop()
