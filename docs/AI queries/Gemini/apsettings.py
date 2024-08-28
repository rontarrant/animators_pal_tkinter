import json
from observer import Observable, Observer

class APSettings(Observable, Observer):
	def __init__(self):
		Observable.__init__(self)
		Observer.__init__(self)
		self.settings = {}

	def load_settings(self):
		# Load settings from JSON file
		pass

	def save_settings(self):
		# Save settings to JSON file
		pass

	def update(self, observable, *args, **kwargs):
		# Update internal settings based on changes from observable
		pass

	def notify_settings_changed(self, property_name):
		# Notify observers about changes in specific property
		pass
