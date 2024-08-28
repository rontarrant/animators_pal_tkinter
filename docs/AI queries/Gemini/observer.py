class Observer:
	def update(self, observable, *args, **kwargs):
		raise NotImplementedError

class Observable:
	def __init__(self):
		self._observers = set()

	def attach(self, observer):
		self._observers.add(observer)

	def detach(self, observer):
		self._observers.remove(observer)  

	def notify_observers(self, *args, **kwargs):
		for observer in self._observers:
			observer.update(self,   *args, **kwargs)
