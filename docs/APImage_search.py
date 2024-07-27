Search "APImage" (29 hits in 9 files of 34 searched)
  D:\Documents\Programming\PythonCode\tkinter\animators_pal\ap_image.py (2 hits)
	Line  17: class APImage():
	Line 233: 	my_ap_image = APImage(image_file_name)
  D:\Documents\Programming\PythonCode\tkinter\animators_pal\ap_image_collection.py (9 hits)
	Line 15: from ap_image import APImage
	Line 26: class APImageCollection():
	Line 37: 		if APImageCollection.__instance is None:
	Line 38: 			APImageCollection.__instance = APImageCollection()
	Line 40: 		return APImageCollection.__instance
	Line 50: 		## a list of APImages
	Line 83: 	image_collection = APImageCollection()
	Line 87: 		image = APImage(file_name)
  D:\Documents\Programming\PythonCode\tkinter\animators_pal\menu_file.py (4 hits)
	Line  10: from ap_image_collection import APImageCollection
	Line  11: from ap_image import APImage
	Line  20: 		self.ap_image_collection = APImageCollection.get_instance()
	Line 129: 				image = APImage(image_file_name)
  D:\Documents\Programming\PythonCode\tkinter\animators_pal\pvw_vw_file_treeview.py (2 hits)
	Line   9: from ap_image_collection import APImageCollection
	Line  21: 		self.ap_image_collection = APImageCollection.get_instance()
  D:\Documents\Programming\PythonCode\tkinter\animators_pal\pvw_vw_thumbnail_canvas.py (4 hits)
	Line   3: Displays a TKImage selected in the Treeview (and stored in APImageCollection)
	Line  13: from ap_image_collection import APImageCollection
	Line  33: 		self.ap_image_collection = APImageCollection.get_instance()
	Line 100: 	image_collection = APImageCollection()
  D:\Documents\Programming\PythonCode\tkinter\animators_pal\vdo_mim_frame.py (1 hit)
	Line  18: 		self.ap_image_collection = APImageCollection.get_instance()
  D:\Documents\Programming\PythonCode\tkinter\animators_pal\vdo_vw_canvas.py (4 hits)
	Line  3: Displays a flipbook of TKImages collected in a APImageCollection. 
	Line 10: from ap_image_collection import APImageCollection
	Line 11: from ap_image import APImage
	Line 38: 		self.ap_image_collection = APImageCollection.get_instance()
  D:\Documents\Programming\PythonCode\tkinter\animators_pal\vdo_vw_controls.py (1 hit)
	Line  29: 		self.ap_image_collection = APImageCollection.get_instance()
  D:\Documents\Programming\PythonCode\tkinter\animators_pal\vdo_vw_video_info_mim.py (2 hits)
	Line  27: from ap_image_collection import APImageCollection
	Line  41: 		self.ap_image_collection = APImageCollection.get_instance()
