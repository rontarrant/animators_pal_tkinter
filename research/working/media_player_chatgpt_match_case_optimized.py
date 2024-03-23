from PIL import Image, ImageTk
import tkinter as tk
import os

class ImagePlayer:
    def __init__(self, root, images_folder, fps = 24):
        self.root = root
        self.images_folder = images_folder
        self.image_files = sorted([f for f in os.listdir(images_folder) if f.endswith(('.jpg', '.png', '.gif'))])
        self.current_index = 0
        self.isPlaying = False
        self.isLooping = False
        self.fps = fps
        self.delay = int(1000 / self.fps)  # Calculate delay dynamically based on desired FPS
        self.image_label = tk.Label(root)
        self.image_label.pack()
        self.update_image()
        self.root.bind("<space>", lambda event: self.toggle_play())
        self.root.bind("<Right>", lambda event: self.step_forward())
        self.root.bind("<Left>", lambda event: self.step_backward())
        self.root.bind("<Return>", lambda event: self.rewind())
        self.root.bind("<BackSpace>", lambda event: self.stop())
        self.root.bind("r", lambda event: self.toggle_play_reverse())
        self.root.bind("c", lambda event: self.toggle_loop())

    def update_image(self):
        image_path = os.path.join(self.images_folder, self.image_files[self.current_index])
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

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

    def pause(self):
        self.isPlaying = False

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

if __name__ == "__main__":
    root = tk.Tk()
    player = ImagePlayer(root, "image_sequence", fps = 48)  # Set desired FPS here
    root.mainloop()
