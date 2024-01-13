import cv2
import os

def generate_video():
	shoot_on_threes = True
	shoot_on_twos = False
	fps = 24

	path = 'D:/Documents/Programming/PythonCode/tkinter/animators_pal/image_sequence/'
	out_path = path
	out_video_name = 'lisa_turn_around_on_3s_again.mp4'
	out_video_full_path = out_path + out_video_name

	pre_frames = os.listdir(path)
	frames = []

	for i in pre_frames:
		 i = path + i
		 frames.append(i)

	cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

	frame = cv2.imread(frames[0])
	size = list(frame.shape)
	del size[2]
	size.reverse()
	print("video size:", size)
	#output video name, fourcc, fps, size
	video = cv2.VideoWriter(out_video_full_path, cv2_fourcc, fps, size)

	for i in range(len(frames)): 
			if shoot_on_threes == True:
				for frame_hold in range(3):
					video.write(cv2.imread(frames[i]))
					print('frame ', i + 1, ' of ', len(frames))
			elif shoot_on_twos == True:
				for frame_hold in range(2):
						video.write(cv2.imread(frames[i]))
						print('frame ', i + 1, ' of ', len(frames))
			else:
				video.write(cv2.imread(frames[i]))
				print('frame ', i + 1, ' of ', len(frames))

	video.release()
	print('outputed video to ', out_path)

generate_video()
