import json
from observer import Observer, Observable

class APSettings(Observer, Observable):
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super(APSettings, cls).__new__(cls)
			cls._instance._initialized = False
		return cls._instance

	def __init__(self):
		if self._initialized:
			return
		Observable.__init__(self)
		self._settings = {}
		self._ui_ready = False
		self._initialized = True

	def load_settings(self):
		try:
			with open('settings.json', 'r') as f:
				self._settings = json.load(f)
		except FileNotFoundError:
			self._settings = {}  # Use default settings if file
										# doesn't exist
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
