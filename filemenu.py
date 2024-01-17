from tkinter import *
from tkinter import ttk
from tkinter import filedialog

## local
from preferences import Preferences

class FileMenu(Menu):
	## attributes
	label_text = "File"
	window = None
	imagetypes = None
	prefs = None
	
	def __init__(self, menubar, window):
		self.window = window
		super().__init__(menubar)
		items = self.index ## shortcut to item index
		## configure stuff
		self.assign_filetypes()
		self.add_command(label = "New", command = self.file_new)
		self.entryconfig(items("New"), accelerator = "(Ctrl-N)")
		window.bind('<Control_L><n>', self.file_new)
		
		self.add_command(label = "Open", command = self.file_open)
		self.entryconfig(items("Open"), accelerator = "(Ctrl-O)")
		window.bind('<Control_L><o>', self.file_open)
		
		self.add_command(label = "Append Images", command = self.append_images)
		self.entryconfig(items("Append Images"), accelerator = "(Ctrl-A)")
		window.bind('<Control_L><a>', self.append_images)

		self.add_command(label = "Save Project", command = self.file_save)
		self.entryconfig(items("Save Project"), accelerator = "(Ctrl-S)")
		window.bind('<Control_L><s>', self.file_save)
	
		self.add_command(label = "Save Project as...", command = self.file_save_as)
		self.entryconfig(items("Save Project as..."), accelerator = "(Ctrl-Shift-S)")
		window.bind('<Control_L><S>', self.file_save_as)
		
		self.add_command(label = "Close Project", command = self.file_close)
		self.entryconfig(items("Close Project"), accelerator = "(Ctrl-W)")
		window.bind('<Control_L><w>', self.file_close)
		
		self.add_command(label = "Build MP4 Video", command = self.build_mp4)
		self.entryconfig(items("Build MP4 Video"), accelerator = "(Ctrl-M)")
		window.bind('<Control_L><m>', self.build_mp4)
		
		self.add_command(label = "Save MP4 Video", command = self.save_mp4)
		self.entryconfig(items("Save MP4 Video"), accelerator = "(Ctrl-Shift-M)")
		window.bind('<Control_L><M>', self.save_mp4)
		
		self.add_command(label = "Exit", command = self.exit)
		self.entryconfig(items("Exit"), accelerator = "(Ctrl-X)")
		window.bind('<Control_L><x>', self.exit)

	def assign_filetypes(self):
		all_formats = r"*.png *.jpg *.bmp *.pbm *.pgm *.ppm *.tif *.tiff *.exr"
		self.imagetypes = (("Portable Network Graphics", "*.png"),
								("Joint Photographic Experts Group", "*.jpg"),
								("Windows Bitmap", "*.bmp"),
								("Portable Image Formats", "*.pbm *.pgm *.ppm"),
								("Tag Image File Format", "*.tif *.tiff"),
								("High-dynamic-range Image File Format", "*.exr"),
								("All formats", all_formats))

	def file_new(self, event = None):
		print("creating a new file", event)
		print("filename: ", self.window.filename)
	
	def file_open(self, event = None):
		print("retrieving image files...")
		self.window.image_files = filedialog.askopenfilenames(filetypes = self.imagetypes)
		print("image file names: ", self.window.image_files)
		
		for image in self.window.image_files:
			print(image)

	def file_save(self, event = None):
		print("saving project...")
		if self.window.filename == None:
			print("filename: ", self.window.filename)
			filedialog.asksaveasfilename(filetypes = self.imagetypes)

	def file_save_as(self, event = None):
		print("saving project as...")
		print("filename: ", self.window.filename)

	def file_close(self, event = None):
		print("closing project...")
		print("filename: ", self.window.filename)

	def append_images(self, event = None):
		print("appending images...")

	def build_mp4(self, event = None):
		print("building MP4 video...")

	def save_mp4(self, event = None):
		print("saving MP4 video...")

	def exit(self, event = None):
		print("exiting...")
		print("filename: ", self.window.filename)

