## play a video from RAM
import cv2
import numpy as np

## load the video into RAM
video_data = open('../images/RemoteDog.mp4', 'rb').read()

if video_data == None:
	print("failed to load")

## convert the video data to a NumPy array
video_array = np.frombuffer(video_data, dtype = np.uint8)

if video_array.any() == None:
	print("failed to convert")
	
## decode the video using OpenCV
video = cv2.imdecode(video_array, cv2.IMREAD_COLOR)

## Check if the video was loaded successfully
if video is not None:
	## Create a window to display the video
	cv2.namedWindow("Video from RAM", cv2.	WINDOW_NORMAL)
	cv2.resizeWindow("Video from RAM", 800, 600)
	
	## Play the video frame by frame
	for frame in video:
		cv2.inshow("Video from RAM", frame)
	
		## Break the loop if the 'q' key is pressed
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	
	cv2.destroyAllWindows()
else:
	print("decoding failed.")
