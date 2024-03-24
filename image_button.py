from tkinter import *

class ImageButton(Button):
	## These can be class variables because only one
	## button image is swapped at a given instant in time
	## and button image refresh takes care of itself.
	unclicked_swap_image = None
	clicked_swap_image = None
	unclicked_image = None
	clicked_image = None
	swapable = False ## does the button have swap images
	swapped = False ## track the state of swapped/unswapped
	
	def __init__(self, parent, up_image, down_image, swap_on = None, swap_off = None, *args, **kwargs):
		### ic(up_image, down_image)
		if swap_on != None and swap_off != None:
			### ic(swap_on, swap_off)
			self.unclicked_swap_image = PhotoImage(file = swap_off)
			self.clicked_swap_image = PhotoImage(file = swap_on)
			self.unclicked_image = PhotoImage(file = up_image)
			self.clicked_image = PhotoImage(file = down_image)
			self.unclickedImage = PhotoImage(file = up_image)
			self.clickedImage = PhotoImage(file = down_image)
			self.swapable = True
		else:
			self.unclickedImage = PhotoImage(file = up_image)
			self.clickedImage = PhotoImage(file = down_image)
			self.swapable = False
			
		super().__init__(parent, *args, image = self.unclickedImage, **kwargs)
		self.toggleState = 1
		self.bind("<Button-1>", self.clickFunction)
			
	def swapable_image(self, event = None):
		self.swapable = True
		
	def clickFunction(self, event = None):
		ic()
		if self.swapable == True:
			if self.swapped == False: ## we're in an unswapped state; change to swapped state
				### ic("swapped = True... swapping images")
				self.swapped = True
				self.unclickedImage = self.unclicked_swap_image
				self.clickedImage = self.clicked_swap_image
			else:
				### ic("swapped = False")
				self.swapped = False
				self.unclickedImage = self.unclicked_image
				self.clickedImage = self.clicked_image
			
		if self.cget("state") != "disabled": #Ignore click if button is disabled
			self.toggleState *= -1
			
			if self.toggleState == -1:
				self.config(image = self.clickedImage)
			else:
				self.config(image = self.unclickedImage)

