import tkinter as tk
from main_frame import MainFrame
from ap_settings import APSettings

class Window(tk.Tk):
	def __init__(self):
		super().__init__()
		self.ap_settings = APSettings()  # Get the singleton instance
		self.main_frame = MainFrame(self)
		self.main_frame.pack(fill = tk.BOTH, expand = True)
		self.after(100, self.notify_ui_ready)

	def notify_ui_ready(self):
		self.ap_settings.update(self, 'ui_ready')
