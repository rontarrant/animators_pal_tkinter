## example of the Borg Idiom used for globally-accessible
## settings.
import os, sys

class Borg:
	_shared_state = {}
	
	def __init__(self):
		self.__dict__ = self._shared_state
		
class Preferences(Borg):
	images_location = StringVar()
	image_file_name_list = StringVar()
	video_location = StringVar()
	video_file_name = StringVar()
	image_resolution = {"width": 1920, "height": 1080} ## default
	video_resolution = {"width": 1920, "height": 1080} ## default
	project_state = ("unsaved", "saved")
	letterbox_effect = (True, False)
	fps = 24 ## default
	direction = 1 ## default
	hold_first = 1 ## default
	shoot_on = 1 ## default
	hold_last = 1 ## default
	
	def __init__(self):
		Borg.__init__(self)
	
	def __str__(self):
		return str((self.fps, self.direction, self.hold_first, self.shoot_on, self.hold_last))
		
	def get_fps(self):
		return self.fps
	
	def get_direction(self):
		return self.direction
	
	def get_hold_first(self):
		return self.hold_first
	
	def get_shoot_on(self):
		return self.shoot_on
	
	def get_hold_last(self):
		return self.hold_last

	def set_fps(self, value):
		self.fps = value
	
	def set_direction(self, value):
		self.direction = value
	
	def set_hold_first(self, value):
		self.hold_first = value
	
	def set_shoot_on(self, value):
		self.shoot_on = value
	
	def set_hold_last(self, value):
		self.hold_last = value

## testing
if __name__ == "__main__":
	a = Preferences()
	b = Preferences()
	print("a: ", a, "b: ", b)
	b.set_fps(30)
	c = Preferences()
	print("a: ", a, "\nb: ", b, "c: ", c)
	a.set_fps(18)
	b.set_direction(-1)
	print(f"fps: {c.get_fps()}")
	b.set_shoot_on(3)
	print("a: ", a, "\nb: ", b, "c: ", c)
