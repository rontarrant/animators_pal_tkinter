import tkinter as tk
from video_image_info_set import VideoImageInfoSet

class ViewFrame(tk.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.video_image_info_set = VideoImageInfoSet(self)
		self.video_image_info_set.pack(fill = tk.BOTH, expand = True)
