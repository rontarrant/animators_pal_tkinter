'''
This test:
- builds a video from a series of images,
- saves it, and
- plays it from saved the file.
'''
import os
import cv2

class OpenCVVideo():
	def generate_video(self, video_to_create, in_path):

		## compile a list of images from which to create the video
		images = []
		
		for img in os.listdir(in_path):
			if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith(".png"):
				images.append(img)
		
		return images

	def save_video(self, images, video_to_save, out_path):
		shoot_on_threes = True
		shoot_on_twos = False
		fps = 24
		## create the video codec from the given characters
		fourcc = cv2.VideoWriter_fourcc(*'mp4v')

		## set the frame width and height from
		## the width and height of first image in the series
		frame = cv2.imread(os.path.join(out_path, images[0]))
		height, width, layers = frame.shape
		
		## full path/file name of video to write
		out_file_path = os.path.join(out_path, video_to_save)
		## 
		video = cv2.VideoWriter(out_file_path, fourcc, fps, (width, height))

		# Appending the images to the video one by one 
		for image in images:
			if shoot_on_threes == True:
				for frame_hold in range(3):
					video.write(cv2.imread(os.path.join(out_path, image)))
			elif shoot_on_twos == True:
				for frame_hold in range(2):
					video.write(cv2.imread(os.path.join(out_path, image)))
			else:
				video.write(cv2.imread(os.path.join(out_path, image)))

			print("frame: ", os.path.join(out_path, image))
			
		# Deallocating memories taken for window creation 
		cv2.destroyAllWindows()
		video.release()  # releasing the video generated 

	def play_video(self, video_to_play, in_path):
		video = cv2.VideoCapture(in_path + video_to_play) # getting video from webcam

		fps = video.get(cv2.CAP_PROP_FPS)
		print(fps)

		number_of_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
		print("number of frames: ", number_of_frames)

		quit = False

		while(True):
			for frame_id in range(int(number_of_frames)):
				video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
				ret, frame = video.read()

				cv2.imshow('Lisa', frame)
				
				if cv2.waitKey(1) == ord('q'):
					quit = True
					break ## breaks out of the for loop
			
			if quit == True:
				break ## breaks out of the while loop

		video.release()
		cv2.destroyAllWindows()

my_video = OpenCVVideo()
video_name = 'lisa_003.mp4'
video_path = "image_sequence/"

image_sequence = my_video.generate_video(video_name, video_path)
my_video.save_video(image_sequence, video_name, video_path)
my_video.play_video(video_name, video_path)
