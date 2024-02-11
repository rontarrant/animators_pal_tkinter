'''
Video Canvas
Displays a flipbook of CVImages collected in a TKImageCollection. 
'''
class VideoCanvas():
	fps: int = 24 ## can also be 18, 25, or 30
	shoot_on: int = 1 ## 1's, 2's, 3's up to 9's
	width: int = 1920 ## default: HD
	height: int = 1080 ## default: HD
	direction: int = 1 ## default: forward (-1 = reverse)
	first_frame_hold: int = 1 ## anything from 1 to 90
	last_frame_hold: int = 1 ## anything from 1 to 90
	
	def __init__(self):
		pass
	
	def play_forward(self):
		pass
	
	def play_reverse(self):
		pass
	
	def stop(self):
		pass
	
	def go_to_frame(self):
		pass
	
	def step_forward(self):
		pass
	
	def step_reverse(self):
		pass
	
	