import cv2
import tkinter 
from PIL import Image, ImageTk

# Load an color image
image = cv2.imread('image_sequence/Lisa_Turnaround_1920x1080_0000.png')

#Rearrang the color channel
blue, green, red = cv2.split(image)
image = cv2.merge((red, green, blue))

# A root window for displaying objects
root = tkinter.Tk()  

# Convert the Image object into a TkPhoto object
photo = Image.fromarray(image)
imagetk = ImageTk.PhotoImage(image = photo) 

# Put it in the display window
tkinter.Label(root, image = imagetk).pack() 

root.mainloop() # Start the GUI
