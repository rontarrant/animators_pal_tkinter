## Python
import os
import sys
## tkinter
from tkinter import *
from tkinter.ttk import *

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)

## local
from ap_constants import *
'''
Following is a list of the class properties in APSettings:
Video Playback Settings
_direction:
	: determines the order the loaded images
	: will be written to the final video file
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
	# Create a private class attribute to store the single instance
	__instance = None
	
	@staticmethod
	def get_instance():
		"""
		Static method to access the single instance of APSettings
		"""
		if APSettings.__instance is None:
			APSettings.__instance = APSettings()

		return APSettings.__instance

	def __init__(self, *args, **kwargs):
		## Use the name of the class to declare class variables
		## within a class method.
		## use the 'value' keyword to avoid error:
		##   object has no attribute '_root'
		APSettings._direction = IntVar(value = AP_FORWARD)
		APSettings._direction_default = IntVar(value = AP_FORWARD)
		APSettings._shoot_on = IntVar(value = 1)
		APSettings._shoot_on_default = IntVar(value = 1)
		APSettings._fps = IntVar(value = 24)
		APSettings._fps_default = IntVar(value = 24)
		APSettings._delay = int(round(1000 / 24))
		
		APSettings._resolution = StringVar(value = "1080p (1920x1080)")
		APSettings._resolution_default = StringVar(value = "1080p (1920x1080)")
		APSettings._projection = StringVar(value = "HDTV (16:9)")
		APSettings._projection_default = StringVar(value = "HDTV (16:9)")
		APSettings._pillar_displacement = IntVar(value = 0)
		APSettings._pillar_displacement_default = IntVar(value = 0)
		APSettings._letterbox_displacement = IntVar(value = 0)
		APSettings._letterbox_displacement_default = IntVar(value = 0)

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

	## For some reason, this refuses to work as an IntVar()
	## So this gives direct access instead of using .get()
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
		##ic(value)
		
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

## testing
if __name__ == "__main__":
	## a window has to exist to use tkinter variables,
	## but doesn't have to be used 
	root = Tk()
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


