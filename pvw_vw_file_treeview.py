from tkinter import *
from tkinter.ttk import *

## python
import os
import sys

## local
from ap_image_collection import APImageCollection

class FileTreeview(Treeview):
	def __init__(self, parent, column_count, preview_thumbnail):
		## instance variables
		self._cids = []
		self.treeview = None
		self.parent = parent
		## associate with parent
		super().__init__(parent)
		self.grid()
		## make sure we have a collection of images
		self.image_collection = APImageCollection()

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
		self.grid(sticky = (N, E, W, S))
		self.cid_generator(column_count)
		self._configure_columns(column_specs)
		self._configure_headings(heading_specs)
		## The bound variable 'event' isn't used, but needs to be
		## mentioned in the lambda statement because it's returned
		## by something somewhere.
		self.bind('<<TreeviewSelect>>', lambda event: self.preview(preview_thumbnail))

	def preview(self, preview_thumbnail):
		'''
		Takes a method name for previewing the selected image.
		'''
		## find the selected item ID (iid) ie. row
		selected_iid = self.selection()[0]
		## # ic(self.selection())
		## get the full path and image file name
		row_number = self.index(self.selection()[0])
		## # ic(self.index(self.selection()[0]))
		preview_thumbnail(row_number)
	
	'''
	The purpose of all the mucking around in build_new_image_list()
	is to avoid adding the previously-added image file names
	to the Treeview each time we add new images.
	
	Previously-added image file names are already in
	the image_collection. So, we find the end of the list, and
	do a bit of simple math to find out where the new file names
	will be added.
	'''
	def build_new_image_list(self, new_file_count):
		## start with an empty list of images to add
		data = []
		## number of images already in the collection
		count = len(self.image_collection.images)
		
		## To get the file names to add,
		## look at each image in the collection...
		for image in self.image_collection.images:
			## This keeps us from re-adding pre-existing
			## images for a second time.
			if count > new_file_count:
				count -= 1
				continue
			## Now that we're past the pre-existing images,
			## we can get to work...
			## separate the file name from the path
			file_name = image.file_name
			path = image.path
			## create shortened file path so we're only seeing
			## the lowest sub-directory where the image lives
			path_parts = path.split("/")
			last_part = len(path_parts) - 1
			short_path = "/" + path_parts[last_part] + "/"
			## put file name and shortened path into data
			data.append((file_name, short_path, "", ""))
		
		## Now that we have a list of new images,
		## we can send them off to be inserted into the Treeview.
		self.inject_data(data)

	def set_col_width(self, cid):
		# ic(cid)
		pass
	'''
	CID Generator
	Creates IDs for Treeview columns
	Given an integer between 2 and 9, generates a list of cids
	like this "#0", "#1", "#2", etc.
	CID's cannot be changed.
	'''
	def cid_generator(self, columns):
		## The 0th column is created automatically
		## when the Treeview is instantiated, so we
		## decrease the count by one.
		columns -= 1
		
		if columns > 1:
			if columns < 10:
				for i in range(columns):
					cid = "#" + str(i)
					self._cids.append(cid)
			else:
				# ic("Too many columns")
				pass
		else:
			# ic("Not enough columns")
			pass

	def _configure_columns(self, specs):
		self["columns"] = self._cids
		
		for cid, config in specs.items():
			self.column(cid, **config)

	def _configure_headings(self, specs):
		for cid, config in specs.items():
			self.heading(cid, **config)

	def inject_data(self, data):
		for item in data:
			self.insert("", "end", text = item[0], values = (item[1], item[2], item[3]))

	## local testing - show all data rows
	def list_rows(self):
		for row in self.get_children():
			# ic(self.item(row)['text'], self.item(row)['values'])
			pass
		
## testing
def main():
	window = Tk()
	#window.geometry("400x300")

	def preview_method():
		pass
		## just a dummy function to satisfy instantiation requirements
		
	column_count = 4
	file_treeview = FileTreeview(window, column_count, preview_method)
	window.mainloop()

if __name__ == "__main__":
	main()
