class Observer:
	def update(self, observable, *args, **kwargs):
		raise NotImplementedError
