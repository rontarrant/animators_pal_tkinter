'''
When a button is clicked, the status of the video player (self.status) changes
to one of the constants defined in __init__.

The match/case construct in show_next_frame() checks the status and does
the absolute minimum to move things along. There are no if/elif/else statements
because that slows things down. Playing forward without looping and playing forward
with looping are two different statuses, so we won't have to check for looping
while we're trying to keep up the fps on playback. We should have speedy playback if
we need it (up to 60 fps) because:
- the images are pre-loaded into RAM rather than being loaded from disk for each frame,
- the first four case statements take care of playback in both directions, looping
  or non-looping, meaning that there is a minimal number of checks before showing
  the next (or previous) frame, and
- the status doesn't change unless another button is pressed which means playback
  speed shouldn't matter at that point.

TODO:
- load images into an ImageCollection instance (use image_collection.py as a guide
  starting on line 53),
- add drop-down for testing fps (use set_fps_radio.py as a guide),
- rewrite testing framework
- move all code from button callbacks to show_next_frame() (or just the 
  stuff for playing in both directions)
- use buttons ONLY to set status and loop_status,
- frame to display: image_collection.images[current_frame].tk_image
'''
from tkinter import *
from PIL import Image, ImageTk
import os

from image_ap import APImage
from image_collection import APImageCollection

