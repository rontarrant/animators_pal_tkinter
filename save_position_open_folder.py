import tkinter as tk
from tkinter import filedialog
import json
import os

class MainWindow(tk.Tk):
	def __init__(self):
		super().__init__()
		self.settings_file = "settings.json"
		self.settings = self.load_settings()
		
		# Set initial window size
		self.geometry("300x300")
      
		self.load_window_position()
		self.protocol("WM_DELETE_WINDOW", self.on_close)
		
		# Button to open the file dialog
		self.open_button = tk.Button(self, text="Open Image", command=self.open_file)
		self.open_button.pack(pady=20)
	
	def save_settings(self):
		x = self.winfo_x()
		y = self.winfo_y()
		self.settings['window_position'] = {'x': x, 'y': y}
		with open(self.settings_file, "w") as file:
			json.dump(self.settings, file)
	
	def load_settings(self):
		if os.path.exists(self.settings_file):
			with open(self.settings_file, "r") as file:
				return json.load(file)
		return {}
	
	def load_window_position(self):
		if 'window_position' in self.settings:
			pos = self.settings['window_position']
			self.geometry(f"+{pos['x']}+{pos['y']}")

	def on_close(self):
		self.save_settings()
		self.destroy()

	def open_file(self):
		initial_dir = self.settings.get('last_opened_folder', '.')
		file_path = filedialog.askopenfilename(initialdir=initial_dir)
		if file_path:
			self.settings['last_opened_folder'] = os.path.dirname(file_path)
			self.save_settings()

if __name__ == "__main__":
	app = MainWindow()
	app.mainloop()
