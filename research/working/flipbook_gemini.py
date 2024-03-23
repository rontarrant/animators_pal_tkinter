import tkinter as tk
from tkinter import ttk  # for buttons
from PIL import Image, ImageTk
import os


class ImageSequencePlayer:
	def __init__(self, master):
		self.master = master
		master.title("Image Sequence Player")

		# Image sequence folder path
		self.image_folder = "image_sequence"

		# Load images and create PhotoImage objects
		self.images = []
		self.load_images()

		# Animation variables
		self.current_frame = 0
		self.is_playing = False
		self.loop = True

		# Create UI elements
		self.create_widgets()

		# Start the main loop
		self.master.after(1000 // 24, self.update_animation)  # Aim for 24 fps

	def load_images(self):
		for filename in os.listdir(self.image_folder):
			if filename.endswith(".png") or filename.endswith(".jpg"):
				filepath = os.path.join(self.image_folder, filename)
				image = Image.open(filepath)
				self.images.append(ImageTk.PhotoImage(image))

	def create_widgets(self):
		# Image label
		self.image_label = tk.Label(self.master, image=self.images[0])
		self.image_label.pack()

		# Control buttons frame
		controls_frame = ttk.Frame(self.master)
		controls_frame.pack()

		# Play button
		self.play_button = ttk.Button(
			controls_frame, text="Play", command=self.play_pause
		)
		self.play_button.pack(side=tk.LEFT)

		# Pause button
		self.pause_button = ttk.Button(
			controls_frame, text="Pause", command=self.play_pause, state=tk.DISABLED
		)
		self.pause_button.pack(side=tk.LEFT)

		# Stop button
		self.stop_button = ttk.Button(controls_frame, text="Stop", command=self.stop)
		self.stop_button.pack(side=tk.LEFT)

		# Step forward button
		self.step_forward_button = ttk.Button(
			controls_frame, text="Step Forward", command=self.step_forward
		)
		self.step_forward_button.pack(side=tk.LEFT)

		# Step backward button
		self.step_backward_button = ttk.Button(
			controls_frame, text="Step Backward", command=self.step_backward
		)
		self.step_backward_button.pack(side=tk.LEFT)

		# Go to start button
		self.go_to_start_button = ttk.Button(
			controls_frame, text="Start", command=self.go_to_start
		)
		self.go_to_start_button.pack(side=tk.LEFT)

		# Go to end button
		self.go_to_end_button = ttk.Button(
			controls_frame, text="End", command=self.go_to_end
		)
		self.go_to_end_button.pack(side=tk.LEFT)

		# Loop checkbox
		self.loop_var = tk.IntVar(value=1)  # 1 for loop on, 0 for off
		self.loop_checkbox = ttk.Checkbutton(
			controls_frame, text="Loop", variable=self.loop_var
		)
		self.loop_checkbox.pack(side=tk.LEFT)

	def play_pause(self):
		if self.is_playing:
			self.is_playing = False
			self.pause_button.config(state=tk.DISABLED)
			self.play_button.config(state=tk.NORMAL)
		else:
			self.is_playing = True
			self.pause_button.config(state=tk.NORMAL)
			self.play_button.config(state=tk.DISABLED)

	def stop(self):
		self.is_playing = False
		self.current_frame = 0
		self.update_image()
		self.pause_button.config(state=tk.DISABLED)
		self.play_button.config(state=tk.NORMAL)

# Create the main window and run the application
root = tk.Tk()
player = ImageSequencePlayer(root)
root.mainloop()
