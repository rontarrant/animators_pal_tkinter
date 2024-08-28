import tkinter as tk
from tkinter import ttk
from observer import Observer
from ap_settings import ap_settings

class ProjectionSet(tk.Frame, Observer):
	def __init__(self, master):
		super().__init__(master)
		self.projection_var = tk.StringVar()

		self.projection_menu = ttk.OptionMenu(self,
			self.projection_var, "Select Projection", 
			"Perspective", "Orthographic", 
			command = self.on_projection_change)

		self.projection_menu.pack()
		ap_settings.add_observer(self)

	def on_projection_change(self, *args):
		ap_settings.update('option_changed', 'projection',
			self.projection_var.get())

	def update(self, *args, **kwargs):
		if args[0] == 'settings_loaded':
			self.projection_var.set(ap_settings.get_property('projection'))
