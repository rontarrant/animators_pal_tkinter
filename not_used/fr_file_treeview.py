## TreeFrame
from tkinter import *
from tkinter.ttk import *

class TreeGenFrame():
	treeview: Treeview = None
	
	def __init__(self, parent):
		self.treeview = Treeview()

	'''
	CID Generator
	Creates IDs for Treeview columns
	Given an integer between 2 and 9, generates a list of cids
	like this "#0", "#1", "#2", etc.
	CID's cannot be changed.
	'''
	def cid_generator(self, columns):
		## instance variables
		self.cids = []
		
		if columns > 1:
			if columns < 10:
				for i in range(columns):
					cid = "#" + str(i)
					self.cids.append(cid)
			else:
				## # ic("Too many columns")
		else:
			## # ic("Not enough columns")

## testing
if __name__ == "__main__":
	window = Tk()
	mytreeframe = TreeFrame(window)
