## View part of the Model/View/Control for files to be processed.
from tkinter import *
from tkinter.ttk import Treeview, Frame

class FileNamesFrame(Frame):
	def __init__(self, parent):
		super().__init__(parent)
		self.parent = parent
		self.grid(sticky = (N, E, W, S))
		self.initUI()
	
	def initUI(self):
		
		data = [ ["Lisa_Turnaround_1920x1080_0000.png", "image_sequence/", "R|C|H|V|D|I"],
					["Lisa_Turnaround_1920x1080_0001.png", "image_sequence/", "R|C|H|V|D|I"],
					["Lisa_Turnaround_1920x1080_0002.png", "image_sequence/", "R|C|H|V|D|I"],
					["Lisa_Turnaround_1920x1080_0003.png", "image_sequence/", "R|C|H|V|D|I"],
					["Lisa_Turnaround_1920x1080_0004.png", "image_sequence/", "R|C|H|V|D|I"],
					["Lisa_Turnaround_1920x1080_0005.png", "image_sequence/", "R|C|H|V|D|I"],
					["Lisa_Turnaround_1920x1080_0006.png", "image_sequence/", "R|C|H|V|D|I"],
					["Lisa_Turnaround_1920x1080_0007.png", "image_sequence/", "R|C|H|V|D|I"]]
		
		tree = Treeview(self, columns = ("file_name", "location"))
		tree.heading('#0', text = "File Name")
		tree.heading('#1', text = "Location")
		tree.column('#1', anchor = E)
		tree.heading("#2", text = "SFX")
		tree.column("#2", anchor = E)
		tree.tag_configure("evenrow", background = "khaki3")
		tree.tag_configure("oddrow", background = "khaki1")
		
		i = 0
		
		for data_item in data:
			if (i % 2 ==  0):
				tree.insert("", index = END, text = data_item[0], values = (data_item[1], data_item[2]), tags = ("oddrow",))
			else:
				tree.insert("", index = END, text = data_item[0], values = (data_item[1], data_item[2]), tags = ('evenrow',))
				
			i += 1
			
		tree.pack(fill = BOTH, expand = True)
		self.pack()
		
def main():
	window = Tk()
	file_names_frame = FileNamesFrame(window)
	window.title("FileNamesFrame Demo")
	window.geometry("+300+300")
	window.grid_propagate(False)
	window.mainloop()
	
if __name__ ==  '__main__':
	main()