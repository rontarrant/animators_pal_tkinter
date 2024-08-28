import tkinter as tk
from resolution_set import ResolutionSet
from projection_set import ProjectionSet

class VideoImageInfoSet(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.resolution_set = ResolutionSet(self)
		self.projection_set = ProjectionSet(self)
		self.resolution_set.pack(fill = tk.X)
		self.projection_set.pack(fill = tk.X)
