from tkinter import *
from tkinter import ttk
from tkinter import filedialog

## Python stuff
import os
import sys
import cv2

## local
from ap_image_collection import APImageCollection
from ap_image import APImage
from vdo_vw_canvas import VideoCanvas
from ap_settings import APSettings

class FileMenu(Menu):
	def __init__(self, menubar, window, video_canvas, image_size_set, build_new_image_list):
		self.ap_settings = APSettings()
		self.label_text = "File"
		self.window = window
		self.ap_image_collection = APImageCollection.get_instance()
		super().__init__(menubar)
		items = self.index ## shortcut to item index
		## CONFIGURE
		self.assign_filetypes()

		self.add_command(label = "New", command = self.file_new)
		self.entryconfig(items("New"), accelerator = "(Ctrl-N)")
		window.bind('<Control_L><n>', self.file_new)
		
		self.add_command(label = "Add Images",
			command = lambda: self.add_images(video_canvas, image_size_set, build_new_image_list))
		
		self.entryconfig(items("Add Images"), accelerator = "(Ctrl-A)")
		
		window.bind('<Control_L><a>',
			lambda: self.add_images(video_canvas, image_size_set, build_new_image_list))
		'''
		self.add_command(label = "Open Project", command = self.file_open)
		self.entryconfig(items("Open Project"), accelerator = "(Ctrl-O)")
		window.bind('<Control_L><o>', self.file_open)
		
		self.add_command(label = "Save Project", command = self.file_save)
		self.entryconfig(items("Save Project"), accelerator = "(Ctrl-S)")
		window.bind('<Control_L><s>', self.file_save)
	
		self.add_command(label = "Save Project as...", command = self.file_save_as)
		self.entryconfig(items("Save Project as..."), accelerator = "(Ctrl-Shift-S)")
		window.bind('<Control_L><S>', self.file_save_as)
		
		self.add_command(label = "Close Project", command = self.file_close)
		self.entryconfig(items("Close Project"), accelerator = "(Ctrl-W)")
		window.bind('<Control_L><w>', self.file_close)
		'''
		
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
		## ic(event)
		## ic(self.window.project_name)
		pass
		
	'''
	def file_open(self, event = None):
		## ic()
		pass
		
	def file_save(self, event = None):
		ic()
		if self.window.project_name == None:
			## ic(self.window.project_name)
			filedialog.asksaveasproject_name(filetypes = self.imagetypes)

	def file_save_as(self, event = None):
		## ic()
		## ic(self.window.project_name)
		pass

	def file_close(self, event = None):
		## ic()
		## ic(self.window.project_name)
		pass
	'''
	
	def add_images(self, video_canvas, image_size_set, build_new_image_list, event = None):
		'''
		The askopenfilenames() dialog returns a tuple, but it'll be
		easier to add to the image	list if it's an actual Python list.
		So, the dialog results are assigned to a temp variable first.
		Then a for loop append()s each image to the image_files variable.
		This opens us up to appending multiple image sequences
		from multiple sources to create a longer animation. In fact,
		the same sequence can be added over and over, if desired.
		'''
		## Make sure that if we cancel, we don't get an error.
		image_file_name = None
		temp = None
		#prefs = Preferences()
		
		## change initialdir to point at the stored location
		## when you figure that shit out
		initial_dir = self.ap_settings.last_opened_folder
		temp = filedialog.askopenfilenames(filetypes = self.imagetypes, initialdir = initial_dir)
		
		if temp:
			## ic("temp: \n", temp)
			
			## Find out how many images are already in the collection.
			old_count = len(self.ap_image_collection.images)
			
			## add the new images to the ap_image_collection
			for image_file_name in temp:
				image = APImage(image_file_name)
				self.ap_image_collection.add(image)
			
			## save the current path
			if image_file_name:
				self.ap_settings.last_opened_folder = os.path.dirname(image_file_name)
				self.ap_settings.save_settings()

			## now get the number of images in the collection again...
			new_count = len(self.ap_image_collection.images)
			## and find the added_images_count, thus we know how many new images were added
			added_images_count = new_count - old_count
			## testing
			'''
			for index in self.ap_image_collection.images:
				## ic("collection image: ", index)
			'''
			video_canvas.show_frame(old_count) ## put 1st new frame in video_canvas
			image_size_set.update(image.image_width, image.image_height)
			build_new_image_list(added_images_count)

			## testing
			'''
			## ic("from the window:")

			for image in self.window.image_files:
				## ic(image)

			## ic("from prefs:")

			for image in prefs.image_file_name_list:
				## ic(image)
			'''

	'''
	Need access to:
	- list of images loaded (self.ap_image_collection.images)
	- file handle for saving
	- from APSettings:
		- self.ap_settings.shoot_on
		- self.ap_settings.fps
		- self.ap_settings.resolution (to set width and height of video)
			- compare image ratio to projection ratio so see which dimension will be fit
		- self.ap_settings.projection (to index into screen_resolutions dictionary)
		- self.ap_settings.pillarbox_offset (to place image)
		- self.ap_settings.letterbox_offset (to place image)
	- save dialog
	- OpenCV library
	
	Operations:
	- set the video file type (.mp4)
	- set the video width and height
	- instantiate a video file handle (cv2.VideoWriter() needs output file name, fps, width, and height)
	- step through the images:
		- build image layers:
			- lay down the black background
			- get image projection ratio
			- compare image projection to projection ratio in self.ap_settings.projection
				- divide the image height by the resolution height to get the scaling factor
				- divide the image height and width by the scaling factor to get the fitted image width and height
				- resize image
			- lay down the image on top
		- range through the shoot_on for number of times to hold each frame
		- write the frame to the video
	
	- cv2.destroyAllWindows() to deallocate RAM
	- release the video (video.release())
	'''
	def save_mp4(self, event = None):
		
		## ic("saving MP4 video...")
		pass

	def exit(self, event = None):
		## ic("exiting...")
		pass
