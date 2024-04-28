## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from ap_constants import *
'''
Following is a list of the class properties in APSettings:
Video Playback Settings
_direction:
	: which direction the video is to be played
	: can be either AP_FORWARD or AP_REVERSE
	: default: AP_FORWARD
_shoot_on:
	: how long to display each image
	: can be 1 ... 9
	: default: 1
_fps:
	: speed of playback in frames per second
	: can be 18, 24, or 30
	: default: 24
Video & Image Size Settings
_displacement:
	: width of pillars in pillarbox mode or
	: height of letterboxing in letterbox mode
	: possible values: based on resolution & projection size
	: default: 0
_displacement_direction:
	: images are displaced within the frame 
	  either horizontally, vertically or not at all
	  if the aspect ratio of the image matches the 
	  projection size
	: possible values: AP_NEUTRAL, AP_VERTICAL, AP_HORIZONTAL
	: default: AP_NEUTRAL (to match HDTV/1080p)
_image_width:
_image_height:
	: width and height of the image on disk
	: possible range: anything up to the dimensions of a digital photo
	: defaults: N/A
'''
class APSettings():
	_direction: int = AP_FORWARD
	_direction_default: int = AP_FORWARD
	_shoot_on: int = 1
	_shoot_on_default: int = 1
	_fps: int = 24
	_fps_default = 24
	
	_resolution: str = "1080p"
	_resolution_default: str = "1080p"
	_projection: str = "HDTV"
	_projection_default: str = "HDTV"
	_pillar_displacement: int = 0
	_pillar_displacement_default = 0
	_letterbox_displacement: int = 0
	_leterbox_displacement_default = 0
	_image_width: int = 1920
	_image_width_default: int = 1920
	_image_height: int = 1080
	_image_height_default: int = 1080
	
	@property
	def direction(self):
		return self._direction
	
	@direction.setter
	def direction(self, value):
		if type(value) == AP_FORWARD or value == AP_REVERSE:
			self._direction = value
		else:
			self._direction = self._direction_default

	@property
	def shoot_on(self):
		return self._shoot_on
	
	@shoot_on.setter
	def shoot_on(self, value):
		if value > 0 and value < 10:
			self._shoot_on = value
		else:
			self._shoot_on = self._shoot_on_default
	
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
	def resolution(self):
		return self._resolution
	
	@resolution.setter
	def resolution(self, value):
		if type(value) == str:
			self._resolution = value
		else:
			self._resolution = self.resolution_default

	@property
	def projection(self):
		return self._projection
	
	@projection.setter
	def projection(self, value):
		if type(value) == str:
			self._projection = value
		else:
			self._projection = self.projection_default
	
	@property
	def pillar_displacement(self):
		return self._pillar_displacement
	
	@pillar_displacement.setter
	def pillar_displacement(self, value):
		if type(value) == int:
			self._pillar_displacement = value
		else:
			self._pillar_displacement = self._pillar_displacement_default

	@property
	def letterbox_displacement(self):
		return self._letterbox_displacement
	
	@letterbox_displacement.setter
	def letterbox_displacement(self, value):
		if type(value) == int:
			self._letterbox_displacement = value
		else:
			self._letterbox_displacement = self._letterbox_default

	@property
	def original_image_width(self):
		return self._image_width
	
	@original_image_width.setter
	def original_image_height(self, value):
		if type(value) == int:
			self._image_height = value
		else:
			self._image_height = self._image_height_default


## testing
if __name__ == "__main__":
	settings = APSettings()
	print("test direction:")
	settings.direction = -2
	print("\tsetting to -2: ", settings.direction)
	settings.direction = -1
	print("\tsetting to -1: ", settings.direction)

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

	print("test pillar displacement:")
	settings.pillar_displacement = 870
	print("\tset to 870 - " + str(settings.pillar_displacement))

	print("test resolution:")
	settings.resolution = "8k"
	print("\tset to 8k: ", settings.resolution)


