from tkinter import *

class ImageButton(Button):
	## These can be class variables because only one
	## button image is changed at a given instant in time
	## and button image refresh takes care of itself.
	image_alt_image_up = None
	image_alt_image_down = None
	image_up = None
	image_down = None
	changeable = False ## does the button have alt images
	image_state = False ## track the state of the button image (normal/changed)
	
	def __init__(self, parent, image_up, image_down,
					 alt_image_down = None, alt_image_up = None,
					 *args, **kwargs):
		## ic(image_up, image_down)
		if alt_image_down != None and alt_image_up != None:
			self.image_up = PhotoImage(file = image_up)
			self.image_down = PhotoImage(file = image_down)
			self.image_alt_image_up = PhotoImage(file = alt_image_up)
			self.image_alt_image_down = PhotoImage(file = alt_image_down)
			self.live_image_up = PhotoImage(file = image_up)
			self.live_image_down = PhotoImage(file = image_down)
			self.changeable = True
		else:
			self.live_image_up = PhotoImage(file = image_up)
			self.live_image_down = PhotoImage(file = image_down)
			self.changeable = False
			
		super().__init__(parent, *args, image = self.live_image_up, **kwargs)
		self.toggleState = 1
		self.bind("<ButtonRelease-1>", self.change_button_image)

	def changeable_image(self, event = None):
		self.changeable = True
		
	def change_button_image(self, event = None):
		## ic(event)
		if self.changeable == True:
			if self.image_state == False: ## we're in an unchanged state; switch to changed state
				## ic("image_state = True... switching images")
				self.image_state = True
				self.live_image_up = self.image_alt_image_up
				self.live_image_down = self.image_alt_image_down
			else:
				## ic("image_state = False")
				self.image_state = False
				self.live_image_up = self.image_up
				self.live_image_down = self.image_down
			
		if self.cget("state") != "disabled": #Ignore click if button is disabled
			self.toggleState *= -1
			
			if self.toggleState == -1:
				self.configure(image = self.live_image_down)
			else:
				self.configure(image = self.live_image_up)

## testing
if __name__ == "__main__":
	window = Tk()
	loop_image_up = "images/loop_off_up.png"
	loop_image_down = "images/loop_off_down.png"
	loop_image_alt_image_up = "images/loop_on_up.png"
	loop_image_alt_image_down = "images/loop_on_down.png"

	window.configure(width = 1280, height = 806)
	button = ImageButton(window, loop_image_up, loop_image_down, alt_image_down = loop_image_alt_image_up, alt_image_up = loop_image_alt_image_down)
	button.grid()
	window.mainloop()

