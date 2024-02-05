import cv2
import sys
import os

## get the execution path
path = os.path.abspath(os.path.dirname(sys.argv[0]))

im = cv2.imread('images/bogey.tif')

print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)
print(type(im.shape))
# (225, 400, 3)
# <class 'tuple'>

height, width, channels = im.shape
print('width:  ', width)
print('height: ', height)
print('channel:', channels)
# width:   400
# height:  225
# channel: 3
