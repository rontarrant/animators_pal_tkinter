from tkinter import *
from tkinter.ttk import *

class TreeFrame(Frame):
	def __init__(self, parent, num_columns):
		super().__init__(parent)
		self.grid()
		## instance variables
		self._cids = []
		self.treeview = Treeview(self)
		## column specs
		column_config = {
			"#0": {"width": 200, "minwidth": 50, "anchor": W, "stretch": False},
			"#1": {"width": 100, "minwidth": 50, "anchor": W, "stretch": True},
			"#2": {"width": 40, "minwidth": 50, "anchor": W, "stretch": True},
			"#3": {"width": 40, "minwidth": 50, "anchor": W, "stretch": True}
		}
		
		self._configure_columns(column_config)
		## heading specs
		heading_config = {
			"#0": {"text": "File Name", "command": lambda: self.do_something("#0"), "anchor": W, "image": ''},
			"#1": {"text": "Location", "command": lambda: self.do_something("#1"), "anchor": W, "image": ''},
			"#2": {"text": "Width", "command": lambda: self.do_something("#2"), "anchor": W, "image": ''},
			"#3": {"text": "Height", "command": lambda: self.do_something("#3"), "anchor": W, "image": ''}
		}
		self._configure_headings(heading_config)

	def cid_generator(self, columns):
		## The first column is created automaticlly when
		## the Treeview is instantiated.
		self._cids -= 1
		
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
			print("configured columns: ", self.treeview["columns"])
			print("cid: ", cid)
			self.treeview.column(cid, **config)

	def _configure_headings(self, config):
		for cid, data in config.items():
			self.treeview.heading(cid, **data)

	def inject_data(self, data):
		for item in data:
			self.treeview.insert("", "end",
										text = item[0], 
										values = (item[1], item[2], item[3]))

	def do_something(self, cid):
		print("Clicked on heading: ", self.treeview.heading(cid)['text'])
		
def main():
	window = Tk()
	window.geometry("600x400")

	num_columns = 4
	## We decrease the number of columns by one because instantiating
	## the Treeview also creates column "#0".
	tree_frame = TreeFrame(window, num_columns)

	data = [
		("image_001.png", "./images", 1920, 1080),
		("image_001.png", "./images", 1920, 1080),
		("image_001.png", "./images", 1920, 1080),
		("image_001.png", "./images2", 1920, 1080)
	]
	tree_frame.inject_data(data)

	tree_frame.treeview.grid()

	window.mainloop()

if __name__ == "__main__":
	main()
