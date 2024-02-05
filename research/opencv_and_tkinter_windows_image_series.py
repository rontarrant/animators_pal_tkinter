from tkinter import *
from tkinter.ttk import *
import cv2
import numpy as np
from threading import *

'''
1) refactor window_Tk so it's a class.
2) hook up button so it closes both windows
'''

def main():
	video_window = Window_CV()
	main_window = Window_Tk(video_window)
	## set up threads for each window
	print("creating threads...")
	t1 = Thread(target = main_window.start_up)
	t2 = Thread(target = video_window.keep_it_open)
	## start the threads
	print("starting threads...")
	t1.start()
	t2.start()
	print("entering mainloop")
	main_window.mainloop()
	
	
class Window_Tk(Tk):
	def __init__(self, cv_window, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.geometry('200x200')
		button = Button(self, text = 'Quit')
		button.pack()
		button.configure(command = lambda: self.quit_this(cv_window))
	
	## dummy to simplify getting threads started
	def start_up(self):
		pass
		
	def quit_this(self, cv_window):
		cv_window.quit = True
		self.destroy()
		print("Quiting")


class Window_CV():
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.video = cv2.VideoCapture("images/lisa.mp4")
		self.fps = self.video.get(cv2.CAP_PROP_FPS)
		print(self.fps)

		self.number_of_frames = self.video.get(cv2.CAP_PROP_FRAME_COUNT)
		print("number of frames: ", self.number_of_frames)

		self.quit = False
	
	def keep_it_open(self):
		while(True):
			for frame_id in range(int(self.number_of_frames)):
				self.video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
				_, frame = self.video.read() ## Underscore: not using this value
				cv2.imshow('Lisa', frame)
				
				if cv2.waitKey(1) == ord('q'):
					self.quit = True
					break ## for loop
			
			if self.quit == True:
				break ## while loop

		
if __name__ == "__main__":
	main()
