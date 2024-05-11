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
		APVideoFlags.PLAY = 1
		APVideoFlags.HALT = 0
		APVideoFlags.FORWARD_PLAY_ID = 100
		APVideoFlags.FORWARD_PAUSE_ID = 110
		APVideoFlags.FORWARD_STOP_ID = 120
		APVideoFlags.REVERSE_PLAY_ID = 200
		APVideoFlags.REVERSE_PAUSE_ID = 210
		APVideoFlags.REVERSE_STOP_ID = 220
		APVideoFlags.GOTO_END_ID = 300
		APVideoFlags.GOTO_START_ID = 400
		
		APVideoFlags.LOOP_ID = 500
		APVideoFlags.LOOP_ON = 510
		APVideoFlags.LOOP_OFF = 520
		
		APVideoFlags.DIRECTION_FORWARD = 600
		APVideoFlags.DIRECTION_REVERSE = 610
		