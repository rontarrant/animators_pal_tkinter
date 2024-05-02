## This avoids errors wherein we try to update a widget
## before it's instantiated by making sure all widgets
## are drawn before we try to configure them.

class UIReady():
	ui_ready = False

	def __init__(self, *args, **kwargs):
		pass
		
	def set(self):
		self.ui_ready = True
