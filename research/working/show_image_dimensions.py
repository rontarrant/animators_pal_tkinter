from tkinter import *
from tkinter.ttk import *
import cv2
from PIL import Image, ImageTk

## set up display
window = Tk()
canvas = Canvas(window, width = 700, height = 320)
canvas.grid()

## Load an image as OpenCV
cv_image = cv2.imread("images/one_dollar.jpg")

## show size of OpenCV image
open_cv_height, open_cv_width = cv_image.shape[:2]
print("OpenCV image dimensions: ", open_cv_width, open_cv_height)

## convert ##

## reverse the order of the colour channels
blue, green, red = cv2.split(cv_image)
image_rgb = cv2.merge((red, green, blue))
pillow_image_data = Image.fromarray(image_rgb)

## show size of PIL image
pillow_width, pillow_height = pillow_image_data.size
print("Pillow image dimensions: ", pillow_width, pillow_height)

## convert to TkImage
tk_image = ImageTk.PhotoImage(pillow_image_data)

## show size of tkinter image
tkinter_width = tk_image.width()
tkinter_height = tk_image.height()
print("tkinter image dimensions: ", tkinter_width, tkinter_height)

## put the image on the canvas
canvas.create_image(0, 0, anchor = "nw", image = tk_image)

## open the display
window.mainloop()
