import tkinter as tk
from observer import Observer
from apsettings import APSettings

class ResolutionSet(tk.Frame, Observer):
	def __init__(self, master, apsettings):
		tk.Frame.__init__(self, master)
		Observer.__init__(self)
		self.apsettings = apsettings
		self.apsettings.attach(self)
		# ... create OptionMenu and other UI elements

	def update(self, observable, *args, **kwargs):
		# Update UI based on changes in APSettings
		pass

	def on_resolution_change(self, new_resolution):
		# Update APSettings and notify observers
		self.apsettings.update_resolution(new_resolution)
