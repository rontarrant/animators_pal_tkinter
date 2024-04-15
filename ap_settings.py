## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local

## constants
FORWARD: int = 1
REVERSE: int = -1

class APSettings():
	_direction: int = FORWARD
	_direction_default: int = FORWARD ## default: play from first frame to last
	_shoot_on: int = 1
	_shoot_on_default: int = 1 ## default: each image held for one frame
	_fps: int = 24
	_fps_default = 24	## default: 24 frames per second
	_crop_to: int = [] ## 2-element list for frame ratio (16:9, 3:4, etc.)
	_resize_to: int = [] ## 2-element list for frame size (8k, 6k, 4k, etc.)
	_aspect_ratio: str = "16:9"
	_aspect_ratio_default: str = "16:9" ## default: HD
	_resolution: int = [1920, 1080]
	_resolution_default: int = [1920, 1080] ## default: HD
	
	def get_aspect_ratio(self):
		return self._aspect_ratio
	
	def set_aspect_ratio(self, value):
		if type(value) == str:
			self._aspect_ratio = value
		else:
			self._aspect_ratio = self._aspect_ratio_default
	
	def get_resolution(self):
		return self._resolution
	
	def set_resolution(self, value):
		if type(value) == list:
			if len(value) == 2:
				self._resolution = value
			else:
				self._resolution = self.resolution_default
	
	def get_direction(self):
		print("get direction: ", self._direction)
		return self._direction
	
	def set_direction(self, value):
		if type(value) == FORWARD or value == REVERSE:
			self._direction = value
		else:
			self._direction = self._direction_default
		print("set direction: ", self._direction)

	def get_shoot_on(self):
		print("shoot_on: ", self._shoot_on)
		return self._shoot_on
	
	def set_shoot_on(self, value):
		if value > 0 and value < 10:
			self._shoot_on = value
		else:
			self._shoot_on = self._shoot_on_default
		print("shoot_on: ", self._shoot_on)

	def get_fps(self):
		print("fps: ", self._fps)
		return self._fps
	
	def set_fps(self, value):
		if value == 12 or value == 18 or value == 24 or value == 30 or value == 60:
			self._fps = value
		else:
			self._fps = 24
		
		print("fps: ", self._fps)

	def get_crop_to(self):
		return self._crop_to
	
	def set_crop_to(self, value: list[int]):
		if type(value) == list:
			if len(value) == 2:
				self._crop_to = value
	
	def get_resize_to(self):
		return self._resize_to
		
	def set_resize_to(self, value: list[int]):
		if type(value) == list:
			if len(value) == 2:
				self._resize_to = value
				
## testing
if __name__ == "__main__":
	settings = APSettings()
	print("test direction:")
	settings.direction = -2
	print("setting to -2: ", settings.direction)
	settings.direction = -1
	print("setting to -1: ", settings.direction)

	print("test shoot_on:")
	settings.shoot_on = 9
	print("setting to 9: ", settings.shoot_on)
	settings.shoot_on = -2
	print("setting to -2: ", settings.shoot_on)

	print("test fps:")
	settings.fps = 37
	print("setting to 37: ", settings.fps)
	settings.fps = 18
	print("setting to 18:", settings.fps)

	print("test crop_to:")
	settings.crop_to = [1.78, 1]
	print("set to 1.78:1 - " + str(settings.crop_to[0]) + ":" + str(settings.crop_to[1]))

	print("test resize_to:")
	settings.crop_to = [6144, 2226]
	print("set to 6144 x 2226 - width: ", settings.crop_to[0], ", height: ", settings.crop_to[1])

