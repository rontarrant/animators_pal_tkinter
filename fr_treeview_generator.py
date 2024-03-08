from tkinter import *
from tkinter.ttk import *

## python
import os
import sys

## local
from image_collection import TKImageCollection
from image_ap import APImage

class TreeFrame(Frame):
	def __init__(self, parent, column_count):
		## instance variables
		self._cids = []
		self.treeview = None
		self.parent = parent
		## associate with parent
		super().__init__(parent)
		self.grid()

		## make sure we have a collection of images
		self.image_collection = TKImageCollection()

		## total width: 380
		column_specs = {
			"#0": {"width": 175, "minwidth": 50, "anchor": W, "stretch": False},
			"#1": {"width": 125, "minwidth": 50, "anchor": W, "stretch": True},
			"#2": {"width": 40, "minwidth": 40, "anchor": W, "stretch": True},
			"#3": {"width": 40, "minwidth": 40, "anchor": W, "stretch": True}
		}

		heading_specs = {
			"#0": {"text": "File Name", "command": lambda: self.set_col_width("#0"), "anchor": W, "image": ''},
			"#1": {"text": "Location", "command": lambda: self.set_col_width("#1"), "anchor": E, "image": ''},
			"#2": {"text": "Wd", "command": lambda: self.set_col_width("#2"), "anchor": W, "image": ''},
			"#3": {"text": "Ht", "command": lambda: self.set_col_width("#3"), "anchor": W, "image": ''}
		}

		## configure properties
		self.treeview = Treeview(self)
		self.treeview.pack(expand = True, fill = BOTH)
		self.cid_generator(column_count)
		self._configure_columns(column_specs)
		self._configure_headings(heading_specs)
	
	## Because all the image file names are already stored in
	## the image_collection, we need a way to tell where the 
	## newly-added file names start in the image_collection.
	## We do this will a bit of simple math in FileMenu.add_files().
	## When the file Add Images dialog closes, and before we start
	## adding the new images, we get the length of the image_collection.
	## Then we add the new files and get the length again. The difference
	## is passed to build_file_data() as new_file_count.
	## In the current method, we again look at the length of
	## the image_collection and set a count. In the for loop,
	## do a countdown until we countdown to new_file_count. Only
	## then do we start adding images.
	## The purpose of all this is to avoid adding the same image
	## file names to the Treeview over and over each time we add
	## new images.
	def build_file_data(self, new_file_count):
		## start with an empty list of images to add
		data = []
		## number of images already in the collection
		count = len(self.image_collection.images)
		
		for image in self.image_collection.images:
			## This keeps us from adding the images already
			## in the collection for a second time.
			if count > new_file_count:
				count -= 1
				continue
			## separate the file name from the path
			full_path = image
			file_name = os.path.split(full_path)[1]
			path = os.path.split(full_path)[0]
			## create shortened file path so we're only seeing
			## the lowest sub-directory where the image lives
			path_parts = path.split("/")
			last_part = len(path_parts) - 1
			short_path = "/" + path_parts[last_part] + "/"
			## put file name and shortened path into data
			data.append((file_name, short_path, "", ""))
		
		self.inject_data(data)

	def set_col_width(self, cid):
		print("Got cid: ", cid)
	'''
	CID Generator
	Creates IDs for Treeview columns
	Given an integer between 2 and 9, generates a list of cids
	like this "#0", "#1", "#2", etc.
	CID's cannot be changed.
	'''
	def cid_generator(self, columns):
		columns -= 1
		
		if columns > 1:
			if columns < 10:
				for i in range(columns):
					cid = "#" + str(i)
					self._cids.append(cid)
			else:
				print("Too many columns")
		else:
			print("Not enough columns")

	def _configure_columns(self, specs):
		self.treeview["columns"] = self._cids
		
		for cid, config in specs.items():
			self.treeview.column(cid, **config)

	def _configure_headings(self, specs):
		for cid, config in specs.items():
			self.treeview.heading(cid, **config)

	def inject_data(self, data):
		for item in data:
			self.treeview.insert("", "end", text = item[0], values = (item[1], item[2], item[3]))
		
		## local testing - show all data rows
		#'''
		for row in self.treeview.get_children():
			print(self.treeview.item(row)['text'], self.treeview.item(row)['values'])
		#'''
		
## testing
def main():
	window = Tk()
	#window.geometry("400x300")

	column_count = 4
	tree_frame = TreeFrame(window, column_count)
	window.mainloop()

if __name__ == "__main__":
	main()
