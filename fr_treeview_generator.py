from tkinter import *
from tkinter.ttk import *

class TreeFrame(Frame):
	def __init__(self, parent, number_of_columns):
		## instance variables
		self._cids = []
		self.treeview = None
		self.parent = parent
		## associate with parent
		super().__init__(parent)
		self.grid()

		
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
		self.cid_generator(number_of_columns)
		self._configure_columns(column_specs)
		self._configure_headings(heading_specs)
		
	def build_file_data(self, file_list, path_list):
		data = []
		for i in range(len(file_list)):
			## create shortened file path so we're only seeing
			## the lowest sub-directory where the image lives
			path_parts = path_list[i].split("/")
			last_part = len(path_parts) - 1
			short_path = "/" + path_parts[last_part] + "/"
			## put file name and shortened path into data
			data.append((file_list[i], short_path, "", ""))
		
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

	number_of_columns = 4
	tree_frame = TreeFrame(window, number_of_columns)
	window.mainloop()

if __name__ == "__main__":
	main()
