import tkinter as tk
from observer import Observable

class UIReady(Observable):
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super().__new__(cls, *args, **kwargs)
		return cls._instance

	def __init__(self):
		if not hasattr(self, '_initialized'):
			self._observers = set()
			self._ui_ready = False
			self.root = None
			self.loading_dialog = None
			self._initialized = True

	@property
	def ui_ready(self):
		return self._ui_ready

	@ui_ready.setter
	def ui_ready(self, value):
		self._ui_ready = value

		if value:
			self.notify_observers()

	def initialize(self, root):
		self.root = root

		# Create a loading dialog
		self.loading_dialog = tk.Toplevel(self.root)
		self.loading_dialog.geometry("200x100")
		loading_label = tk.Label(self.loading_dialog, text="UI not ready")
		loading_label.pack(expand=True)

	def check_ui_ready(self):
		if self.root and self.root.winfo_ismapped():
			self.root.after(500, self.ensure_ui_ready)  # Additional delay to ensure UI is fully drawn
		else:
			self.root.after(100, self.check_ui_ready)

	def ensure_ui_ready(self):
		self.ui_ready = True
		self.loading_dialog.destroy()
		