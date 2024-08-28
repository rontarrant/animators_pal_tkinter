from observer import Observer

class UIElement(Observer):
	def __init__(self, ap_settings):
		self.ap_settings = ap_settings
		self.ap_settings.register_observer(self)

	def update(self, observable, *args, **kwargs):
		if observable == 'load_properties':
			self.load_properties()
		elif observable == 'update_property':
			self.update_property(*args, **kwargs)

	def load_properties(self):
		raise NotImplementedError

	def update_property(self, name, value):
		raise NotImplementedError
