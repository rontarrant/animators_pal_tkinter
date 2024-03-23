'''
One way to achieve this in an object-oriented style is to create a
parent class for your video control module, which will have a 
reference to the video canvas as an instance variable. The child
classes for your buttons can then inherit from this parent class
and access the canvas through the parent class's instance variable.

In this example, the VideoPlayer class is the parent class that 
contains the video canvas and the play_video method. The 
PlayButton and PauseButton classes inherit from VideoPlayer 
and have access to the video canvas through the self.video_canvas 
instance variable. The pause_video method in the PauseButton class
checks if the video thread is running and joins it if it is.

This implementation allows you to easily add more buttons with 
different functionalities while keeping the video canvas and its
functionality in a centralized location.

Here's an example implementation:
'''


import tkinter as tk
import cv2

class VideoPlayer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.video_canvas = tk.Canvas(self, width=640, height=480)
        self.video_canvas.pack()
        self.video_thread = None

    def play_video(self, filename):
        cap = cv2.VideoCapture(filename)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            self.video_canvas.create_image(0, 0, image=tk.PhotoImage(data=cv2.imencode('.jpg', frame)[1].tostring()), anchor=tk.NW)
            self.video_canvas.update()
            self.after(10)
        cap.release()
        cv2.destroyAllWindows()

class PlayButton(VideoPlayer):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_ui()
        self.create_widgets()

    def create_widgets(self):
        self.play_button = tk.Button(self, text="Play", command=self.play_video)
        self.play_button.pack()

class PauseButton(VideoPlayer):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_ui()
        self.create_widgets()

    def create_widgets(self):
        self.pause_button = tk.Button(self, text="Pause", command=self.pause_video)
        self.pause_button.pack()

    def pause_video(self):
        if self.video_thread is not None:
            self.video_thread.join()
            self.video_thread = None

# Create the main window and add the video player and buttons
root = tk.Tk()
root.geometry("800x600")

video_player = VideoPlayer(root)
play_button = PlayButton(video_player)
pause_button = PauseButton(video_player)

root.mainloop()
