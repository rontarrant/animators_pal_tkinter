## A solution to playing video from RAM.
'''
This test:
- loads a series of images using cv2,
- reverses colour channel order,
- converts them from cv2 to ImageTk.PhotoImages, and
- displays them as a flipbook.

In the show_next_frame() function, fps is set by passing the desired
frames per second to fps2milliseconds() which converts it
to milliseconds (which is what window.after() needs).

This method of doing a flipbook works reliably up to ~60 fps,
certainly fast enough for any hand-drawn animation cels.

'''
import tkinter as tk 
from PIL import Image, ImageTk 
import sys
import os
import cv2

## local
from fps2milliseconds import fps2ms

# Create a Tkinter window 
window = tk.Tk() 
 
# Create a Canvas widget 
canvas = tk.Canvas(window, width = 1920, height = 1080) 
canvas.pack() 

## initialize an empty array for the frames
images = []

## Load frames as OpenCV images and convert to pillow format
for i in range(8): 
	image_bgr = cv2.imread(f"image_sequence/Lisa_Turnaround_1920x1080_{i:04d}.png")
	## reverse order of colour channels
	blue, green, red = cv2.split(image_bgr) 
	image_rgb = cv2.merge((red, green, blue))
	photo = Image.fromarray(image_rgb)
	## add the image to the frame list
	images.append(photo)

## Convert from pillow to tkinter PhotoImages
# OLD: video_frames = [ImageTk.PhotoImage(frame) for frame in images]
video_frames = []

for frame in images:
	video_frames.append(ImageTk.PhotoImage(frame))

# Define a function to show_next_frame the video frames 
def show_next_frame(frame_num): 
	## prepare the canvas for the next frame
	canvas.delete("all") 
	# Display the current frame 
	canvas.create_image(0, 0, anchor = "nw", image = video_frames[frame_num]) 

	# fps
	fps = fps2ms(12)
	
	# Schedule the next frame to be displayed 
	print("frame: (frame_num + 1) = ", (frame_num + 1), "len(video_frames) = ", len(video_frames), "(frame_num + 1) % len(video_frames) = ", (frame_num + 1) % len(video_frames))
	'''
	The line following this comment does the same thing as:
	
	frame_num += 1
	
	if frame_num == len(video_frames):
		frame_num = 0
	window.after(fps, show_next_frame, frame_num)
	'''
	window.after(fps, show_next_frame, (frame_num + 1) % len(video_frames))
 
# Start the animation 
show_next_frame(0) 

# Start the Tkinter event loop 
window.mainloop()
