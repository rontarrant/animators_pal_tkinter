import tkinter as tk
from main_frame import MainFrame
from observer import Observable

class Window(tk.Tk, Observable):
	def __init__(self):
		super().__init__()
		Observable.__init__(self)
		self.main_frame = MainFrame(self)
		self.main_frame.pack(fill = tk.BOTH, expand = True)
		self.after(100, self.notify_ui_ready)

	def notify_ui_ready(self):
		self.notify_observers('ui_ready')
