class Player():
	FIRST_FRAME = -3 ## goto start frame
	PREV_FRAME = -2 ## goto previous frame
	REVERSE = -1 ## play backwards
	STOP = 0 ## halt playback and goto start frame
	PLAY = 1 ## play forward
	NEXT_FRAME = 2 ## goto next frame
	LAST_FRAME = 3 ## goto last frame
	PAUSE = 4 ## stop playback and stay on current frame
	LOOP_ON = True
	LOOP_OFF = False
	loop_status = False ## either on or off
	status = STOP

	def video_mode(self, status):
		match status:
			case (self.PLAY, self.LOOP_OFF):
				print("playing")
			case (self.REVERSE, self.LOOP_OFF):
				print("reversing")
			case (self.PLAY, self.LOOP_ON):
				print("playing & looping")
			case (self.REVERSE, self.LOOP_ON):
				print("reversing and looping")
			case (self.STOP, self.LOOP_ON | self.LOOP_OFF):
				print("stopped")
			case (self.FIRST_FRAME, self.LOOP_ON | self.LOOP_OFF):
				print("going to first frame")
			case (self.LAST_FRAME, self.LOOP_ON | self.LOOP_OFF):
				print("going to last frame")
			case (self.NEXT_FRAME, self.LOOP_ON | self.LOOP_OFF):
				print("going to next frame")
			case (self.PREV_FRAME, self.LOOP_ON | self.LOOP_OFF):
				print("going to previous frame")
			case (self.PAUSE, self.LOOP_ON | self.LOOP_OFF):
				print("paused")

Player.video_mode(Player, (Player.PLAY, Player.loop_status)) ## playing
Player.loop_status = True
Player.video_mode(Player, (Player.PLAY, Player.loop_status)) ## playing loop
Player.loop_status = False
Player.video_mode(Player, (Player.REVERSE, Player.loop_status)) ## reverse
Player.loop_status = True
Player.video_mode(Player, (Player.REVERSE, Player.loop_status)) ## reverse loop
Player.loop_status = False
Player.video_mode(Player, (Player.STOP, Player.loop_status)) ## stopped
Player.loop_status = True
Player.video_mode(Player, (Player.PREV_FRAME, Player.loop_status)) ## previous frame
Player.video_mode(Player, (Player.NEXT_FRAME, Player.loop_status)) ## next frame
Player.video_mode(Player, (Player.LAST_FRAME, Player.loop_status)) ## last frame
Player.video_mode(Player, (Player.PAUSE, Player.loop_status)) ## paused



