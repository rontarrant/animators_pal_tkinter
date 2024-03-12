# First you need to import the libraries in question.
import numpy
import cv2
from PIL import Image

# And then you need a PIL image to work with, for now, 
# an image from a local file is going to be used.
pillow_image = Image.open("images/demo1.jpg")

# The conversion from PIL to OpenCV is done with the
# handy NumPy method "numpy.array" which converts the 
# PIL image into a NumPy array.
# cv2.cvtColor does the trick for correcting the colour
# when converting between PIL and OpenCV Image formats via NumPy.
opencvImage = cv2.cvtColor(numpy.array(pillow_image), cv2.COLOR_RGB2BGR)

# Display the OpenCV image using inbuilt methods.
cv2.imshow('Demo 2 Image',opencvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Which results in:
