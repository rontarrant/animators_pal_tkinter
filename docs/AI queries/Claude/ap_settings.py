import json
from observer import Observable, Observer

class APSettings(Observable, Observer):
	def __init__(self):
		Observable.__init__(self)
		self.properties = {}
		self.ui_ready = False

	def load_settings(self):
		with open('settings.json', 'r') as f:
			self.properties = json.load(f)
		if self.ui_ready:
			self.notify_observers('settings_loaded')

	def save_settings(self):
		with open('settings.json', 'w') as f:
			json.dump(self.properties, f)

	def update(self, *args, **kwargs):
		if args[0] == 'ui_ready':
			self.ui_ready = True
			self.load_settings()
		elif args[0] == 'option_changed':
			self.properties[args[1]] = args[2]
			self.save_settings()

	def get_property(self, key):
		return self.properties.get(key)

ap_settings = APSettings()
