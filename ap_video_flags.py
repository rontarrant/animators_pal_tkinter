## ap_video_flags

class APVideoFlags():
	# Create a private class attribute to store the single instance
	__instance = None
	
	@staticmethod
	def get_instance():
		"""
		Static method to access the single instance of APVideoFlags
		"""
		if APVideoFlags.__instance is None:
			APVideoFlags.__instance = APVideoFlags()

		return APVideoFlags.__instance

	def __init__(self):
		## modes
		APVideoFlags.MODE_PLAY = "MODE PLAY"
		APVideoFlags.MODE_HALT = "MODE HALT"
		APVideoFlags.MODE_NONE = "MODE NONE"
		## video control buttons
		APVideoFlags.STOP_ID = "STOP"
		APVideoFlags.FORWARD_PLAY_ID = "FORWARD PLAY"
		APVideoFlags.FORWARD_PAUSE_ID = "FORWARD PAUSE"
		APVideoFlags.FORWARD_STOP_ID = "FORWARD STOP"
		APVideoFlags.REVERSE_PLAY_ID = "REVERSE PLAY"
		APVideoFlags.REVERSE_PAUSE_ID = "REVERSE PAUSE"
		APVideoFlags.REVERSE_STOP_ID = "REVERSE STOP"
		APVideoFlags.REVERSE_STEP_ID = "REVERSE STEP"
		APVideoFlags.FORWARD_STEP_ID = "FORWARD STEP"
		APVideoFlags.GOTO_END_ID = "GO TO END"
		APVideoFlags.GOTO_START_ID = "GO TO START"
		APVideoFlags.LOOP_ID = "LOOP"
		## loop switch IDs
		APVideoFlags.LOOP_ON = "LOOP ON"
		APVideoFlags.LOOP_OFF = "LOOP OFF"
		## directions
		APVideoFlags.DIRECTION_NONE = "DIRECTION NEUTRAL"
		APVideoFlags.DIRECTION_FORWARD = "DIRECTION FORWARD"
		APVideoFlags.DIRECTION_REVERSE = "DIRECTION REVERSE"
		
		## keep track of which play button was pressed
		APVideoFlags._reverse_button_pressed = False
		APVideoFlags._forward_button_pressed = False
	
	@property
	def reverse_button_pressed(self):
		return self._reverse_button_pressed
	
	@reverse_button_pressed.setter
	def reverse_button_pressed(self, value):
		self._reverse_button_pressed = value

	@property
	def forward_button_pressed(self):
		return self._forward_button_pressed
	
	@forward_button_pressed.setter
	def forward_button_pressed(self, value):
		self._forward_button_pressed = value


### testing
flags = APVideoFlags.get_instance()
print("before", flags.reverse_button_pressed)
flags.reverse_button_pressed = True
print("after", flags.reverse_button_pressed)
flags.reverse_button_pressed = False
print("after-after", flags.reverse_button_pressed)
