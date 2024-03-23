'''
Observer Pattern

Implement the observer pattern. Here's how it works: 
- Define an interface (abstract class) called VideoObserver with a method
  update(video_data). This method will be called whenever there's an update
  to the video data (like a new frame).
- Make your video playback module (where the canvas resides) implement this
  interface.
- When the buttons need to perform an action on the video (play, pause, 
  etc.), they can call a method on the video playback module to register
  themselves as observers.
- The video playback module will then call the update method on all
  registered observers whenever there's a change in the video data.
- Inside the update method of the button class, you can access and potentially
  update the video canvas based on the video state.
  
Benefits

- Loose Coupling: Buttons and the video playback module are loosely coupled.
  They interact through an interface or variable, not directly referencing 
  each other's internal implementation.
- Maintainability: Easier to maintain and extend the code as you can modify
  functionalities in separate modules without affecting others.

If you need more flexibility and control over how buttons interact with the
video (e.g., sending specific commands), the Observer pattern might be a 
better fit.
'''

from abc import ABC, abstractmethod

class VideoObserver(ABC):
  @abstractmethod
  def update(self, video_data):
    pass

#----------------------------------------

from tkinter import Tk, Canvas

class VideoPlaybackModule:
  def __init__(self, root):
    self.root = root
    self.canvas = Canvas(root)
    self.canvas.pack()
    self.observers = []
    self.current_state = "stopped"  # Example video state

  def play(self):
    self.current_state = "playing"
    self.update_observers()

  def pause(self):
    self.current_state = "paused"
    self.update_observers()

  # Implement methods for other video controls

  def register_observer(self, observer):
    self.observers.append(observer)

  def update_observers(self):
    for observer in self.observers:
      observer.update(self.current_state)

# Example function to update canvas based on state (replace with your video playback logic)
  def update_canvas(self, state):
    if state == "playing":
      # Update canvas with new frame
      pass
    # Handle other states

#--------------------------------------------

class Button(VideoObserver):
  def __init__(self, root, text, video_module):
    self.button = Button(root, text=text, command=self.handle_click)
    self.button.pack()
    self.video_module = video_module
    self.video_module.register_observer(self)

  def handle_click(self):
    if self.video_module.current_state == "stopped":
      self.video_module.play()
    else:
      self.video_module.pause()  # Modify for other button actions

  def update(self, video_data):
    if video_data == "playing":
      self.button.config(text="Pause")
    elif video_data == "paused":
      self.button.config(text="Play")
    # Handle other state updates for button behavior
