## example of the Borg Idiom

class Borg:
	_shared_state = {}
	
	def __init__(self):
		self.__dict__ = self._shared_state

if __name__ == "__main__":
	class Example(Borg):
		def __init__(self, name = None):
			Borg.__init__(self)
			
			if name is not None:
				self.name = name
			
		def __str__(self):
			return 'Example(%s)' % self.name

a = Example("Lara")
b = Example()
print("a: ", a, " b: ", b)
c = Example("Boris")
print("a: ", a, " b: ", b, " c: ", c)
b.name = "Marcel"
print("a: ", a, " b: ", b, " c: ", c)
