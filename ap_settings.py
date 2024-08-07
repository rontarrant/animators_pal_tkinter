import os
import json
from tkinter import IntVar, StringVar

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

from ap_constants import *

class APSettings:
	# Create a private class attribute to store the single instance
	__instance = None

	@staticmethod
	def get_instance():
		"""Static method to access the single instance of APSettings"""
		if APSettings.__instance is None:
			APSettings.__instance = APSettings()
		return APSettings.__instance

	def __init__(self, *args, **kwargs):
		if APSettings.__instance is not None:
			raise Exception("This class is a singleton!")
		else:
			APSettings.__instance = self
		
		self.settings_file = "settings.json"

		# Initialize default values
		self._window_position = {'x': 100, 'y': 100}
		self._last_opened_folder = '.'
		## for displaying images on canvas
		self.canvas_width = 1280
		self.canvas_height = 720
		self.checkerboard_colours = ("#8ea7dd", "#7d95c7")  # light blue and dark blue
		
		self._direction = IntVar(value = AP_FORWARD)
		self._direction_default = IntVar(value = AP_FORWARD)
		self._shoot_on = IntVar(value = 1)
		self._shoot_on_default = IntVar(value = 1)
		self._fps = IntVar(value = 24)
		self._fps_default = IntVar(value = 24)
		self._delay = int(round(1000 / 24))

		self._resolution = StringVar(value = "1080p (1920x1080)")
		self._resolution_default = StringVar(value = "1080p (1920x1080)")
		self._projection = StringVar(value = "HDTV (16:9)")
		self._projection_default = StringVar(value = "HDTV (16:9)")
		self._pillar_displacement = IntVar(value = 0)
		self._pillar_displacement_default = IntVar(value = 0)
		self._letterbox_displacement = IntVar(value = 0)
		self._letterbox_displacement_default = IntVar(value = 0)

		self.load_settings()

	def save_settings(self):
		self.ap_settings['window_position'] = self._window_position
		self.ap_settings['last_opened_folder'] = self._last_opened_folder
		with open(self.settings_file, "w") as file:
			json.dump(self.ap_settings, file)

	def load_settings(self):
		if os.path.exists(self.settings_file):
			with open(self.settings_file, "r") as file:
				self.ap_settings = json.load(file)
			self._window_position = self.ap_settings.get('window_position', self._window_position)
			self._last_opened_folder = self.ap_settings.get('last_opened_folder', self._last_opened_folder)
		else:
			self.ap_settings = {}

	def update(self):
		self.load_settings()
		
	@property
	def window_position(self):
		return self._window_position

	
	@window_position.setter
	def window_position(self, pos):
		self._window_position = pos

	@property
	def last_opened_folder(self):
		return self._last_opened_folder
	
	@last_opened_folder.setter
	def last_opened_folder(self, folder):
		self._last_opened_folder = folder

	@property
	def direction(self):
		return self._direction.get()
	
	@direction.setter
	def direction(self, value):
		if type(value) == AP_FORWARD or value == AP_BOUNCE:
			self._direction.set(value)
			## ic()
		else:
			self._direction.set(self._direction_default.get())
			## ic()

	@property
	def fps(self):
		## ic(self._fps.get())
		return self._fps.get()
	
	@fps.setter
	def fps(self, value):
		if value == 18 or value == 24 or value == 30:
			self._fps.set(value)
			self._delay = self.fps2ms(value)
			##ic(self._fps.get(), self._delay)
		else:
			self._fps.set(self._fps_default.get())
			self._delay = self.fps2ms(self._fps_default.get())
			##ic(self._fps.get(), self._delay)

	'''
	This doesn't need a setter. It's taken care of in fps().
	'''
	@property
	def delay(self):
		return self._delay
		
	@property
	def shoot_on(self):
		## ic(self._shoot_on.get())
		return self._shoot_on.get()
	
	@shoot_on.setter
	def shoot_on(self, value):
		if value > 0 and value < 10:
			self._shoot_on.set(value)
			## ic(self._shoot_on.get())
		else:
			self._shoot_on.set(self._shoot_on_default.get())
			## ic(self._shoot_on.get())
	
	@property
	def resolution(self):
		return self._resolution.get()
	
	@resolution.setter
	def resolution(self, value):
		##ic(value)
		
		if type(value) == str:
			self._resolution.set(value)
		else:
			self._resolution.set(self.resolution_default.get())

	@property
	def projection(self):
		return self._projection.get()
	
	@projection.setter
	def projection(self, value):
		pass ## ic(value)
		
		if type(value) == str:
			self._projection.set(value)
		else:
			self._projection.set(self.projection_default.get())
	
	@property
	def pillar_displacement(self):
		return self._pillar_displacement.get()
	
	@pillar_displacement.setter
	def pillar_displacement(self, value):
		if type(value) == int:
			self._pillar_displacement.set(value)
		else:
			self._pillar_displacement.set(self._pillar_displacement_default.get())

	@property
	def letterbox_displacement(self):
		return self._letterbox_displacement.get()
	
	@letterbox_displacement.setter
	def letterbox_displacement(self, value):
		if type(value) == int:
			self._letterbox_displacement.set(value)
		else:
			self._letterbox_displacement.set(self._letterbox_default.get())

	def fps2ms(self, fps):
		value = int(round(1000 / fps))
		return value
   