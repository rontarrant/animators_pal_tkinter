'''
ColumnProperties class
Contains configuration properties for a single Treeview column.

'''
from tkinter import *
from tkinter.ttk import *

class ColumnProperties():
	@property
	def cid(self):
		return self._cid
		
	@cid.setter
	def cid(self, cid):
		if type(cid) == str: ## is it a string?
			if cid[:1] == "#": ## is the first character an octothorp?
				if cid[-1:].isdigit() == True: ## is the last character a number?
					self._cid = cid
		
	@property
	def anchor(self):
		return self._anchor
		
	@anchor.setter
	def anchor(self, anchor):
		if type(anchor) == str:
			self._anchor = anchor
		
	@property
	def width(self):
		return self._width
		
	@width.setter
	def width(self, value):
		if type(value) == int:
			self._width = value
		
	@property
	def minwidth(self):
		return self._minwidth
		
	@minwidth.setter
	def minwidth(self, value):
		if type(value) == int:
			self._minwidth = value
		
	@property
	def stretch(self):
		return self._stretch
		
	@stretch.setter
	def stretch(self, value):
		if type(value) == int:
			self._stretch = value
		
	def __init__(self, cid, width = 200, minwidth = 20, anchor = W, stretch = 1):
		_cid: str
		_width: int
		_minwidth: int
		_anchor: str = W
		_stretch: int

		self.cid = cid
		self.width = width
		self.minwidth = minwidth
		self.anchor = anchor
		self.stretch = stretch

	def dump(self):
		print("ColumnProperties:")
		print("cid: ", self.cid)
		print("width: ", self.width)
		print("anchor: ", self.anchor)
		print("minwidth: ", self.minwidth)
		print("stretch: ", self.stretch)

## testing	
if __name__ == "__main__":
	colprop = ColumnProperties("#2", 250, 40)
	colprop.dump()
