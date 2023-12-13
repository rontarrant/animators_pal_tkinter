from tkinter import *
from tkinter import ttk

class SettingsMenu(Menu):
	## attributes
	label_text = "Settings"
	direction = "forward"
	fps = 24
	frame_holds = 1
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
		
		self.add_command(label = "FPS Rate", command = self.set_fps)
		self.entryconfig(items("FPS Rate"), accelerator = "(Ctrl-R)")
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

	def set_fps(self, event = None):
		print("dialog for setting speed")

	def frames_hold(self, event = None):
		if event:
			self.frame_holds = int(event.keysym)
		else:
			self.frame_holds = 1
			
		print("frame holds are: ", self.frame_holds)

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

