from tkinter import *
from tkinter.ttk import *
import cv2
from PIL import Image, ImageTk

def set_ratio_type(width, height):
	##- subtract height from width:
	difference = width / height
	print("difference: ", difference)
	##	- result: 1.78 or less: pillarbox
	## - 1.781 or more: letterbox
	if difference < 1.78:
		ratio_flag = "pillarbox"
	else:
		ratio_flag = "letterbox"
	
	return ratio_flag

## set up display
window = Tk()
canvas = Canvas(window, width = 720, height = 320)
canvas.grid()

# Load an image as OpenCV
##cv_image = cv2.imread("images/starry_night_b&w.png")
##cv_image = cv2.imread("images/one_dollar.png")
##cv_image = cv2.imread("images/background.png")
##cv_image = cv2.imread("images/bogey.tif")
cv_image = cv2.imread("images/square.png")
## convert ##

## reverse the order of the colour channels
blue, green, red = cv2.split(cv_image)
image_rgb = cv2.merge((red, green, blue))
pillow_image_data = Image.fromarray(image_rgb)

## get width and height
width = cv_image.shape[1]
height = cv_image.shape[0]
print("original width: ", width, ", original height: ", height)

## the the ratio difference type
ratio_type = set_ratio_type(width, height)
print("ratio_type: ", ratio_type)

## set target resolution
target_width = 384
target_height = 216

## resize the image to fit within the target resolution
## and get the size divisor for calculating image resize
if ratio_type == "letterbox":
	new_width = target_width
	divisor = width / target_width ## always assume we're downsizing
	new_height = int(height / divisor)
	print("letterbox...\n divisor: ", divisor, "\n new_width: ", new_width, "\n new_height: ", new_height)
elif ratio_type == "pillarbox":
	new_height = target_height
	divisor = height / target_height
	new_width = int(width / divisor)
	print("pillarbox...\n divisor: ", divisor, "\n new_width: ", new_width, "\n new_height: ", new_height)

print("new_height: ", new_height, ", new_width: ", new_width)

## get placement
if new_height == target_height: ## pillarbox mode
	pillars = (target_width - new_width) / 2
	letters = 0
elif new_width == target_width: ## letterbox mode
	letters = (target_height - new_height) / 2
	pillars = 0

print("pillars: ", pillars, ", letters: ", letters)

## resize image
pillow_image_data = pillow_image_data.resize((new_width, new_height))

## convert to TkImage
tk_image = ImageTk.PhotoImage(pillow_image_data)

canvas.create_rectangle(0, 0, 384, 216, fill = "black")
## put the image on the canvas
canvas.create_image(pillars, letters, anchor = "nw", image = tk_image)

## open the display
window.mainloop()
