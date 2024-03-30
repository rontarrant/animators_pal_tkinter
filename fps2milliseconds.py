## convert between milliseconds and fps
def fps2ms(fps):
	value = int(round(1000 / fps))
	
	return value

## testing
if __name__ == "__main__":
	# ic("24 fps: ", fps_to_milliseconds(24))
	# ic("15 fps: ", fps_to_milliseconds(15))
	# ic("30 fps: ", fps_to_milliseconds(30))
	# ic("25 fps: ", fps_to_milliseconds(25))
	# ic("60 fps: ", fps_to_milliseconds(60))
	# ic("48 fps: ", fps_to_milliseconds(48))
	# ic("23.976 fps: ", fps_to_milliseconds(23.976))
	# ic("29.940 fps: ", fps_to_milliseconds(29.940))
