from ap_video_flags import *

## for debugging
from icecream import install
install()
ic.configureOutput(includeContext = True)


## outline for handling playback control buttons
def playback_control(button_id, mode, direction, frame_number):
	global loop_state
	global last_frame
	
	match button_id:
		case flags.LOOP_ID: ## swap loop state
			match loop_state:
				case flags.LOOP_ON:
					## set loop_state = off
					loop_state = flags.LOOP_OFF
					## ic("loop is OFF")
				case flags.LOOP_OFF:
					## set loop_state = on
					loop_state = flags.LOOP_ON
					## ic("loop is ON")
		case _: ## everything except flags.LOOP_ID
			## call VideoCanvas.show_next_frame(frame_number)
			## (********* or should this come last? **************)
			
			match mode:
				case flags.PLAY:
					match direction:
						case flags.DIRECTION_FORWARD:
							match loop_state:
								case flags.LOOP_ON:
									if frame_number == last_frame:
										frame_number = 0
									else:
										frame_number += 1
								case flags.LOOP_OFF:
									if frame_number == last_frame:
										mode = halt_mode
									else:
										frame_number += 1
						case flags.DIRECTION_REVERSE:
							match loop_state:
								case flags.LOOP_ON:
									if frame_number == first_frame:
										frame_number = 0
									else:
										frame_number -= 1
								case flags.LOOP_OFF:
									if frame_number == first_frame:
										mode = halt_mode
									else:
										frame_number -= 1
				case flags.HALT:
					match button_id: ## FORWARD_PAUSE, REVERSE_PAUSE, FORWARD_STOP, REVERSE_STOP, GOTO_END, GOTO_START
						case flags.FORWARD_PAUSE_ID:
							## change forward button image from Pause to Play
							## ic()
						case flags.REVERSE_PAUSE_ID:
							## change reverse button image from Pause to Play
							## ic()
						case flags.FORWARD_STOP_ID:
							## change forward button image from Pause to Play
							## ic()
						case flags.REVERSE_STOP_ID:
							## change reverse button image from Pause to Play
							## ic()
						case flags.GOTO_END_ID:
							## no button image change
							## ic()
						case flags.GOTO_START_ID:
							## no button image change
							## ic()

if __name__ == "__main__":
	flags = APVideoFlags()
	loop_state = flags.LOOP_ON
	last_frame = 12
	button_id = flags.LOOP_ID
	mode = flags.HALT
	direction = flags.DIRECTION_FORWARD
	frame_number = 0
	
	playback_control(button_id, mode, direction, frame_number)
	playback_control(button_id, mode, direction, frame_number)
	playback_control(button_id, mode, direction, frame_number)
	playback_control(button_id, mode, direction, frame_number)
