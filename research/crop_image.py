import cv2 

img = cv2.imread("images/one_dollar.jpg") 
print(type(img)) 
  
# Shape of the image 
print("Shape of the image", img.shape) 

# [rows, columns] 
crop = img[20:175, 300:525]    ## order: y-start:x-start, y-end:x-end
  
cv2.imshow('original', img) 
cv2.imshow('cropped', crop) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
