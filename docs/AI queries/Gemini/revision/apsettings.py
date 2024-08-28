import json
from state_manager import StateManager

class APSettings(StateManager):
	def __init__(self):
		super().__init__()
		self.load_settings()

	def load_settings(self):
		# Load settings from JSON file
		pass

	def save_settings(self):
		# Save settings to JSON file
		pass
