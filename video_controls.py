'''
Video Controls
The usual controls for video... play, stop, pause, etc. 
'''

from tkinter import *
#from tkinter.ttk import *

class ImageButton(Button):
	unclicked_swap_image = None
	clicked_swap_image = None
	unclicked_image = None
	clicked_image = None
	swapable = False ## does the button have swap images
	swapped = False ## track the state of swapped/unswapped
	
	def __init__(self, parent, up_image, down_image, swap_on = None, swap_off = None, *args, **kwargs):
		if swap_on != None and swap_off != None:
			self.unclicked_swap_image = PhotoImage(file = swap_off)
			self.clicked_swap_image = PhotoImage(file = swap_on)
			self.unclicked_image = PhotoImage(file = up_image)
			self.clicked_image = PhotoImage(file = down_image)
			self.unclickedImage = PhotoImage(file = up_image)
			self.clickedImage = PhotoImage(file = down_image)
			self.swapable_image()
		else:
			self.unclickedImage = PhotoImage(file = up_image)
			self.clickedImage = PhotoImage(file = down_image)
			
		super().__init__(parent, *args, image = self.unclickedImage, **kwargs)
		self.toggleState = 1
		self.bind("<Button-1>", self.clickFunction)
			
	def swapable_image(self, event = None):
		self.swapable = True
		
	def clickFunction(self, event = None):
		if self.swapable == True:
			if self.swapped == False: ## we're in an unswapped state; change to swapped state
				self.swapped = True
				self.unclickedImage = self.unclicked_swap_image
				self.clickedImage = self.clicked_swap_image
				print("looping is on")
			else:
				self.swapped = False
				self.unclickedImage = self.unclicked_image
				self.clickedImage = self.clicked_image
				print("looping is off")
				
			
		if self.cget("state") != "disabled": #Ignore click if button is disabled
			self.toggleState *= -1
			
			if self.toggleState == -1:
				self.config(image = self.clickedImage)
			else:
				self.config(image = self.unclickedImage)

class VideoControlsFrame(Frame):
	colour = "CadetBlue1"
	
	def __init__(self, parent):
		super().__init__(parent)
		## configure
		self.parent = parent
		self.configure(width = 1280, height = 72)
		## populate
		# goto start
		goto_start_button = ImageButton(self, "images/goto_start_64x64_up.png", "images/goto_start_64x64_down.png")
		# step backward
		step_backward_button = ImageButton(self, "images/step_backward_64x64_up.png", "images/step_backward_64x64_down.png")
		# play button
		play_button = ImageButton(self, "images/play_64x64_up.png", "images/play_64x64_down.png")
		# pause
		pause_button = ImageButton(self, "images/pause_64x64_up.png", "images/pause_64x64_down.png")
		# stop
		stop_button = ImageButton(self, "images/stop_64x64_up.png", "images/stop_64x64_down.png")
		# step forward
		step_forward_button = ImageButton(self, "images/step_forward_64x64_up.png", "images/step_forward_64x64_down.png")
		# goto end
		goto_end_button = ImageButton(self, "images/goto_end_64x64_up.png", "images/goto_end_64x64_down.png")
		# loop on/off
		loop_image_up = "images/loop_off_64x64_up.png"
		loop_image_down = "images/loop_off_64x64_down.png"
		loop_image_swap_up = "images/loop_on_64x64_up.png"
		loop_image_swap_down = "images/loop_on_64x64_down.png"
		loop_button = ImageButton(self, loop_image_up, loop_image_down, swap_on = loop_image_swap_up, swap_off = loop_image_swap_down)
		## layout
		goto_start_button.pack(side = LEFT)
		step_backward_button.pack(side = LEFT)
		play_button.pack(side = LEFT)
		pause_button.pack(side = LEFT)
		stop_button.pack(side = LEFT)
		step_forward_button.pack(side = LEFT)
		goto_end_button.pack(side = LEFT)
		loop_button.pack(side = LEFT)
		## button bindings
		goto_start_button.bind("<Button-1>", self.goto_start_callback)
		step_backward_button.bind("<Button-1>", self.step_backward_callback)
		play_button.bind("<Button-1>", self.play_callback)
		pause_button.bind("<Button-1>", self.pause_callback)
		stop_button.bind("<Button-1>", self.stop_callback)
		step_forward_button.bind("<Button-1>", self.step_forward_callback)
		goto_end_button.bind("<Button-1>", self.goto_end_callback)
		loop_button.bind("<Button-1>", self.loop_switch, add="+")

	def goto_start_callback(self, *args, **kwargs):
		print("Goto Start button pressed")

	def step_backward_callback(self, *args, **kwargs):
		print("Step Backward button pressed")

	def play_callback(self, *args, **kwargs):
		print("Play button pressed")

	def pause_callback(self, *args, **kwargs):
		print("Pause button pressed")

	def stop_callback(self, *args, **kwargs):
		print("Stop button pressed")

	def step_forward_callback(self, *args, **kwargs):
		print("Step Forward button pressed")

	def goto_end_callback(self, *args, **kwargs):
		print("Goto End button pressed")

	def loop_switch(self, *args, **kwargs):
		print("loop switch")

## testing
if __name__ == "__main__":
	window = Tk()
	window.configure(width = 1280, height = 840)
	vcanvas = VideoControlsFrame(window)
	vcanvas.pack()
	window.mainloop()
