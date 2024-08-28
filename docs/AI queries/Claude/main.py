from window import Window
from ap_settings import ap_settings

if __name__ == "__main__":
	window = Window()
	ap_settings.add_observer(window)
	window.mainloop()
