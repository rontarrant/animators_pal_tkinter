import tkinter as tk
from APSettings import ap_settings

class ProjectionSet(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)

		self.option_menu = tk.OptionMenu(self, tk.StringVar(), 					"Perspective", "Orthographic")

self.option_menu.pack()

ap_settings.add_observer(self)

		# Track user selection
self.option_menu_var = tk.StringVar()
self.option_menu_var.trace("w", self.on_option_changed)

def on_option_changed(self, *args):
	selected_value = self.option_menu_var.get()
 	ap_settings.update_property("projection", selected_value)

	def update(self, key, value):
		if key == "projection":
			self.option_menu_var.set(value)
		elif key == "ui_loaded":
			self.load_initial_value()

	def load_initial_value(self):
		# Update OptionMenu based on APSettings

		projection = ap_settings.properties.get("projection", 					"Perspective")

		self.option_menu_var.set(projection)
