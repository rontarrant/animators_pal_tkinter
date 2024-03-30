'''
Play a series of images as a video using the Model/View/Presenter pattern
'''
import tkinter as tk

'''
Model
Includes everything we need to show the images:
- actual images (in an APImageCollection),
- preferences object with:
	- playback speed,
	- playback direction,
	- first frame hold,
	- last frame hold,
	- all frames hold (2's, 3's, etc.)
'''
class Model:
    def __init__(self, presenter, image_collection):
        self.presenter = presenter
        self.image_collection = image_collection
        self.playback_speed = 1.0
        self.playback_direction = "forward"
        self.first_frame_duration = 0
        self.last_frame_duration = 0

'''
View
Consists of three areas:
- Preferences bar, 
- video canvas,
- video control buttons

Preferences
- gathers preferences from the user,
- notifies presenter so it can store preferences in model,

VideoCanvas
- displays image,
- deletes current image so new image can be displayed,

Video Control Buttons
- gathers user input to control video,
- passes user input to presenter
- accepts input from presenter to change button face(s)
'''
class View(tk.Tk):
    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter

        # Create UI elements
        self.speed_entry = tk.Entry(self)
        self.direction_var = tk.StringVar(value="forward")
        self.direction_radio_forward = tk.Radiobutton(self, text="Forward", variable=self.direction_var, value="forward")
        self.direction_radio_reverse = tk.Radiobutton(self, text="Reverse", variable=self.direction_var, value="reverse")
        self.canvas = tk.Canvas(self)
        self.play_button = tk.Button(self, text="Play", command=self.on_play)
        # Add more UI elements as needed
        
        # Place UI elements
        self.speed_entry.pack()
        self.direction_radio_forward.pack()
        self.direction_radio_reverse.pack()
        self.canvas.pack()
        self.play_button.pack()
        # Place additional UI elements

    def on_play(self):
        if self.presenter:
            self.presenter.handle_playback()

'''
Presenter (Monkey)
Instantiates the other two pattern classes:
- model, and
- view.
Responsible for:
- playback based on preferences in model,
- setting, clearing, and tracking button states,
- knowing which image is displayed next,
- tracking whether looping is on or off,
- implementing looping,
- notifying window of delay time ( after() method)
'''
class Presenter:
    def __init__(self):
        self.model = Model(self)
        self.view = View(self)
        self.model.presenter = self
        self.view.presenter = self

    def handle_playback(self):
        # Get user inputs from the view and update the model
        self.model.playback_speed = float(self.view.speed_entry.get())
        self.model.playback_direction = self.view.direction_var.get()
        # Update playback based on model data
        # Implement playback functionality

if __name__ == "__main__":
    presenter = Presenter()
    presenter.view.mainloop()
