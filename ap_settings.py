import os
import json
from tkinter import IntVar, StringVar

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

## local
from ap_constants import *
from observer import Observable, Observer

class APSettings(Observer, Observable):
	# Create a private class attribute to store the single instance
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super().__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, '_initialized'):
			self._observers = set()
			self._settings_ready = False
			self.root = None
			self.loading_dialog = None
			self._initialized = True

		self.settings_file = "settings.json"

		# Initialize default values
		self._window_position = {'x': 100, 'y': 100}
		self._last_opened_folder = '.'
		## for displaying images on canvas
		self._canvas_width = 1280
		self._canvas_height = 720
		self._checkerboard_colours = ("#8ea7dd", "#7d95c7")  # light blue and dark blue
		
		self._direction = IntVar(value = AP_FORWARD)
		self._direction_default = IntVar(value = AP_FORWARD)
		self._shoot_on = IntVar(value = 1)
		self._shoot_on_default = IntVar(value = 1)
		self._fps = IntVar(value = 24)
		self._fps_default = IntVar(value = 24)
		self._delay = int(round(1000 / 24)) ## used only for internal playback

		self._resolution = StringVar(value = "1080p")
		self._resolution_default = StringVar(value = "1080p")
		self._projection = StringVar(value = "FHD TV")
		self._projection_default = StringVar(value = "FHD TV")
		self._pillarbox_offset = IntVar(value = 0)
		self._pillarbox_offset_default = IntVar(value = 0)
		self._letterbox_offset = IntVar(value = 0)
		self._letterbox_offset_default = IntVar(value = 0)

		self.load_settings()
		
	def save_settings(self):
		self.ap_settings['window_position'] = self._window_position
		self.ap_settings['last_opened_folder'] = self._last_opened_folder
		self.ap_settings['canvas_width'] = self._canvas_width
		self.ap_settings['canvas_height'] = self._canvas_height
		self.ap_settings['checkerboard_colours'] = self._checkerboard_colours
		self.ap_settings['direction'] = self._direction.get()
		self.ap_settings['shoot_on'] = self._shoot_on.get()
		self.ap_settings['fps'] = self._fps.get()
		self.ap_settings['delay'] = self._delay
		self.ap_settings['resolution'] = self._resolution.get()
		self.ap_settings['projection'] = self._projection.get()
		self.ap_settings['pillarbox_offset'] = self._pillarbox_offset.get()
		self.ap_settings['letterbox_offset'] = self._letterbox_offset.get()
		
		with open(self.settings_file, "w") as file:
			json.dump(self.ap_settings, file)

	def load_settings(self):
		if os.path.exists(self.settings_file):
			with open(self.settings_file, "r") as file:
				self.ap_settings = json.load(file)
			
			self._window_position = self.ap_settings.get('window_position', self._window_position)
			self._last_opened_folder = self.ap_settings.get('last_opened_folder', self._last_opened_folder)
			self._canvas_width = self.ap_settings.get('canvas_width', self._canvas_width)
			self._canvas_height = self.ap_settings.get('canvas_height', self._canvas_height)
			self._checkerboard_colours = self.ap_settings.get('checkerboard_colours', self._checkerboard_colours)
			self._direction.set(self.ap_settings.get('direction', self._direction))
			self._shoot_on.set(self.ap_settings.get('shoot_on', self._shoot_on))
			self._fps.set(self.ap_settings.get('fps', self._fps))
			self._delay = self.ap_settings.get('delay', self._delay)
			self._resolution.set(self.ap_settings.get('resolution', self._resolution))
			self._projection.set(self.ap_settings.get('projection', self._projection))
			self._pillarbox_offset.set(self.ap_settings.get('pillarbox_offset', self._pillarbox_offset))
			self._letterbox_offset.set(self.ap_settings.get('letterbox_offset', self._letterbox_offset))
			##ic(self.ap_settings)
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
	def canvas_width(self):
		return self._canvas_width

	
	@canvas_width.setter
	def canvas_width(self, pos):
		self._canvas_width = pos

	@property
	def canvas_height(self):
		return self._canvas_height

	
	@canvas_height.setter
	def canvas_height(self, pos):
		self._canvas_height = pos

	@property
	def checkerboard_colours(self):
		return self._checkerboard_colours

	
	@checkerboard_colours.setter
	def checkerboard_colours(self, pos):
		self._checkerboard_colours = pos

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
	def pillarbox_offset(self):
		return self._pillarbox_offset.get()
	
	@pillarbox_offset.setter
	def pillarbox_offset(self, value):
		if type(value) == int:
			self._pillarbox_offset.set(value)
		else:
			self._pillarbox_offset.set(self._pillarbox_offset_default.get())

	@property
	def letterbox_offset(self):
		return self._letterbox_offset.get()
	
	@letterbox_offset.setter
	def letterbox_offset(self, value):
		if type(value) == int:
			self._letterbox_offset.set(value)
		else:
			self._letterbox_offset.set(self._letterbox_default.get())

	def fps2ms(self, fps):
		value = int(round(1000 / fps))
		return value
