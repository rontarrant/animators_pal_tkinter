from tkinter import *
from tkinter import ttk

class SettingsMenu(Menu):
	## attributes
	label_text = "Settings"
	
	def __init__(self, menubar):
		super().__init__(menubar)
		## configure stuff
		self.add_command(label= "Hold First", command = self.hold_first)
		self.add_command(label = "Speed", command = self.set_speed)
	
	def hold_first(self):
		print("open Hold First Frame dialog")

	def set_speed(self):
		print("setting speed")

