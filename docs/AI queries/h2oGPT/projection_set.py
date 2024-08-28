from ui_element import UIElement
from tkinter import OptionMenu

class ProjectionSet(UIElement):
	def __init__(self, master, ap_settings):
		super().__init__(ap_settings)
		self.master = master

		self.option_menu = OptionMenu(master, 'option',
			command = self.option_menu_changed)

		self.option_menu.pack()

	def load_properties(self):
		# Load properties from APSettings
		pass

	def update_property(self, name, value):
		if name == 'projection':
			self.option_menu.set(value)

	def option_menu_changed(self, value):
		self.ap_settings.update_property('projection', value)
