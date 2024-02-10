import os
import cv2

def generate_video():
	shoot_on_threes = True
	shoot_on_twos = False
	fps = 24
	
	in_path = "../image_sequence/"
	out_path = in_path
	video_name = 'lisa_turnaround_004.mp4'

	## compile a list of images from which to create the video
	images = []
	
	for img in os.listdir(in_path):
		if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith(".png"):
			images.append(img)
   
    ## create the video codec from the given characters
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')

	## set the frame width and height from
	## the width and height of first image in the series
	frame = cv2.imread(os.path.join(in_path, images[0]))
	height, width, layers = frame.shape
	
	## full path/file name of video to write
	out_file_path = os.path.join(out_path, video_name)
	## 
	video = cv2.VideoWriter(out_file_path, fourcc, fps, (width, height))

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
