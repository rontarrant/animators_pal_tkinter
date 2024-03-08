class Singleton:
	""" A Pythonic Singleton """
	
	class __impl:
		""" Implementation of the Singleton class """
		def spam(self):
			""" Just an example method that returns Singleton instance's ID """
			return id(self)
			
	# The private class attribute holding the "one and only instance"
	__instance = __impl( )
			
	def __getattr__(self, attr):
		return getattr(self.__instance, attr)
			
	def __setattr__(self, attr, value):
		return setattr(self.__instance, attr, value)

if __name__ == "__main__":
	s1 = Singleton()
	print(id(s1), s1.spam())
	
	s2 = Singleton()
	print(id(s2), s2.spam())
