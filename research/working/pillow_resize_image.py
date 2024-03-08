from tkinter import *
from tkinter.ttk import *
import cv2
from PIL import Image, ImageTk

## set up display
window = Tk()
canvas = Canvas(window, width = 720, height = 320)
canvas.grid()

# Load an image as OpenCV
cv_image = cv2.imread("images/one_dollar.jpg")

## convert ##

## reverse the order of the colour channels
blue, green, red = cv2.split(cv_image)
image_rgb = cv2.merge((red, green, blue))
pillow_image_data = Image.fromarray(image_rgb)

## resize image
newsize = (360, 160)
pillow_image_data = pillow_image_data.resize(newsize)

## convert to TkImage
tk_image = ImageTk.PhotoImage(pillow_image_data)

## put the image on the canvas
canvas.create_image(0, 0, anchor = "nw", image = tk_image)

## open the display
window.mainloop()
