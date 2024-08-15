## tkinter
from tkinter import *
from tkinter.ttk import *

'''
To display projection changes, we need access to the image collection, and
through it, access to all images. This would allow each image to be reformatted
to fit the selected Projection settings.
Whatever processing is done would also have to be done (based on Projection settings)
when images are loaded as well (ie. in the FileMenu.add_images() method).
'''

## local
from ap_projection_ratios import *
from ap_settings import *
from ap_image_collection import APImageCollection
from vdo_vw_canvas import VideoCanvas

class ProjectionSet(Frame):
	def __init__(self, parent, padx, parent_update, video_canvas, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		## build & configure options
		self.settings = APSettings.get_instance()
		self.video_canvas = video_canvas
		self.image_collection = APImageCollection.get_instance()
		self.parent_update = parent_update
		default = 1
		self.columnconfigure(0, minsize = 260)
		self.columnconfigure(1, minsize = 260)
		self.options = [] ## empty list
		self.build_options() ## add items
		self.selection = StringVar() ## instantiate associated variable
		
		## instantiate menu & set default (arg #3)
		self.label = Label(self, text = "Projection Ratio")
		self.option_menu = OptionMenu(self, self.selection, self.options[default], *self.options)
		self.label.grid(column = 0, row = 0, sticky = E, padx = padx)
		self.option_menu.grid(column = 1, row = 0, sticky = W, padx = padx)
		self.selection.set(self.settings.projection)
		
		## attach callback
		self.selection.trace('w', self.update)
	
	def build_options(self):
		for ratio, properties in projection_ratios.items():
			option = ratio
			self.options.append(option)
			
	def update(self, *args):
		self.settings.projection = self.selection.get()
		self.parent_update()
		
		if self.image_collection.images:
			for image in self.image_collection.images:
				image.build_image_4_display()
			
			self.video_canvas.show_next_frame(self.video_canvas.current_frame)

## testing
def main():
	window = Window()
	window.mainloop()

class Window(Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.settings = APSettings()
		projection_set = ProjectionSet(self, 10, self.post_info_dummy)
		projection_set.pack(ipadx = 20, ipady = 10)

	def post_info_dummy(self):
		print("filling info")
		
if __name__ == "__main__":
	main()
