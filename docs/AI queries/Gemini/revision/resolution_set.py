from state_manager import Observer

class ResolutionSet(tk.Frame, Observer):
	def __init__(self, master, state_manager):
		tk.Frame.__init__(self, master)
		self.state_manager = state_manager
		self.state_manager.attach(self)
		# ... create OptionMenu and other UI elements

	def update(self, observable, changed_key):
		if changed_key == 'resolution':
			# Update UI based on changed resolution
			pass
