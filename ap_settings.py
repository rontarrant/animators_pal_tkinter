## Python
import os
import sys

## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from constants import *

class APSettings():
	_direction: int = FORWARD
	_direction_default: int = FORWARD ## default: play from first frame to last
	_shoot_on: int = 1
	_shoot_on_default: int = 1 ## default: each image held for one frame
	_fps: int = 24
	_fps_default = 24	## default: 24 frames per second
	_displacement: int = 0 ## width of pillars or letterboxes
	_displacement_direction = NEUTRAL ## HDTV & 1080p, no pillars or letterboxing
	_projection: str = "HDTV"
	_projection_default: str = "HDTV" ## default: HD
	_resolution: str = "1080p"
	_resolution_default: str = "1080p" ## default: HD
	
	@property
	def projection(self):
		return self._projection
	
	@projection.setter
	def projection(self, value):
		if type(value) == str:
			self._projection = value
		else:
			self._projection = self._projection_default
	
	@property
	def resolution(self):
		return self._resolution
	
	@resolution.setter
	def resolution(self, value):
		if type(value) == str:
			self._resolution = value
		else:
			self._resolution = self._resolution_default
	
	@property
	def direction(self):
		return self._direction
	
	@direction.setter
	def direction(self, value):
		if value == FORWARD or value == REVERSE:
			self._direction = value
		else:
			self._direction = self._direction_default
	
	@property
	def shoot_on(self):
		print("shoot_on: ", self._shoot_on)
		return self._shoot_on
	
	@shoot_on.setter
	def shoot_on(self, value):
		if value > 0 and value < 10:
			self._shoot_on = value
		else:
			self._shoot_on = self._shoot_on_default
		print("shoot_on: ", self._shoot_on)

	@property
	def fps(self):
		return self._fps
	
	@fps.setter
	def fps(self, value):
		if value == 12 or value == 18 or value == 24 or value == 30 or value == 60:
			self._fps = value
		else:
			self._fps = 24

	@property
	def displacement(self):
		return self._displacement
	
	@displacement.setter
	def displacement(self, value: int):
		if type(value) == int:
			self._displacement = value
				
## testing
if __name__ == "__main__":
	settings = APSettings()
	print("test #1 direction:")
	settings.direction = -2
	print("\tsetting to -2: ", settings.direction)
	settings.direction = -1
	print("\tsetting to -1: ", settings.direction)

	print("test #2 shoot_on:")
	settings.shoot_on = 12
	print("\tsetting to 12: ", settings.shoot_on)
	settings.shoot_on = -2
	print("\tsetting to -2: ", settings.shoot_on)

	print("test #3 fps:")
	settings.fps = 37
	print("\tsetting to 37: ", settings.fps)
	settings.fps = 18
	print("\tsetting to 18:", settings.fps)

	print("test #4 pillar_width:")
	settings.displacement = 870
	print("\tset to 870 - " + str(settings.displacement))

	print("test letterbox_height:")
	settings.displacement = 192
	print("\tset to 192 - height: ", settings.displacement)

	print("test #5 projection:")
	settings.projection = 192
	print("\tset to 192: ", settings.projection)

	print("test projection:")
	settings.projection = "VistaVision"
	print("\tset to VistaVision: ", settings.projection)

	print("test #6 resolution:")
	settings.resolution = "8k"
	print("\tset to 8k: ", settings.resolution)

	print("test resolution:")
	settings.resolution = 2300
	print("\tset to 2300: ", settings.resolution)

'''
need a way to distinguish between an image with pillars and an image with letterboxing
'''