import tkinter as tk
from PIL import Image, ImageTk
import os

class ImageAnimator:
    def __init__(self, master, images):
        self.master = master
        self.images = images
        self.index = 0
        self.playing = False
        self.loop = False

        self.canvas = tk.Canvas(master, width=1920, height=1080)
        self.canvas.pack()

        self.btn_stop = tk.Button(master, text="Stop", command=self.stop_animation)
        self.btn_play = tk.Button(master, text="Play", command=self.play_animation)
        self.btn_pause = tk.Button(master, text="Pause", command=self.pause_animation)
        self.btn_next = tk.Button(master, text="Next Frame", command=self.next_frame)
        self.btn_prev = tk.Button(master, text="Previous Frame", command=self.prev_frame)
        self.btn_loop = tk.Button(master, text="Loop On/Off", command=self.toggle_loop)

        self.btn_stop.pack(side=tk.LEFT)
        self.btn_play.pack(side=tk.LEFT)
        self.btn_pause.pack(side=tk.LEFT)
        self.btn_prev.pack(side=tk.LEFT)
        self.btn_next.pack(side=tk.LEFT)
        self.btn_loop.pack(side=tk.LEFT)

    def show_image(self):
        image_path = os.path.join(self.images[self.index])
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        # Display the image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)

        # Keep a reference to the photo to prevent it from being garbage collected
        self.canvas.image = photo

        if self.playing:
            if not self.loop and self.index == len(self.images) - 1:
                # Stop playing if not looping and reached the end
                self.playing = False
            else:
                # Move to the next frame after a delay corresponding to 24 frames per second (1000ms / 24fps)
                delay_time = int(1000 / 24)  # Calculate delay time for 24 frames per second
                self.index = (self.index + 1) % len(self.images)
                self.master.after(delay_time, lambda: self.show_image())

    def play_animation(self):
        if not self.playing:
            self.playing = True
            self.show_image()

    def stop_animation(self):
        if self.playing:
            self.playing = False

    def pause_animation(self):
        if self.playing:
            self.playing = False

    def next_frame(self):
        if not self.playing:
            if self.index < len(self.images) - 1:
                self.index += 1
                image_path = os.path.join(self.images[self.index])
                image = Image.open(image_path)
                photo = ImageTk.PhotoImage(image)
                # Display the next frame on the canvas
                self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                # Keep a reference to the photo to prevent it from being garbage collected
                self.canvas.image = photo

    def prev_frame(self):
        if not self.playing:
            if self.index > 0:
                self.index -= 1
                image_path = os.path.join(self.images[self.index])
                image = Image.open(image_path)
                photo = ImageTk.PhotoImage(image)
                # Display the previous frame on the canvas
                self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                # Keep a reference to the photo to prevent it from being garbage collected
                self.canvas.image = photo

    def toggle_loop(self):
        self.loop = not self.loop
        if self.loop:
            print("Looping enabled")
        else:
            print("Looping disabled")
        
# Example usage
root = tk.Tk()
folder_path = "image_sequence"  # Specify your folder path here
images_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.jpg', '.png'))]
animator = ImageAnimator(root, images_list)
root.mainloop()
