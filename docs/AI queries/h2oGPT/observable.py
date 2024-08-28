class Observable:
	def __init__(self):
		self.observers = []

	def register_observer(self, observer):
		self.observers.append(observer)

	def remove_observer(self, observer):
		self.observers.remove(observer)

	def notify_observers(self, *args, **kwargs):
		for observer in self.observers:
			observer.update(self, *args, **kwargs)
