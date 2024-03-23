'''
Observer pattern. The Observer pattern is a behavioral design 
pattern that allows objects to be notified when the state of 
another object changes. In your case, the buttons can act as 
observers, and the video canvas can be the subject. Here's a 
high-level overview of how you can implement this: 

Subject (VideoCanvas)

1.	Create a VideoCanvas class that represents the canvas where 
   the video will play.
2.	Implement a method to attach observers (buttons) to the 
   VideoCanvas instance.
3.	Implement a method to detach observers from the VideoCanvas
   instance.
4.	Implement a method to notify all attached observers when 
   the state of the VideoCanvas changes (e.g., when the video 
   starts, stops, or changes position).
   
Observer (Button)

1.	Create a Button class that represents the buttons for 
   controlling the video.
2.	Implement an update method in the Button class, which will 
   be called by the VideoCanvas instance when its state changes.
3.	In the update method, you can define the behavior of the 
   button based on the state of the VideoCanvas.
   
In this example, the VideoCanvas class is the subject, and the Button 
class is the observer. The Button instances register themselves with the 
VideoCanvas instance using the attach method. When an event occurs 
(e.g., "play" or "pause"), the VideoCanvas instance notifies all attached
observers by calling their update method with the event as an argument.

By using the Observer pattern, you can decouple the buttons from the video 
canvas, making your code more modular and easier to maintain. Additionally,
you can add or remove buttons without modifying the VideoCanvas class, as 
long as they implement the update method.
'''
# subject.py
class VideoCanvas:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)

# observer.py
class Button:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.attach(self)

    def update(self, event):
        # Define the behavior of the button based on the event
        if event == "play":
            print("Play button clicked")
        elif event == "pause":
            print("Pause button clicked")
        # ... and so on

# main.py
from subject import VideoCanvas
from observer import Button

# Create the video canvas
canvas = VideoCanvas()

# Create the buttons
play_button = Button(canvas)
pause_button = Button(canvas)

# Simulate events
canvas.notify("play")
canvas.notify("pause")
