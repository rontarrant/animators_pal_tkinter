import tkinter as tk
from tkinter import ttk
from observer import Observer
from ap_settings import ap_settings

class ResolutionSet(tk.Frame, Observer):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		Observer.__init__(self)
		self.resolution_var = tk.StringVar()
		self.resolution_menu = ttk.OptionMenu(self, self.resolution_var, "Select Resolution", "1080p", "720p", "480p", command = self.on_resolution_change)
		self.resolution_menu.pack()
		ap_settings.add_observer(self)

	def on_resolution_change(self, *args):
		ap_settings.update(self, 'option_changed', 'resolution', self.resolution_var.get())

	def update(self, observable, *args, **kwargs):
		if args[0] == 'settings_loaded':
			self.resolution_var.set(ap_settings.get_setting('resolution'))
