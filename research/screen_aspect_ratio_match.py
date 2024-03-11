from screen_aspect_ratios import *

def check_height(height, height_set):
	match height:
		case _ if height < height_set["720p"]:
			print("Height ", height, " is less than 720p")
		case _ if height > height_set["720p"] and height < height_set["1080p"]:
			print("Height ", height, " is less than 1080p")
		case _ if height > height_set["1080p"] and height < height_set["2k"]:
			print("Height ", height, " is less than 2k")
		case _ if height > height_set["2k"] and height < height_set["3k"]:
			print("Height ", height, " is less than 3k")
		case _ if height > height_set["3k"] and height < height_set["4k"]:
			print("Height ", height, " is less than 4k")
		case _ if height > height_set["4k"] and height < height_set["5k"]:
			print("Height ", height, " is less than 5k")
		case _ if height > height_set["5k"] and height < height_set["6k"]:
			print("Height ", height, " is less than 6k")
		case _ if height > height_set["6k"] and height < height_set["8k"]:
			print("Height ", height, " is less than 8k")
		case _ if height > height_set["8k"]:
			print("Height ", height, " is more than 8k")

def check_width(width, width_set):
	match width:
		case _ if width < width_set["720p"]:
			print("width", width, " is less than 720p")
		case _ if width > width_set["720p"] and width < width_set["1080p"]:
			print("width", width, " is less than 1080p")
		case _ if width > width_set["1080p"] and width < width_set["2k"]:
			print("width", width, " is less than 2k")
		case _ if width > width_set["2k"] and width < width_set["3k"]:
			print("width", width, " is less than 3k")
		case _ if width > width_set["3k"] and width < width_set["4k"]:
			print("width", width, " is less than 4k")
		case _ if width > width_set["4k"] and width < width_set["5k"]:
			print("width", width, " is less than 5k")
		case _ if width > width_set["5k"] and width < width_set["6k"]:
			print("width", width, " is less than 6k")
		case _ if width > width_set["6k"] and width < width_set["8k"]:
			print("width", width, " is less than 8k")
		case _ if width > width_set["8k"]:
			print("width ", width, " is more than 8k")

# Example usage:
height_set = { "8k": screen_aspect_ratios["8k"]['height'],
					"6k": screen_aspect_ratios["6k"]['height'],
					"5k": screen_aspect_ratios["5k"]['height'],
					"4k": screen_aspect_ratios["4k"]['height'],
					"3k": screen_aspect_ratios["3k"]['height'],
					"2k": screen_aspect_ratios["2k"]['height'],
					"1080p": screen_aspect_ratios["1080p"]['height'],
					"720p": screen_aspect_ratios["720p"]['height']
			 }

width_set = {  "8k": screen_aspect_ratios["8k"]['width'],
					"6k": screen_aspect_ratios["6k"]['width'],
					"5k": screen_aspect_ratios["5k"]['width'],
					"4k": screen_aspect_ratios["4k"]['width'],
					"3k": screen_aspect_ratios["3k"]['width'],
					"2k": screen_aspect_ratios["2k"]['width'],
					"1080p": screen_aspect_ratios["1080p"]['width'],
					"720p": screen_aspect_ratios["720p"]['width']
			 }


check_width(1279, width_set) ## < 720p
check_width(1919, width_set) ## < 1080p
check_width(2047, width_set) ## < 2k
check_width(2879, width_set) ## < 3k
check_width(3839, width_set) ## < 4k
check_width(5119, width_set) ## < 5k
check_width(6143, width_set) ## < 6k
check_width(7679, width_set) ## < 8k
check_width(7681, width_set) ## > 8k
print()
check_height(719, height_set) ## < 720p
check_height(1079, height_set) ## < 1080p
check_height(1151, height_set) ## < 2k
check_height(1619, height_set) ## < 3k
check_height(2159, height_set) ## < 4k
check_height(2879, height_set) ## < 5k
check_height(3455, height_set) ## < 6k
check_height(4319, height_set) ## < 8k
check_height(4321, height_set) ## > 8k
