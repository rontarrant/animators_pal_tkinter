'''
a class for column configuration specifications

Create an instance one of this class for each column of a Treeview.

'''
from tkinter import *
from tkinter.ttk import *

from collections.abc import Callable

class ColumnSpecs():
	@property
	def cid(self):
		return self._cid
		
	@cid.setter
	def cid(self, cid):
		if type(cid) == str: ## is it a string?
			if cid[:1] == "#": ## is the first character an octothorp?
				if cid[-1:].isdigit() == True: ## is the last digit a number?
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
		
	def __init__(self, cid):
		## instance variables
		self._cid: str = cid
		self._width: int
		self._minwidth: int
		self._anchor: str = W
		self._stretch: int
	
	def set_specs(self, width = 200, minwidth = 20, anchor = W, stretch = 1):
		self.width = width
		self.minwidth = minwidth
		self.anchor = anchor
		self.stretch = stretch

	def dump(self):
		print("ColumnSpecs:")
		print("cid: ", self.cid)
		print("width: ", self.width)
		print("anchor: ", self.anchor)
		print("minwidth: ", self.minwidth)
		print("stretch: ", self.stretch)


if __name__ == "__main__":

	colprop1 = ColumnSpecs("#0")
	colprop1.set_specs(width = 250, anchor = N)
	colprop1.dump()

	colprop2 = ColumnSpecs("#2")
	colprop2.set_specs(width = 20, anchor = E, minwidth = 30)
	colprop2.dump()

