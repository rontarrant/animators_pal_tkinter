'''
classes for heading and column configuration properties

For each heading/column of a Treeview, create an instance of each
class -- one HeadingSpecs and one ColumnProperties.

HeadingSpecs arguments:
cid -- column ID
	defaults: "#0", "#1", "#2", etc.
	or can be set to arbiltrary strings
	This argument must be supplied when instantiating HeadingSpecs.
	
text -- the string that appears in the column heading
	This argument must be supplied when instantiating HeadingSpecs.

command = None -- the callback triggered when the user clicks the heading
	
anchor = W -- alignment of the heading
	defaults to W (left aligned)

image = "" -- the icon that shares the heading with the text (above)

'''
from tkinter import *
from tkinter.ttk import *

from collections.abc import Callable

class HeadingSpecs():
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
	def text(self):
		return self._text
		
	@text.setter
	def text(self, text):
		if type(text) == str:
			self._text = text
		
	@property
	def command(self):
		return self._command
	
	@command.setter
	def command(self, command):
		if isinstance(command, Callable): ## is it a callable function/method?
			self._command = command
		else:
			self._command = None
			print("command isn't callable")
		
	@property
	def anchor(self):
		return self._anchor
		
	@anchor.setter
	def anchor(self, anchor):
		if type(anchor) == str:
			self._anchor = anchor
		
	def __init__(self, cid):
		## instance variables
		self._cid: str = cid
		self._anchor: str = W
		self._command: Callable[[], None]
		self._image: str
		self._text: str
	
	def set_specs(self, text, command = None, anchor = W, image = ""):
		self.text = text
		self.command = command
		self.anchor = anchor
		self.image = image

	def dump(self):
		print("HeadingSpecs:")
		print("cid: ", self.cid)
		print("text: ", self.text)
		print("anchor: ", self.anchor)
		print("image: ", self.image)

		if self.command:
			print("command: ", self.command)
			self.command()

def do_something():
	print("we're doing something")
	
if __name__ == "__main__":
	headprop1 = HeadingSpecs("#0")
	## If the arguments are given in order, they don't have to be named.
	headprop1.set_specs("column name", do_something)
	##headprop.dump()
	
	headprop2 = HeadingSpecs("#1")
	headprop2.set_specs("other column name", anchor = S, image = "images/my_image.png")
	##headprop2.dump()

	headings_list = [headprop1, headprop2]
	
	for heading in headings_list:
		heading.dump()
