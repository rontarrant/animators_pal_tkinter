'''
Subject-Subscriber Pattern (similar to Observer Pattern)

This approach uses the built-in tkinter.Variable class to act as a 
subject for changes.

- Create a tkinter.Variable instance to hold the current video state
  (playing, paused, etc.).
- In the video playback module, whenever the state changes, update 
  the variable.
- The buttons can subscribe to changes in this variable using the 
  trace method.
- When the variable changes (indicating a video state update), the 
  button's trace callback function will be triggered.
- Inside the callback function, the button can access the current 
  state from the variable and potentially update the video canvas
  accordingly.

Benefits

- Loose Coupling: Buttons and the video playback module are loosely coupled.
  They interact through an interface or variable, not directly referencing 
  each other's internal implementation.
- Maintainability: Easier to maintain and extend the code as you can modify
  functionalities in separate modules without affecting others.
  
If a simpler solution focusing on reacting to video state changes is 
sufficient, the Subject-Subscriber pattern might be easier to implement.
'''
from tkinter import Tk, Canvas, StringVar

class VideoPlaybackModule:
  def __init__(self, root):
    self.root = root
    self.canvas = Canvas(root)
    self.canvas.pack()
    self.video_state = StringVar(value="stopped")  # Example video state

  def play(self):
    self.video_state.set("playing")

  def pause(self):
    self.video_state.set("paused")

  # Implement methods for other video controls

# Example function to update canvas based on state (replace with your video playback logic)
  def update_canvas(self, state):
    if state == "playing":
      # Update canvas with new frame
      pass
    # Handle other states

#------------------------------------------

from tkinter import Button

class Button:
  def __init__(self, root, text, video_module):
    self.button = Button(root, text=text)
    self.button.pack()
    self.video_module = video_module
    self.video_state = video_module.video_state  # Access variable directly
    self.update_button_text()
    self.video_state.trace_add("write", self.update_button_text)

  def handle_click(self):
    if self.video_state.get() == "stopped":
      self.video_module.play()
    else:
      self.video_module.pause()  # Modify for other button actions

  def update_button_text(self, *args):
    if self.video_state.get() == "playing":
      self.button.config(text="Pause")
    elif self.video_state.get() == "paused":
      self.button.config(text="Play")
    # Handle other state updates for button behavior
