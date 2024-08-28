class Observer:
	def update(self, observable):
		pass

class Observable:
	'''
	NOTE: When overriding this __init__() method,
	make sure to add the body statements to the
	override method.
	'''
	def __init__(self):
		self._observers = set() ## put this in the override

	def attach(self, observer):
		self._observers.add(observer)

	def detach(self, observer):
		self._observers.remove(observer) 

	def notify_observers(self):
		for observer in self._observers:
			observer.update()
