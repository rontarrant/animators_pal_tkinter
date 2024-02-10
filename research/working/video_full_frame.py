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

		cv2.imshow('Lisa', frame)
		
		if cv2.waitKey(1) == ord('q'):
			quit = True
			break ## breaks out of the for loop
	
	if quit == True:
		break ## breaks out of the while loop

video.release()
cv2.destroyAllWindows()

## NOTE replace play_video() with this