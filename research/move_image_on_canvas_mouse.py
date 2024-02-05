'''
Move an image over a canvas background using the arrow keys. Holding
the Shift key and pressing an arrow key moves the image ten times faster.
'''
from tkinter import *
from tkinter.ttk import *
import sys
import os

## get the execution path
path = os.path.abspath(os.path.dirname(sys.argv[0]))

window = Tk()
window.title("Move image around a canvas")
window.geometry("800x600")

window_width = 600
window_height = 400
x = window_width / 2
y = window_height / 2

my_canvas = Canvas(window, width = window_width, height = window_height, bg = "white")
my_canvas.pack(pady = 20)

image = PhotoImage(file = path + "/images/head126x127.png")
## centre the image in the canvas
mid_x = (window_width - image.width()) / 2
mid_y = (window_height - image.height()) / 2
print("mid_x: ", mid_x, ", mid_y: ", mid_y)
my_image = my_canvas.create_image(mid_x, mid_y, anchor = NW, image = image)

def left(event):
	x = -1
	y = 0
	my_canvas.move(my_image, x, y)

def shift_left(event):
	x = -10
	y = 0
	my_canvas.move(my_image, x, y)

def shift_right(event):
	x = 10
	y = 0
	my_canvas.move(my_image, x, y)

def right(event):
	x = 1
	y = 0
	my_canvas.move(my_image, x, y)

def shift_up(event):
	x = 0
	y = -10
	my_canvas.move(my_image, x, y)

def up(event):
	x = 0
	y = -1
	my_canvas.move(my_image, x, y)

def shift_down(event):
	x = 0
	y = 10
	my_canvas.move(my_image, x, y)

def down(event):
	x = 0
	y = 1
	my_canvas.move(my_image, x, y)

def mouse_move(event):
	x, y = my_canvas.coords(my_image)
	
	my_canvas.move(my_image, event.x, event.y)

def on_click(event):
	my_canvas.startxy = (event.x, event.y)

def on_drag(event):
	delta_x = event.x - my_canvas.startxy[0]
	delta_y = event.y - my_canvas.startxy[1]
	# move the selected item
	my_canvas.move(my_image, delta_x, delta_y)
	# update last position
	my_canvas.startxy = (event.x, event.y)

window.bind("<Left>", left)
window.bind("<Right>", right)
window.bind("<Up>", up)
window.bind("<Down>", down)
window.bind("<Shift-Left>", shift_left)
window.bind("<Shift-Right>", shift_right)
window.bind("<Shift-Up>", shift_up)
window.bind("<Shift-Down>", shift_down)
window.bind("<Button-1>", on_click)
window.bind("<B1-Motion>", on_drag)
window.mainloop()
