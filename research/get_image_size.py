import cv2
import sys
import os

## get the execution path
path = os.path.abspath(os.path.dirname(sys.argv[0]))

image = cv2.imread('images/bogey.tif')

print("type(image): ", type(image))
# <class 'numpy.ndarray'>

print("image.shape: ", image.shape)
print(type(image.shape))
# (225, 400, 3)
# <class 'tuple'>

height, width, channels = image.shape
print('width:  ', width)
print('height: ', height)
print('channel:', channels)
# width:   400
# height:  225
# channel: 3
