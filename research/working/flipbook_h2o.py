'''
Sure, here's an updated version of the code that loads all images in a folder named "image_sequence" instead of loading them by name:
'''
import tkinter as tk
from PIL import Image, ImageTk
import os
import time

# Set up the UI
root = tk.Tk()
root.title("Image Sequence Player")

# Create a canvas to display the images
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)

# Create a label to display the controls
control_label = tk.Label(root, text="Controls:", bg="black")
control_label.pack(fill="both", expand=True)

# Create buttons for the controls
play_button = tk.Button(root, text="Play", command=lambda: play_animation())
play_button.pack(side="left")

pause_button = tk.Button(root, text="Pause", command=lambda: pause_animation())
pause_button.pack(side="left")

stop_button = tk.Button(root, text="Stop", command=lambda: stop_animation())
stop_button.pack(side="left")

step_forward_button = tk.Button(root, text="Step Forward", command=lambda: step_forward())
step_forward_button.pack(side="left")

step_backward_button = tk.Button(root, text="Step Backward", command=lambda: step_backward())
step_backward_button.pack(side="left")

go_to_start_button = tk.Button(root, text="Go to Start", command=lambda: go_to_start())
go_to_start_button.pack(side="left")

go_to_end_button = tk.Button(root, text="Go to End", command=lambda: go_to_end())
go_to_end_button.pack(side="left")

loop_button = tk.Button(root, text="Loop On/Off", command=lambda: toggle_loop())
loop_button.pack(side="left")

# Set up the animation
image_folder = "image_sequence"
image_list = []
for filename in os.listdir(image_folder):
    image_path = os.path.join(image_folder, filename)
    image = Image.open(image_path)
    image_list.append(image)

def play_animation():
    global animation_running
    animation_running = True
    while animation_running:
        for image in image_list:
            canvas.create_image(image[0], anchor=tk.NW)
            root.update()
            time.sleep(0.04)

def pause_animation():
    global animation_running
    animation_running = False

def stop_animation():
    global animation_running
    animation_running = False
    canvas.delete(tk.ALL)

def step_forward():
    global current_image
    current_image += 1
    if current_image >= len(image_list):
        current_image = 0
    canvas.delete(tk.ALL)
    canvas.create_image(image_list[current_image], anchor=tk.NW)

def step_backward():
    global current_image
    current_image -= 1
    if current_image < 0:
        current_image = len(image_list) - 1
    canvas.delete(tk.ALL)
    canvas.create_image(image_list[current_image], anchor=tk.NW)

def go_to_start():
    canvas.delete(tk.ALL)
    canvas.create_image(image_list[0], anchor=tk.NW)

def go_to_end():
    canvas.delete(tk.ALL)
    canvas.create_image(image_list[-1], anchor=tk.NW)

def toggle_loop():
    global loop_status
    loop_status = not loop_status
    if loop_status:
        print("Loop is on")
    else:
        print("Loop is off")

# Start the animation
root.mainloop()
'''
In this version of the code, we use the `os` module to list all the files in the "image_sequence" folder, and then iterate through the list of files to create a list of images. We then use this list of images to create the animation.

I hope this helps! Let me know if you have any questions.
'''