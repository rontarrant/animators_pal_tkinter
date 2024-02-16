from tkinter import *

class ImageButton(Button):
	def __init__(self, master, image1, image2, *args, **kwargs):
		self.unclickedImage = PhotoImage(file = image1)
		self.clickedImage = PhotoImage(file = image2)
		super().__init__(master, *args, image = self.unclickedImage, **kwargs)
		self.toggleState = 1
		self.bind("<Button-1>", self.clickFunction)
		
	def clickFunction(self, event = None):
		if self.cget("state") != "disabled": #Ignore click if button is disabled
			self.toggleState *= -1
			
			if self.toggleState == -1:
				self.config(image = self.clickedImage)
			else:
				self.config(image = self.unclickedImage)

class Example(Frame):

	def __init__(self, master, *args, **kwargs):
		super().__init__(master, *args, **kwargs)
		self.init_ui()

	def init_ui(self):
		ImageButton(self, "./images/play_64x64.png", "./images/play_64x64.png").pack(side = LEFT)
		ImageButton(self, "./images/stop_64x64.png", "./images/stop_64x64.png").pack(side = RIGHT)


def main():

	root = Tk()
	root.configure(bg = 'white')
	ex = Example(root)
	ex.pack(fill = "both", expand = True)
	root.title('')
	root.geometry("400x100+300+300")
	root.mainloop()


if __name__ == '__main__':
	main()