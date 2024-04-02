'''
Play a series of images as a video using the MiM (Monkey in the Middle) pattern
a.k.a. View/Monkey/DataSet/Monkey/View (VMDMV)
'''
from tkinter import *
from tkinter.ttk import *
from image_collection import APImageCollection

'''
DataSet
Includes everything we need to show the images:
- actual images (in an APImageCollection),
- preferences object with:
	- playback speed,
	- playback direction,
	- first frame hold,
	- last frame hold,
	- all frames hold (2's, 3's, etc.)
'''
class DataSet:
	def __init__(self, monkey, image_collection):
		self.monkey = monkey
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
- notifies monkey so it can store preferences in dataset,

VideoCanvas
- displays image,
- deletes current image so new image can be displayed,

Video Control Buttons
- gathers user input to control video,
- passes user input to monkey
- accepts input from monkey to change button face(s)
'''
class View():
	def __init__(self, window, monkey):
		super().__init__()
		self.monkey = monkey

		# Create UI elements
		self.speed_entry = Entry(self)
		self.direction_var = StringVar(value="forward")
		self.direction_radio_forward = Radiobutton(self, text="Forward", variable=self.direction_var, value="forward")
		self.direction_radio_reverse = Radiobutton(self, text="Reverse", variable=self.direction_var, value="reverse")
		self.canvas = Canvas(self)
		self.play_button = Button(self, text="Play", command=self.on_play)
		# Add more UI elements as needed
		
		# Place UI elements
		self.speed_entry.pack()
		self.direction_radio_forward.pack()
		self.direction_radio_reverse.pack()
		self.canvas.pack()
		self.play_button.pack()
		# Place additional UI elements

	def on_play(self):
		if self.monkey:
			self.monkey.handle_playback()

'''
Monkey
Instantiates the other two pattern classes:
- dataset, and
- view.
Responsible for:
- playback images on the VideoCanvas based on preferences in dataset,
- setting, clearing, and tracking button states,
- knowing which image is displayed next,
- tracking whether looping is on or off,
- looping video playback when needed,
- notifying window of delay time ( after() method) for each frame
'''
class MonkeyFrame(Frame):
	def __init__(self, window, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.image_collection = APImageCollection
		self.dataset = DataSet(self, self.image_collection)
		self.view = View(self)
		self.dataset.monkey = self
		self.view.monkey = self

	def handle_playback(self):
		# Get user inputs from the view and update the dataset
		self.dataset.playback_speed = float(self.view.speed_entry.get())
		self.dataset.playback_direction = self.view.direction_var.get()
		# Update playback based on dataset data
		# Implement playback functionality

if __name__ == "__main__":
	window = Tk()
	monkey = MonkeyFrame(window)
	monkey.grid()
	window.mainloop()
