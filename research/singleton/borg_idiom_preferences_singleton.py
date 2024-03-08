## example of the Borg Idiom

class Borg:
	_shared_state = {}
	
	def __init__(self):
		self.__dict__ = self._shared_state
		
class Preferences(Borg):
	fps = 24
	direction = 1
	hold_first = 1
	shoot_on = 1
	hold_last = 1
	
	def __init__(self):
		Borg.__init__(self)
		
	def __str__(self):
		return f'fps: {self.fps} direction: {self.direction}'

## testing
if __name__ == "__main__":
	a = Preferences()
	b = Preferences()
	print("a: ", a, " b: ", b)
	b.fps = 30
	c = Preferences()
	print("a: ", a, " b: ", b, " c: ", c)
	a.fps = 18
	print(f"fps: {c.fps}")
	print("a: ", a, " b: ", b, " c: ", c)
