import tkinter as tk
from MainFrame import MainFrame
from APSettings import ap_settings

class App(tk.Tk):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.main_frame = MainFrame(self)
		self.main_frame.pack()

		# Load saved properties from a JSON file
		ap_settings.update_from_json("settings.json")

if __name__ == "__main__":
	app = App()
	app.mainloop()