class ImagePlayer:
	def __init__(self, window, images_folder, fps = 24):
		self.window = window
		self.images_folder = images_folder
		self.image_files = sorted([file for file in os.listdir(images_folder) if file.endswith(('.jpg', '.png', '.gif'))])
		self.current_frame = 0
		self.isPlaying = False
		self.isLooping = False
		
		self.FIRST_FRAME = -3 ## goto start frame
		self.PREV_FRAME = -2 ## goto previous frame
		self.REVERSE = -1 ## play backwards
		self.STOP = 0 ## halt playback and goto start frame
		self.PLAY = 1 ## play forward
		self.NEXT_FRAME = 2 ## goto next frame
		self.LAST_FRAME = 3 ## goto last frame
		self.PAUSE = 4 ## stop playback and stay on current frame
		LOOP_ON = True
		LOOP_OFF = False
		loop_status = False ## default to off
		status = self.STOP
		
		self.fps = fps
		self.delay = self.fps2ms(self.fps)  # Calculate delay dynamically based on desired FPS

		# Add buttons
		self.add_control_buttons()
		## add canvas
		self.canvas = Canvas(window, width = 1920, height = 1080)  # Set canvas size according to your needs
		self.canvas.pack()

		self.update_image()

	## convert between milliseconds and fps
	def fps2ms(self, fps):
		value = int(round(1000 / fps))
		
		return value
	
	def show_next_frame(self, current_frame):
		match status:
			case (self.PLAY, self.LOOP_OFF):
				canvas.delete("all") 
				canvas.create_image(0, 0, anchor = "nw", image = video_frames[current_frame]) 
				window.after(self.fps, show_next_frame, (current_frame + 1) % len(video_frames))
				print("playing")
			case (self.REVERSE, self.LOOP_OFF):
				canvas.delete("all") 
				canvas.create_image(0, 0, anchor = "nw", image = video_frames[current_frame]) 
				window.after(self.fps, show_next_frame, (current_frame - 1) % len(video_frames))
				print("reversing")
			case (self.PLAY, self.LOOP_ON):
				canvas.delete("all") 
				canvas.create_image(0, 0, anchor = "nw", image = video_frames[current_frame]) 
				window.after(self.fps, show_next_frame, (current_frame + 1) % len(video_frames))
				print("playing & looping")
			case (self.REVERSE, self.LOOP_ON):
				canvas.delete("all") 
				canvas.create_image(0, 0, anchor = "nw", image = video_frames[current_frame]) 
				window.after(self.fps, show_next_frame, (current_frame - 1) % len(video_frames))
				print("reversing and looping")
		'''
			case (self.FIRST_FRAME, self.LOOP_ON | self.LOOP_OFF):
				current_frame = 0
				canvas.delete("all") 
				canvas.create_image(0, 0, anchor = "nw", image = video_frames[current_frame]) 
				print("going to first frame")
			case (self.LAST_FRAME, self.LOOP_ON | self.LOOP_OFF):
				current_frame = len(video_frames)
				canvas.delete("all") 
				canvas.create_image(0, 0, anchor = "nw", image = video_frames[current_frame]) 
				print("going to last frame")
			case (self.NEXT_FRAME, self.LOOP_ON | self.LOOP_OFF):
				current_frame += 1
				canvas.delete("all") 
				canvas.create_image(0, 0, anchor = "nw", image = video_frames[current_frame]) 
				print("going to next frame")
			case (self.PREV_FRAME, self.LOOP_ON | self.LOOP_OFF):
				current_frame -+ 1
				canvas.delete("all") 
				canvas.create_image(0, 0, anchor = "nw", image = video_frames[current_frame]) 
				print("going to previous frame")
			case (self.PAUSE, self.LOOP_ON | self.LOOP_OFF):
				print("paused")
				pass
			case (self.STOP, self.LOOP_ON | self.LOOP_OFF):
				print("stopped")
				self.rewind()
				pass
		'''
	
	def update_image(self):
		self.canvas.delete("all")
		image_path = os.path.join(self.images_folder, self.image_files[self.current_frame])
		image = Image.open(image_path)
		photo = ImageTk.PhotoImage(image)
		self.canvas.create_image(0, 0, anchor = NW, image = photo)
		self.canvas.image = photo

	def play_forward(self):
		if self.isPlaying and self.current_frame < len(self.image_files) - 1:
			self.current_frame += 1
			self.update_image()
			self.window.after(self.delay, self.play_forward)
		elif self.isPlaying and self.isLooping:
			self.rewind()
			self.window.after(self.delay, self.play_forward)

	def play_reverse(self):
		if self.isPlaying and self.current_frame > 0:
			self.current_frame -= 1
			self.update_image()
			self.window.after(self.delay, self.play_reverse)
		elif self.isPlaying and self.isLooping:
			self.current_frame = len(self.image_files) - 1
			self.update_image()
			self.window.after(self.delay, self.play_reverse)

	def step_forward(self):
		if self.current_frame < len(self.image_files) - 1:
			self.current_frame += 1
			self.update_image()

	def step_backward(self):
		if self.current_frame > 0:
			self.current_frame -= 1
			self.update_image()

	def rewind(self):
		self.current_frame = 0
		self.update_image()

	def stop(self):
		self.isPlaying = False
		self.rewind()

	## not needed
	def toggle_play(self):
		self.isPlaying = not self.isPlaying
		if self.isPlaying:
			self.play_forward()

	## not needed
	def toggle_play_reverse(self):
		self.isPlaying = not self.isPlaying
		if self.isPlaying:
			self.play_reverse()

	def toggle_loop(self):
		self.loop_status = not self.loop_status

	def go_to_next_frame(self):
		self.step_forward()

	def go_to_previous_frame(self):
		self.step_backward()

	def go_to_start_frame(self):
		self.rewind()

	def go_to_end_frame(self):
		self.current_frame = len(video_frames) - 1
		self.update_image()

	def add_control_buttons(self):
		button_frame = Frame(self.window)
		button_frame.pack(side = TOP, pady = 10)  # Adjust the padding as needed

		play_button = Button(button_frame, text = "Play", command = self.toggle_play)
		play_button.pack(side = LEFT)

		reverse_button = Button(button_frame, text = "Reverse", command = self.toggle_play_reverse)
		reverse_button.pack(side = LEFT)

		loop_button = Button(button_frame, text = "Loop", command = self.toggle_loop)
		loop_button.pack(side=LEFT)

		stop_button = Button(button_frame, text = "Stop", command = self.stop)
		stop_button.pack(side=LEFT)

		next_frame_button = Button(button_frame, text = "Next Frame", command = self.go_to_next_frame)
		next_frame_button.pack(side = LEFT)

		previous_frame_button = Button(button_frame, text = "Previous Frame", command = self.go_to_previous_frame)
		previous_frame_button.pack(side = LEFT)

		start_frame_button = Button(button_frame, text = "Start Frame", command = self.go_to_start_frame)
		start_frame_button.pack(side = LEFT)

		end_frame_button = Button(button_frame, text = "End Frame", command = self.go_to_end_frame)
		end_frame_button.pack(side = LEFT)

if __name__ == "__main__":
	window = Tk()
	player = ImagePlayer(window, "image_sequence", fps = 48)  # Set desired FPS here
	window.mainloop()
