## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from ap_constants import *

class APSettings():
	_direction: int = AP_FORWARD
	_direction_default: int = AP_FORWARD ## default: play from first frame to last
	_shoot_on: int = 1
	_shoot_on_default: int = 1 ## default: each image held for one frame
	_fps: int = 24
	_fps_default = 24	## default: 24 frames per second
	_displacement: int = 0 ## width of pillars or letterboxes
	_displacement_direction = AP_NEUTRAL ## HDTV & 1080p, no pillars or letterboxing
	_projection: str = "HDTV"
	_projection_default: str = "HDTV" ## default: HD
	_resolution: str = "1080p"
	_resolution_default: str = "1080p" ## default: HD
	
	def get_direction(self):
		return self._direction
	
	def set_direction(self, value):
		if type(value) == AP_FORWARD or value == AP_REVERSE:
			self._direction = value
		else:
			self._direction = self._direction_default

	def get_shoot_on(self):
		return self._shoot_on
	
	def set_shoot_on(self, value):
		if value > 0 and value < 10:
			self._shoot_on = value
		else:
			self._shoot_on = self._shoot_on_default
		
	def get_fps(self):
		return self._fps
	
	def set_fps(self, value):
		if value == 12 or value == 18 or value == 24 or value == 30 or value == 60:
			self._fps = value
		else:
			self._fps = 24
		
	def get_displacement(self):
		return self._displacement
	
	def set_displacement(self, value):
		if type(value) == int:
			self._displacement = value
		else:
			self._displacement = self._displacement_default
	
	def get_resolution(self):
		return self._resolution
	
	def set_resolution(self, value):
		if type(value) == str:
			self._resolution = value
		else:
			self._resolution = self.resolution_default

	def get_projection(self):
		return self._projection
	
	def set_projection(self, value):
		if type(value) == str:
			self._projection = value
		else:
			self._projection = self.projection_default

## testing
if __name__ == "__main__":
	settings = APSettings()
	print("test direction:")
	settings.set_direction(-2)
	print("\tsetting to -2: ", settings.get_direction())
	settings.set_direction(-1)
	print("\tsetting to -1: ", settings.get_direction())

	print("test shoot_on:")
	settings.shoot_on = 9
	print("\tsetting to 9: ", settings.shoot_on)
	settings.shoot_on = -2
	print("\tsetting to -2: ", settings.shoot_on)

	print("test fps:")
	settings.fps = 37
	print("\tsetting to 37: ", settings.fps)
	settings.fps = 18
	print("\tsetting to 18:", settings.fps)

	print("test displacement:")
	settings.displacement = 870
	print("\tset to 870 - " + str(settings.displacement))

	print("test resolution:")
	settings.displacement = 192
	print("\tset to 192 - height: ", settings.displacement)

	print("test projection:")
	settings.displacement = 192
	print("\tset to 192 - height: ", settings.displacement)

