import tkinter as tk
from ap_settings import APSettings
from resolution_set import ResolutionSet
from projection_set import ProjectionSet

def main():
	root = tk.Tk()
	ap_settings = APSettings()

	# Create UI elements
	resolution_set = ResolutionSet(root, ap_settings)
	projection_set = ProjectionSet(root, ap_settings)

	# Notify APSettings when UI is ready
	def ui_ready():
		ap_settings.notify_observers('ui_ready')

	# Call ui_ready after UI is drawn
	root.after(100, ui_ready)

	root.mainloop()

if __name__ == '__main__':
	main()
