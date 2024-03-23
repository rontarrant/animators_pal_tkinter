'''
This code is the jumping-off point for testing a fast media player
using match/case to switch the status of the player.
'''
from PIL import Image, ImageTk
import tkinter as tk
import os

class ImagePlayer:
	def __init__(self, root, images_folder, fps = 24):
		self.root = root
		self.images_folder = images_folder
		self.image_files = sorted([file for file in os.listdir(images_folder) if file.endswith(('.jpg', '.png', '.gif'))])
		self.current_index = 0
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
		status = STOP
		
		self.fps = fps
		self.delay = self.fps2ms(self.fps)  # Calculate delay dynamically based on desired FPS

		# Add buttons
		self.add_control_buttons()
		## add canvas
		self.canvas = tk.Canvas(root, width = 1920, height = 1080)  # Set canvas size according to your needs
		self.canvas.pack()

		self.update_image()

	## convert between milliseconds and fps
	def fps2ms(self, fps):
		value = int(round(1000 / fps))
		
		return value
	
	def update_image(self):
		self.canvas.delete("all")
		image_path = os.path.join(self.images_folder, self.image_files[self.current_index])
		image = Image.open(image_path)
		photo = ImageTk.PhotoImage(image)
		self.canvas.create_image(0, 0, anchor = tk.NW, image = photo)
		self.canvas.image = photo

	def play_forward(self):
		if self.isPlaying and self.current_index < len(self.image_files) - 1:
			self.current_index += 1
			self.update_image()
			self.root.after(self.delay, self.play_forward)
		elif self.isPlaying and self.isLooping:
			self.rewind()
			self.root.after(self.delay, self.play_forward)

	def play_reverse(self):
		if self.isPlaying and self.current_index > 0:
			self.current_index -= 1
			self.update_image()
			self.root.after(self.delay, self.play_reverse)
		elif self.isPlaying and self.isLooping:
			self.current_index = len(self.image_files) - 1
			self.update_image()
			self.root.after(self.delay, self.play_reverse)

	def step_forward(self):
		if self.current_index < len(self.image_files) - 1:
			self.current_index += 1
			self.update_image()

	def step_backward(self):
		if self.current_index > 0:
			self.current_index -= 1
			self.update_image()

	def rewind(self):
		self.current_index = 0
		self.update_image()

	def stop(self):
		self.isPlaying = False
		self.rewind()

	def toggle_play(self):
		self.isPlaying = not self.isPlaying
		if self.isPlaying:
			self.play_forward()

	def toggle_play_reverse(self):
		self.isPlaying = not self.isPlaying
		if self.isPlaying:
			self.play_reverse()

	def toggle_loop(self):
		self.isLooping = not self.isLooping

	def go_to_next_frame(self):
		self.step_forward()

	def go_to_previous_frame(self):
		self.step_backward()

	def go_to_start_frame(self):
		self.rewind()

	def go_to_end_frame(self):
		self.current_index = len(self.image_files) - 1
		self.update_image()

	def add_control_buttons(self):
		button_frame = tk.Frame(self.root)
		button_frame.pack(side = tk.TOP, pady = 10)  # Adjust the padding as needed

		play_button = tk.Button(button_frame, text = "Play", command = self.toggle_play)
		play_button.pack(side = tk.LEFT)

		reverse_button = tk.Button(button_frame, text = "Reverse", command = self.toggle_play_reverse)
		reverse_button.pack(side = tk.LEFT)

		loop_button = tk.Button(button_frame, text = "Loop", command = self.toggle_loop)
		loop_button.pack(side=tk.LEFT)

		stop_button = tk.Button(button_frame, text = "Stop", command = self.stop)
		stop_button.pack(side=tk.LEFT)

		next_frame_button = tk.Button(button_frame, text = "Next Frame", command = self.go_to_next_frame)
		next_frame_button.pack(side = tk.LEFT)

		previous_frame_button = tk.Button(button_frame, text = "Previous Frame", command = self.go_to_previous_frame)
		previous_frame_button.pack(side = tk.LEFT)

		start_frame_button = tk.Button(button_frame, text = "Start Frame", command = self.go_to_start_frame)
		start_frame_button.pack(side = tk.LEFT)

		end_frame_button = tk.Button(button_frame, text = "End Frame", command = self.go_to_end_frame)
		end_frame_button.pack(side = tk.LEFT)

if __name__ == "__main__":
	root = tk.Tk()
	player = ImagePlayer(root, "image_sequence", fps = 48)  # Set desired FPS here
	root.mainloop()
