'''
Based on chatgpt_checkerboard_copies.py
'''

import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import time  # Import time module for the delay
# for debugging
from icecream import install
install()
ic.configureOutput(includeContext=True)

class Checkerboard(Image.Image):
	def __init__(self, width, height, colours, square_size = 20):
		# Create a new image
		image = Image.new('RGB', (width, height), 'white')
		self.__dict__ = image.__dict__.copy()
		
		# square properties
		draw_colour = colours[0]  # colour of first square
		columns = int(width / square_size)  # width in squares
		rows = int(height / square_size)  # height in squares
		draw = ImageDraw.Draw(self)
		
		for row in range(rows):  # rows
			for column in range(columns):  # columns
				x_origin = column * square_size
				y_origin = row * square_size
				width = x_origin + square_size
				height = y_origin + square_size
				draw.rectangle((x_origin, y_origin, width, height), fill = draw_colour, width = 0)
				
				if draw_colour == colours[0]:
					draw_colour = colours[1]
				else:
					draw_colour = colours[0]
					
			if draw_colour == colours[0]:
				draw_colour = colours[1]
			else:
				draw_colour = colours[0]

	def get_tk_image(self):
		return ImageTk.PhotoImage(self)

# testing
if __name__ == "__main__":
	window = tk.Tk()  # this has to be here or PIL's TkImage won't work
	width = 1280
	height = 720
	
	# build a Canvas
	canvas = tk.Canvas(window, width = width, height = height)
	canvas.pack()
	
	# List of color pairs for different checkerboards
	color_pairs = [
		("#AA8888", "#7777AA"),  # light gray and dark blue
		("#88AA88", "#AA7777"),  # light green and light red
		("#8888AA", "#AAAA77"),  # light blue and light yellow
		("#8ea7dd", "#7d95c7")  # light blue and dark blue
	]
	
	# Number of checkerboards to create
	num_checkerboards = 3
	
	# Store references to prevent garbage collection
	checkerboards = [None for _ in range(3)]
	
	# Create one checkerboard
	base_checkerboard = Checkerboard(width, height, color_pairs[3])
	
	for i in range(num_checkerboards):
		# Create a copy of the base checkerboard
		checkerboard_copy = base_checkerboard.copy()
		
		# Create a new ImageTk.PhotoImage from the copy
		tk_image = ImageTk.PhotoImage(checkerboard_copy)
		
		# Add the checkerboard to the Canvas
		canvas.create_image(0, 0, anchor = tk.NW, image = tk_image)
		
		# Keep a reference to the image to prevent garbage collection
		checkerboards.append(tk_image)
		
		# Print number to the console
		print(f"Checkerboard {i+1}")
		
		# Update the window to show the new checkerboard
		window.update()
		
		# Delay for 1 second (adjust as needed)
		time.sleep(1)
	
	window.mainloop()
