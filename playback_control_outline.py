## outline for handling playback control buttons
def playback_control(self, button_id, mode, direction, frame_number)
	match button_id:
		case APVideoFlags.LOOP_ID: ## swap loop state
			match loop_state:
				case APVideoFlags.LOOP_ON:
					## set loop_state = off
					loop_state = APVideoFlags.LOOP_OFF
				case APVideoFlags.LOOP_OFF:
					## set loop_state = on
					loop_state = APVideoFlags.LOOP_ON
		case _: ## everything except APVideoFlags.LOOP_ID
			## call VideoCanvas.show_next_frame(frame_number)
			## (********* or should this come last? **************)
			
			match mode:
				case APVideoFlags.PLAY:
					match direction:
						case APVideoFlags.DIRECTION_FORWARD:
							match loop_state:
								case APVideoFlags.LOOP_ON:
									if frame_number == last_frame:
										frame_number = 0
									else:
										frame_number += 1
								case APVideoFlags.LOOP_OFF:
									if frame_number == last_frame:
										mode = halt_mode
									else:
										frame_number += 1
						case APVideoFlags.DIRECTION_REVERSE:
							match loop_state:
								case APVideoFlags.LOOP_ON:
									if frame_number == first_frame:
										frame_number = 0
									else:
										frame_number -= 1
								case APVideoFlags.LOOP_OFF:
									if frame_number == first_frame:
										mode = halt_mode
									else:
										frame_number -= 1
				case APVideoFlags.HALT:
					match button_id: ## FORWARD_PAUSE, REVERSE_PAUSE, FORWARD_STOP, REVERSE_STOP, GOTO_END, GOTO_START
						case APVideoFlags.FORWARD_PAUSE_ID:
							## change forward button image from Pause to Play
						case APVideoFlags.REVERSE_PAUSE_ID:
							## change reverse button image from Pause to Play
						case APVideoFlags.FORWARD_STOP_ID:
							## change forward button image from Pause to Play
						case APVideoFlags.REVERSE_STOP_ID:
							## change reverse button image from Pause to Play
						case APVideoFlags.GOTO_END_ID:
							## no button image change
						case APVideoFlags.GOTO_START_ID:
							## no button image change

if __name__ == "__main__":
	pass
