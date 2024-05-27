def playback_control():
	match button_id:
		case LOOP_ID: ## Loop On/Off
			match LOOPING:
				case LOOPING_ON:
					LOOPING = LOOPING_OFF
				case LOOPING_OFF:
					LOOPING = LOOPING_ON
		case FORWARD_PLAY_ID: ## Play (Forward)
			match LOOPING:
				case LOOPING_ON:
					match frame_number:
						case last_frame:
							frame_number = 0
						case _:
							frame_number += 1
							## recurse?
				case LOOPING_OFF:
					match frame_number:
						case last_frame:
							mode = HALT
						case _:
							frame_number += 1
							## recurse?
		case 