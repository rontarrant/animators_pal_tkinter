from tkinter import *
from tkinter import ttk

class HelpMenu(Menu):
	## attributes
	label_text = "Help"
	
	def __init__(self, menubar):
		super().__init__(menubar)
		items = self.index ## shortcut to item index
		## configure stuff
		self.add_command(label = "Help", command = self.help_help)
		
		self.add_command(label = "About", command = self.help_about)
		
	def help_help(self):
		print("showing help dialog")
	
	def help_about(self):
		print("showing about dialog")
