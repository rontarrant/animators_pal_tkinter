## ap_video_flags
####################
## TODO
##################
## - make sure all flags are needed
## - change MODE_PLAY to MODE_FORWARD
## - add MODE_REVERSE

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
		APVideoFlags.MODE_FORWARD = "MODE PLAY"
		APVideoFlags.MODE_HALT = "MODE HALT"
		APVideoFlags.MODE_REVERSE = "MODE REVERSE"
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
		APVideoFlags.LOOPING = "LOOPING OFF"
		## loop switch IDs
		APVideoFlags.LOOPING_ON = "LOOPING ON"
		APVideoFlags.LOOPING_OFF = "LOOPING OFF"
		

### testing
if __name__ == "__main__":
	flags = APVideoFlags.get_instance()
	print("before", flags.reverse_button_pressed)
	flags.reverse_button_pressed = True
	print("after", flags.reverse_button_pressed)
	flags.reverse_button_pressed = False
	print("after-after", flags.reverse_button_pressed)
