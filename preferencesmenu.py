from tkinter import *
from tkinter.ttk import *

class PreferencesMenu(Menu):
	## attributes
	label_text = "Preferences"
	direction = "forward"
	fps = 24
	on_holds = 1
	hold_first_frame = 1
	hold_last_frame = 1
	
	def __init__(self, menubar, window):
		super().__init__(menubar)
		items = self.index
		
		## shortcut to item index
		## configure stuff
		self.add_command(label= "Hold First Frame", command = self.hold_first)
		self.entryconfig(items("Hold First Frame"), accelerator = "(Ctrl-F)")
		window.bind('<Control_L><f>', self.hold_first)
		
		self.add_command(label = "Speed (FPS)", command = self.set_fps)
		self.entryconfig(items("Speed (FPS)"), accelerator = "(Ctrl-R)")
		window.bind('<Control_L><r>', self.set_fps)
		
		self.add_command(label = "Frames Hold", command = self.frames_hold)
		self.entryconfig(items("Frames Hold"), accelerator = "(Ctrl-1 to Ctrl-5)")
		window.bind('<Control_L>1', self.frames_hold)
		window.bind('<Control_L>2', self.frames_hold)
		window.bind('<Control_L>3', self.frames_hold)
		window.bind('<Control_L>4', self.frames_hold)
		window.bind('<Control_L>5', self.frames_hold)
		
		self.add_command(label = "Direction", command = self.set_direction)
		self.entryconfig(items("Direction"), accelerator = "(Ctrl-D)")
		window.bind('<Control_L><d>', self.set_direction)
		
		self.add_command(label = "Hold Last Frame", command = self.hold_last)
		self.entryconfig(items("Hold Last Frame"), accelerator = "(Ctrl-L)")
		window.bind('<Control_L><l>', self.hold_last)
		
		self.add_command(label = "Preferences Dialog", command = self.set_preferences)
		self.entryconfig(items("Preferences Dialog"), accelerator = "(Ctrl-P)")
		window.bind('<Control_L><p>', self.set_preferences)

	def set_fps(self, event = None):
		print("dialog for setting speed")

	def frames_hold(self, event = None):
		if event:
			self.on_holds = int(event.keysym)
		else:
			self.on_holds = 1
			
		print("frame holds are: ", self.on_holds)

	def set_direction(self, event = None):
		if self.direction == "forward":
			self.direction = "reverse"
			print("reverse")
		else:
			self.direction = "forward"
			print("forward")
	
	def hold_first(self, event = None):
		print("open Hold First Frame dialog")

	def hold_last(self, event = None):
		print("open Hold Last Frame dialog")

	def set_preferences(self, event = None):
		print("open preferences dialog")
		pref_dialog = PreferencesDialog(self)
		
		if pref_dialog.result:
			##self.fps = pref_dialog.fps
			##self.direction = pref_dialog.direction
			print("fps: ", self.fps)
			print("direction: ", self.direction)
			## fill in preferences


class PreferencesDialog(Toplevel):
	## properties and their defaults
	_fps = 24
	_direction = 1
	_first_frame_hold = 1
	_on_holds = 2
	_last_frame_hold = 1
	_result = None
	_ok_click = None
	_cancel_click = None

	@property
	def result(self):
		return self._result

	@property
	def fps(self):
		return self._fps
	
	@property
	def direction(self):
		return self._direction
		
	@property
	def first_frame_hold(self):
		return self._first_frame_hold
		
	@property
	def on_holds(self):
		return self._on_holds
		
	@property
	def last_frame_hold(self):
		return self._last_frame_hold
		
	def __init__(self, parent, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self._set_properties()
		self._add_widgets()
		##self._fps.focus_set()
		##self.wait_window()
	
	def _add_widgets(self):
		## define the grid
		self.columnconfigure((0, 1), weight = 1)
		self.rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
		## populate
		
		fps_button_set = self.build_fps()
		direction_radiobuttons = self.build_direction()

		## layout
		fps_button_set.grid(row = 0, rowspan = 2, column = 0, sticky = "se", padx = 20)
		direction_radiobuttons.grid(row = 0, rowspan = 2, column =1 , sticky = "sw", padx = 20)
		
		## dialog buttons
		ok_button = Button(self, text = "OK", command = self._on_ok_click)
		ok_button.grid(row = 5, column = 0)
		self.bind("<Return>", self._on_ok_click)
		cancel_button = Button(self, text = "Cancel", command = self._on_cancel_click)
		cancel_button.grid(row = 5, column = 1)
		self.bind("<Escape>", self._on_cancel_click)
	
	def build_fps(self):
		frame = Labelframe(self, text = "fps")
		frame.fps_button_set = []
		frame.fps_var = IntVar()
		
		## populate
		fps1 = Radiobutton(frame, text = "18 fps", variable = frame.fps_var, value = 18)
		fps2 = Radiobutton(frame, text = "24 fps", variable = frame.fps_var, value = 24)
		fps3 = Radiobutton(frame, text = "30 fps", variable = frame.fps_var, value = 30)
		## layout
		frame.fps_button_set.append(fps1)
		frame.fps_button_set.append(fps2)
		frame.fps_button_set.append(fps3)
		## config
		frame.fps_button_set[1].invoke() ## the default
		frame.config(borderwidth = 2, relief = "groove")
		## layout
		for radiobutton in frame.fps_button_set:
			radiobutton.grid(padx = 10)
		
		return frame
			
	def build_direction(self):
		frame = Labelframe(self, text = "direction")
		frame.direction_button_set = []
		frame.direction_var = IntVar()
		
		## populate
		direction1 = Radiobutton(frame, text = "Forward", variable = frame.direction_var, value = 1)
		direction2 = Radiobutton(frame, text = "Reverse", variable = frame.direction_var, value = -1)
		## compile
		frame.direction_button_set.append(direction1)
		frame.direction_button_set.append(direction2)
		## config
		frame.direction_button_set[0].invoke() ## the default
		frame.config(borderwidth = 2, relief = "groove")
		## layout
		for radiobutton in frame.direction_button_set:
			radiobutton.grid(padx = 10)
		
		return frame
		
	def _set_properties(self):
		width = 400
		height = 400
		
		self.title("Animator's Pal Preferences")
		self.geometry(f"{width}x{height}")
		self.resizable(False, False)

		self.bind("<Return>", self._ok_click)
		self.bind("<Escape>", self._cancel_click)

	def _on_cancel_click(self, event = None):
		self._text = None
		self._result = False
		self.destroy()

	def _on_ok_click(self, event = None):
		self._result = True
		self.destroy()
