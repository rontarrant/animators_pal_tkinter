import numpy as np
import cv2

video = cv2.VideoCapture("images/lisa.mp4")
fps = video.get(cv2.CAP_PROP_FPS)
print(fps)

number_of_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
print("number of frames: ", number_of_frames)

quit = False

while(True):
	for frame_id in range(int(number_of_frames)):
		video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
		ret, frame = video.read()
		
		## create a blank frame based on the size of the video
		small_frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
		height, width, channels = frame.shape
		image = 255 * np.ones(shape = (height, width, channels), dtype = np.uint8)
		
		small_frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
		## build four small frames & stuff them into the big frame
		image[:height//2, :width//2] = small_frame
		temp_image = cv2.resize(small_frame, (0, 0), fx = height/width, fy = width/height)
		image[:height//2, width//2:] = cv2.rotate(temp_image, cv2.ROTATE_90_CLOCKWISE)
		image[height//2:, :width//2] = cv2.rotate(small_frame, cv2.ROTATE_180)
		temp_image = cv2.resize(small_frame, (0, 0), fx = height/width, fy = width/height)
		image[height//2:, width//2:] = cv2.rotate(temp_image, cv2.ROTATE_90_COUNTERCLOCKWISE)

		cv2.imshow('Lisa', image)
		
		if cv2.waitKey(1) == ord('q'):
			quit = True
			break ## breaks out of the for loop
	
	if quit == True:
		break ## breaks out of the while loop

video.release()
cv2.destroyAllWindows()

