from tkinter import *
from tkinter.ttk import *
import cv2
from PIL import Image, ImageTk

## set up display
window = Tk()
canvas = Canvas(window, width = 700, height = 320)
canvas.grid()

# Load an image as OpenCV
cv_image = cv2.imread("images/one_dollar.jpg")

## convert ##

## reverse the order of the colour channels
blue, green, red = cv2.split(cv_image)
image_rgb = cv2.merge((red, green, blue))
pillow_image_data = Image.fromarray(image_rgb)

## Size of the image in pixels (size of original image) 
width, height = pillow_image_data.size 
 
## Set the points for cropped image 
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5

## crop the image
cropped_image = pillow_image_data.crop((left, top, right, bottom))

## convert to TkImage
tk_image = ImageTk.PhotoImage(cropped_image)

## put the image on the canvas
canvas.create_image(0, 0, anchor = "nw", image = tk_image)

## open the display
window.mainloop()
