import os
import cv2

def generate_video():
	shoot_on_threes = True
	shoot_on_twos = False
	fps = 24
	
	in_path = "D:/Documents/Programming/PythonCode/tkinter/animators_pal/image_sequence/"
	out_path = in_path
	video_name = 'lisa_turnaround_once_again.mp4'

	images = [img for img in os.listdir(in_path) if img.endswith(".jpg") or
			 img.endswith(".jpeg") or img.endswith(".png")]
   
	fourcc = cv2.VideoWriter_fourcc(*'mp4v') 

	frame = cv2.imread(os.path.join(in_path, images[0]))
	
	# setting the frame width, height width from
	# the width, height of first image 
	height, width, layers = frame.shape

	video = cv2.VideoWriter(os.path.join(in_path, video_name), fourcc, fps, (width, height))
	print("video: ", video_name)
	# Appending the images to the video one by one 
	for image in images:
		if shoot_on_threes == True:
			for frame_hold in range(3):
				video.write(cv2.imread(os.path.join(in_path, image)))
		elif shoot_on_twos == True:
			for frame_hold in range(2):
				video.write(cv2.imread(os.path.join(in_path, image)))
		else:
			video.write(cv2.imread(os.path.join(in_path, image)))

		print("frame: ", os.path.join(in_path, image))
		
	# Deallocating memories taken for window creation 
	cv2.destroyAllWindows()
	video.release()  # releasing the video generated 
	
generate_video()
