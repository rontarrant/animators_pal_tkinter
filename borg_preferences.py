## example of the Borg Idiom used for globally-accessible
## settings.
import os, sys

class Borg:
	_shared_state = {}
	
	def __init__(self):
		self.__dict__ = self._shared_state
		
class Preferences(Borg):
	_images_location = None
	_image_file_name_list = None
	_video_location = None
	_video_file_name = None
	_image_resolution = {"width": 1920, "height": 1080} ## default
	_video_resolution = {"width": 1920, "height": 1080} ## default
	_project_state = ("unsaved", "saved")
	_letterbox_effect = (True, False)
	_fps = 24 ## default
	_direction = 1 ## default
	_hold_first = 1 ## default
	_shoot_on = 1 ## default
	_hold_last = 1 ## default
	
	def __init__(self):
		Borg.__init__(self)
		
	def __str__(self):
		fps = "fps: " + str(self.fps) + "\n"
		direction = "direction: " + str(self.direction) + "\n"
		hold_first = "hold first: " + str(self.hold_first) + "\n"
		shoot_on = "shoot on: " + str(self.shoot_on) + "'s\n"
		hold_last = "hold last: " + str(self.hold_last) + "\n"
		return fps + direction + hold_first + shoot_on + hold_last
	
	@property
	def video_file_name(self):
		return self._video_file_name
	
	@video_file_name.setter
	def video_file_name(self, value: str):
		print("value: ", value)
		if isinstance(value, str):
			print("isinstance...")
			self._video_file_name = value
		else:
			## error - not a string
			pass
	
	@property
	def video_location(self):
		return _video_location
	
	@video_location.setter
	def video_location(self, value):
		if isinstance(value, str):
			self._video_location = value
		else:
			## error - not a string
			pass
	
	@property
	def image_file_name_list(self):
		return self._images_location
	
	@image_file_name_list.setter
	def image_file_name_list(self, value):
		if isinstance(value, str):
			self._image_file_name_list = value
		else:
			## error - not a string
			pass
	
	@property
	def images_location(self):
		return self._images_location
	
	@images_location.setter
	def images_location(self, value):
		if isinstance(value, str):
			self._images_location = value
		else:
			## error - not a string
			pass
	
	@property
	def fps(self):
		return self._fps
	
	@fps.setter
	def fps(self, new_fps):
		if new_fps == 18 or new_fps == 24 or new_fps == 30:
			self._fps = new_fps
		else:
			## return error: fps out of bounds
			pass
	
	@property
	def direction(self):
		return self._direction
	
	@direction.setter
	def direction(self, new_direction):
		if new_direction == 1 or new_direction == -1:
			self._direction = new_direction
		else:
			## error: improper direction
			pass
	
	@property
	def hold_first(self):
		return self._hold_first
	
	@hold_first.setter
	def hold_first(self, hold_length):
		if hold_length < 90 and hold_lenth < 1:
			self._hold_first = hold_length
		else:
			## return error: hold length out of bounds
			pass
	
	@property
	def shoot_on(self):
		return self._shoot_on
		
	@shoot_on.setter
	def shoot_on(self, value):
		if value > 10 or value < 1:
			## error - value too lower
			pass
		else:
			self._shoot_on = value
	
	@property
	def hold_last(self):
		return self._hold_last

	@hold_last.setter
	def hold_last(self, hold_length):
		if hold_length < 90:
			self._hold_last = hold_length
		else:
			## return error: hold length out of bounds
			pass
			
## testing
if __name__ == "__main__":
	a = Preferences()
	b = Preferences()
	print("a:\n", a, "\n\nb:\n", b)
	b.fps = 30
	c = Preferences()
	print("a:\n", a, "\n\nb:\n", b, "c:\n", c, "\n\n")
	a.fps = 18
	b.direction = -1
	print(f"fps: {c.fps}")
	b.shoot_on = 3
	print("a:\n", a, "\n\nb:\n", b, "c:\n", c, "\n\n")
