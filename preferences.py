## example of the Borg Idiom used for globally-accessible
## settings.
import os, sys
from tkinter import *
from tkinter.ttk import *

class Borg:
	_shared_state = {}
	
	def __init__(self):
		self.__dict__ = self._shared_state
		
class Preferences(Borg):
	## widget IntVar() variables
	direction = None
	fps = None
	hold_first = None
	hold_first_for = None
	shoot_on = None
	hold_last = None
	hold_last_for = None
	## file-related strings
	images_location = None
	image_file_name_list = []
	video_location = None
	video_file_name = None
	## project-based attributes
	image_resolution = {"width": 1920, "height": 1080} ## default
	video_resolution = {"width": 1920, "height": 1080} ## default
	project_state = None ## True or False
	letterbox_effect = None ## True or False

	def __init__(self):
		Borg.__init__(self)

	def assign_widget_variables(self,
			direction: IntVar,
			fps: IntVar,
			hold_first: IntVar,
			hold_first_for: IntVar,
			shoot_on: IntVar,
			hold_last: IntVar,
			hold_last_for: IntVar):
			
		## test injected variables
		if type(direction) is IntVar:
			self.direction = direction
		else:
			## error state exists, report it
			pass
			
		if type(fps) is IntVar:
			self.fps = fps
		else:
			## error state exists, report it
			pass
			
		if type(hold_first) is IntVar:
			self.hold_first = hold_first
		else:
			## error state exists, report it
			pass

		if type(hold_first_for) is IntVar:
			self.hold_first_for = hold_first_for
		else:
			## error state exists, report it
			pass

		if type(shoot_on) is IntVar:
			self.shoot_on = shoot_on
		else:
			## error state exists, report it
			pass

		if type(hold_last) is IntVar:
			self.hold_last = hold_last
		else:
			## error state exists, report it
			pass

		if type(hold_last_for) is IntVar:
			self.hold_last_for = hold_last_for
		else:
			## error state exists, report it
			pass
	
	def assign_images_location_variable(self, var: [str]):
		if var:
			self.images_location = var
		else:
			## error state exists; report it
			pass
		
	def assign_image_file_name_list_variable(self, var: (str)):
		if type(var) is list:
			if all(type(item) is str for item in var):
				self.image_file_name_list = var
			else:
				## error state exists; report it
				pass

		elif type(var) is str:
			## handle single image (append??)
			pass
		
	def assign_video_location_variable(self, var: IntVar):
		if var:
			self.video_location = var
		else:
			## error state exists; report it
			pass
	
	def assign_video_file_name_variable(self, var: IntVar):
		if var:
			self.video_file_name = var
		else:
			## error state exists; report it
			pass
		
	def assign_image_resolution_variable(self, var: IntVar):
		if var:
			self.image_resolution = var
		else:
			## error state exists; report it
			pass
		
	def assign_video_resolution_variable(self, var: IntVar):
		if var:
			self.video_resolution = var
		else:
			## error state exists; report it
			pass
		
	def assign_project_state_variable(self, var: IntVar):
		if var:
			self.project_state = var
		else:
			## error state exists; report it
			pass
		
	def assign_letterbox_effect_variable(self, var: IntVar):
		if var:
			self.letterbox_effect = var
		else:
			## error state exists; report it
			pass
