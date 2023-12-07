from tkinter import *
from tkinter import ttk

class FileMenu(Menu):
	## attributes
	label_text = "File"
	
	def __init__(self, menubar):
		super().__init__(menubar)
		## configure stuff
		self.add_command(label = "New", command = self.file_new)
		self.add_command(label = "Load", command = self.load_file)
	
	def file_new(self):
		print("creating a new file")
	
	def load_file(self):
		print("loading file...")

