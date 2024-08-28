import json
from observable import Observable
from observer import Observer

class APSettings(Observable, Observer):
	def __init__(self):
		super().__init__()
		self.properties = {}

	def load_properties(self, filename):
		with open(filename, 'r') as f:
			self.properties = json.load(f)
		self.notify_observers('load_properties')

	def save_properties(self, filename):
		with open(filename, 'w') as f:
			json.dump(self.properties, f)

	def update_property(self, name, value):
		self.properties[name] = value
		self.notify_observers('update_property', name, value)

	def update(self, observable, *args, **kwargs):
		if observable == 'ui_ready':
			self.load_properties('settings.json')
		elif observable == 'option_menu':
			self.update_property(*args, **kwargs)
