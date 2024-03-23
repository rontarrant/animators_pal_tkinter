import tkinter as tk
from PIL import Image, ImageTk
import os

class ImagePlayer(tk.Tk):
	def __init__(self, parent, images):
		super().__init__()
		self.images = images
		self.index = 0
		self.playing = False
		self.reverse_playing = False

		self.canvas = tk.Canvas(self, width=500, height=500)
		self.canvas.pack()

		self.play_button = tk.Button(self, text="Play", command=self.play)
		self.play_button.pack(side=tk.LEFT)

		self.play_reverse_button = tk.Button(self, text="Play Reverse", command=self.play_reverse)
		self.play_reverse_button.pack(side=tk.LEFT)

		self.stop_button = tk.Button(self, text="Stop", command=self.stop)
		self.stop_button.pack(side=tk.LEFT)

		self.prev_button = tk.Button(self, text="Previous", command=self.prev_frame_reverse)
		self.prev_button.pack(side=tk.LEFT)

		self.next_button = tk.Button(self, text="Next", command=self.next_frame)
		self.next_button.pack(side=tk.LEFT)

	def play(self):
		if not self.playing and not self.reverse_playing:
			self.playing = True
			self.play_next_frame()

	def play_reverse(self):
		if not self.playing and not self.reverse_playing:
			self.reverse_playing = True
			self.play_next_frame_reverse()

	def stop(self):
		self.playing = False
		self.reverse_playing = False

	def play_next_frame(self):
		if self.playing:
			self.next_frame()
			self.after(100, self.play_next_frame)

	def play_next_frame_reverse(self):
		if self.reverse_playing:
			self.prev_frame_reverse()
			self.after(100, self.play_next_frame_reverse)

	def next_frame(self):
		if not self.playing:
			return
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.display_frame()

	def prev_frame_reverse(self):
		if not self.reverse_playing:
			return
		if self.index > 0:
			self.index -= 1
		else:
			self.index = len(self.images) - 1
		self.display_frame()

	def display_frame(self):
		image_path = os.path.join(self.images[self.index])
		image = Image.open(image_path)
		photo = ImageTk.PhotoImage(image)
		# Display the current frame on the canvas
		self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
		# Keep a reference to the photo to prevent it from being garbage collected
		self.canvas.image = photo

if __name__ == "__main__":
	# Example usage:
	root = tk.Tk()
	folder_path = "image_sequence"  # Specify your folder path here
	images_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.jpg', '.png'))]
	animator = ImagePlayer(root, images_list)
	root.mainloop()
