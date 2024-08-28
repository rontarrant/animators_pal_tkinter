import tkinter as tk
from ResolutionSet import ResolutionSet
from ProjectionSet import ProjectionSet
from APSettings import ap_settings

class MainFrame(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		
		self.resolution_set = ResolutionSet(self)
		self.projection_set = ProjectionSet(self)

		self.resolution_set.pack(side = "left")
		self.projection_set.pack(side = "right")

		# Notify APSettings when UI is fully loaded
		self.after(0, self.notify_ui_loaded)

	def notify_ui_loaded(self):
		ap_settings.notify_ui_loaded()
