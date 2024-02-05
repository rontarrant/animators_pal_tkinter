from tkinter import *
from PIL import Image
import sys
import os
## get the execution path
path  =  os.path.abspath(os.path.dirname(sys.argv[0]))
print("path: ", path)
root  =  Tk()
root.title("Game")

frame  =  Frame(root)
frame.pack()

width = 700
height = 400
centre_x = width / 2
centre_y = height / 2


canvas  =  Canvas(frame, bg = "black", width = width, height = height)
canvas.pack()


#background  =  PhotoImage(file = path + "/images/for_loop_breakdown.png")
background  =  PhotoImage(file = "images/for_loop_breakdown.png")
canvas.create_image(centre_x, centre_y, image = background)

#character  =  PhotoImage(file = path + "/images/rectangle.png")
character  =  PhotoImage(file = "images/rectangle.png")
canvas.create_image(centre_x, centre_y, image = character)

root.mainloop()
