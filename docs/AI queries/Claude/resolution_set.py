import tkinter as tk
from tkinter import ttk
from observer import Observer
from ap_settings import ap_settings

class ResolutionSet(tk.Frame, Observer):
	def __init__(self, master):
		super().__init__(master)
		self.resolution_var = tk.StringVar()

		self.resolution_menu = ttk.OptionMenu(self,
			self.resolution_var, "Select Resolution",
		  "1920x1080", "1280x720", "640x480", 
		  command = self.on_resolution_change)

		self.resolution_menu.pack()
		ap_settings.add_observer(self)

	def on_resolution_change(self, *args):
		ap_settings.update('option_changed', 'resolution',
			self.resolution_var.get())

	def update(self, *args, **kwargs):
		if args[0] == 'settings_loaded':
		self.resolution_var.set(
			ap_settings.get_property('resolution'))
