## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## local
from set_fps_radio import FPSRadioSet
from set_direction_radio import DirectionRadioSet
from set_shoot_on import ShootOnSet
from set_frame_hold import FrameHoldSet
from set_preferences import Preferences

## constants
FORWARD: int = 1
REVERSE: int = -1

class APSettings():
	_direction: int = FORWARD ## default: play from first frame to last
	_direction_default: int = FORWARD
	_shoot_on: int = 1 ## default: every frame different
	_shoot_on_default: int = 1
	_fps: int = 24 ## default: 24 frames per second
	_crop_to: int = [] ## 2-element list for frame ratio (16:9, 3:4, etc.)
	_resize_to: int = [] ## 2-element list for frame size (8k, 6k, 4k, etc.)
	
	@property
	def direction(self):
		return self._direction
	
	@direction.setter
	def direction(self, value):
		if value == FORWARD or value == REVERSE:
			self._direction = value
		else:
			## set to default
			self._direction = self._direction_default

	@property
	def shoot_on(self):
		return self._shoot_on
	
	@shoot_on.setter
	def shoot_on(self, value):
		if value > 0 and value < 10:
			self._shoot_on = value
		else:
			## set to default
			self._shoot_on = self._shoot_on_default

	@property
	def fps(self):
		return self._fps
	
	@fps.setter
	def fps(self, value):
		if value == 12 or value == 18 or value == 24 or value == 30 or value == 60:
			self._fps = value
		else:
			self._fps = 24 ## set to default on error

	@property
	def crop_to(self):
		return self._crop_to
	
	@crop_to.setter
	def crop_to(self, value: list[int]):
		if type(value) == list:
			if len(value) == 2:
				self._crop_to = value
	
	@property
	def resize_to(self):
		return self._resize_to
		
	@resize_to.setter
	def resize_to(self, value: list[int]):
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

