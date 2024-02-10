## May be a solution to playing video from RAM.
'''
This code loads a series of video frames as PIL Images, converts them to PhotoImages
using the ImageTk.PhotoImage constructor, and displays them in a tkinter.Canvas
widget using the create_image method.

The animate function updates the canvas with a new frame every 42 milliseconds (24 fps),
using the after method to schedule the next frame.

This code has been massaged for png images whose numbers have 3 leading zeros.
'''
import tkinter as tk 
from PIL import Image, ImageTk 
import sys
import os
path = os.path.abspath(os.path.dirname(sys.argv[0]))

# Create a Tkinter window 
window = tk.Tk() 
 
# Create a Canvas widget 
canvas = tk.Canvas(window, width = 1920, height = 1080) 
canvas.pack() 

## initialize an empty array for the frames
images = []

# Load the video frames as PIL Images 
for i in range(8): 
	image = Image.open(path + f"/image_sequence/Lisa_Turnaround_1920x1080_{i:04d}.png") 
	images.append(image) 

# Convert the PIL Images to PhotoImages 
#video_frames = [ImageTk.PhotoImage(frame) for frame in images]
video_frames = []

for frame in images:
	video_frames.append(ImageTk.PhotoImage(frame))
	
# Define a function to animate the video frames 
def animate(frame_num): 
	## prepare the canvas for the next frame
	canvas.delete("all") 
	# Display the current frame 
	canvas.create_image(0, 0, anchor = "nw", image = video_frames[frame_num]) 

	# Schedule the next frame to be displayed 
	window.after(42, animate, (frame_num + 1) % len(video_frames)) 
 
# Start the animation 
animate(0) 
 
# Start the Tkinter event loop 
window.mainloop()
