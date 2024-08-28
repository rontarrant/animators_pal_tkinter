import tkinter as tk
from preview_frame import PreviewFrame
from view_frame import ViewFrame

class MainFrame(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.preview_frame = PreviewFrame(self)
		self.view_frame = ViewFrame(self)

		self.preview_frame.pack(side = tk.LEFT,
									fill = tk.BOTH,
									expand = True)

		self.view_frame.pack(side = tk.RIGHT,
								 fill = tk.BOTH,
								 expand = True)
