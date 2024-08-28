import json
from observer import Observer, Observable

class APSettings(Observer, Observable):
	def __init__(self):
		Observable.__init__(self)
		self._settings = {}
		self._ui_ready = False

	def load_settings(self):
		with open('settings.json', 'r') as f:
			self._settings = json.load(f)
		if self._ui_ready:
			self.notify_observers('settings_loaded')

	def save_settings(self):
		with open('settings.json', 'w') as f:
			json.dump(self._settings, f)

	def update(self, observable, *args, **kwargs):
		if args[0] == 'ui_ready':
			self._ui_ready = True
			self.load_settings()
		elif args[0] == 'option_changed':
			self._settings[args[1]] = args[2]
			self.save_settings()

	def get_setting(self, key):
		return self._settings.get(key)

ap_settings = APSettings()  # Singleton instance
