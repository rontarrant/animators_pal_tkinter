## This avoids errors wherein we try to update a widget
## before it's instantiated by making sure all widgets
## are drawn before we try to configure them.

class UIReady:
	_instance = None

	@staticmethod
	def get_instance():
		"""
		Static method to access the single instance of UIReady
		"""
		if UIReady._instance is None:
			UIReady._instance = UIReady()
		return UIReady._instance
	
	def __new__(cls, *args, **kwargs):
		if cls._instance is None:
			cls._instance = super().__new__(cls, *args, **kwargs)
		return cls._instance
	
	def __init__(self, *args, **kwargs):
		if not hasattr(self, 'ui_ready'):
			self.ui_ready = False
	
	@property
	def ui_ready(self):
		return self._ui_ready
	
	@ui_ready.setter
	def ui_ready(self, value):
		self._ui_ready = value
	