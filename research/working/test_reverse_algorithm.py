## To get the algorithm to work in reverse, just change the
## '+' to a '-'

video_frames = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
frame_num = 0

## forward
for count in range(24):
	frame_num = (frame_num + 1) % len(video_frames)
	print(frame_num)


## reverse
for count in range(24):
	frame_num = (frame_num - 1) % len(video_frames)
	print(frame_num)

print("stage 3:")

for count in range(24):
	if frame_num == len(video_frames) - 1:
		break
		
	frame_num += 1
	print(frame_num)

'''
I'm working in Python. I have code in a for loop that steps through a Python list and, when it reaches the end, starts over at the beginning. What I'd like is for you to modify the for loop so that it stops at the end of the Python list and doesn't rewind to the beginning. Here's the code:

video_frames = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
frame_num = 0

for count in range(24):
	frame_num = (frame_num + 1) % len(video_frames)
	print(frame_num)
'''