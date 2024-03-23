## convert between milliseconds and fps
def fps2ms(fps):
	value = int(round(1000 / fps))
	
	return value

## testing
if __name__ == "__main__":
	print("24 fps: ", fps_to_milliseconds(24))
	print("15 fps: ", fps_to_milliseconds(15))
	print("30 fps: ", fps_to_milliseconds(30))
	print("25 fps: ", fps_to_milliseconds(25))
	print("60 fps: ", fps_to_milliseconds(60))
	print("48 fps: ", fps_to_milliseconds(48))
	print("23.976 fps: ", fps_to_milliseconds(23.976))
	print("29.940 fps: ", fps_to_milliseconds(29.940))
