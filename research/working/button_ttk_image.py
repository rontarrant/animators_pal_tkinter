from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Example(ttk.Frame):
	def __init__(self, master):
		ttk.Frame.__init__(self, master)
		master.title('Button Test')

		self.configure(padding='10 10 10 10')
		self.grid(column = 0, row = 0, sticky = (N, E, W, S))

		buttonImage = Image.open('images/play_64x64.png')

		# use self.buttonPhoto
		self.buttonPhoto = ImageTk.PhotoImage(buttonImage) 

		# use self.buttonPhoto
		myButton = ttk.Button(self, image = self.buttonPhoto, padding = '10 10 10 10')
		myButton.grid(column = 1, row = 1, sticky = (E, W))

if __name__ == "__main__":
	root = Tk()
	example = Example(root)
	root.mainloop()