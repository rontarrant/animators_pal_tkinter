import cv2

def play_video():
	cap = cv2.VideoCapture("images/RemoteDog.mp4") # getting video from webcam

	while cap.isOpened():
		ret, img = cap.read()
		cv2.imshow("Frame",img)
		key = cv2.waitKey(1)
		
		if key == ord('q'):
			break

		if key == ord('p'):
			cv2.waitKey(-1) #wait until any key is pressed

	cap.release()
	cv2.destroyAllWindows()

play_video()