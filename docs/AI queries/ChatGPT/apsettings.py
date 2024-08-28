class APSettings:
	_instance = None

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super(APSettings, cls).__new__(cls)
			cls._instance._observers = []
			cls._instance.properties = {}
		return cls._instance

	def add_observer(self, observer):
		self._observers.append(observer)

	def notify_observers(self, key):
		for observer in self._observers:
			observer.update(key, self.properties.get(key))

	def update_property(self, key, value):
		self.properties[key] = value
		self.notify_observers(key)

	def update_from_json(self, json_file):
		# Load from JSON, then notify observers of updates
		pass

	def notify_ui_loaded(self):
		# Called when the UI finishes loading
		self.notify_observers("ui_loaded")

## Singleton pattern ensures APSettings is globally accessible.
ap_settings = APSettings()
