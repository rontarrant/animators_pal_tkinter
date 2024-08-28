import tkinter as tk
from apsettings import APSettings
from resolution_set import ResolutionSet
from projection_set import ProjectionSet

class Window(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.apsettings = APSettings()
		self.main_frame = MainFrame(self)
		# ... rest of the window setup

class MainFrame(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		# ... rest of the frame setup

class ViewFrame(tk.Frame):
	def __init__(self, master):
		tk.Frame.__init__(self, master)
		# ... rest of the frame setup

# ... other frame classes
