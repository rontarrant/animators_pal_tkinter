'''
class for heading configuration properties

For each heading of a Treeview, create an instance of HeadingProperties.

HeadingProperties arguments:
cid -- column ID
	defaults: "#0", "#1", "#2", etc.
	Other than "#0", the rest can be arbiltrary strings
	This argument must be supplied when instantiating HeadingProperties.
	
text -- the string that appears in the column heading
	This argument must be supplied when instantiating HeadingProperties.

command = None -- the callback triggered when the user clicks the heading
	
anchor = W -- alignment of the heading
	defaults to W (left aligned)

image = "" -- the icon that shares the heading with the text (above)

'''
from tkinter import *
from tkinter.ttk import *

from collections.abc import Callable

class HeadingProperties():
	_cid: str
	_anchor: str = W
	_command: Callable[[], None]
	_image: str
	_text: str

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
		
	def __init__(self, cid, text, command = None, anchor = W, image = ""):
		self.cid = cid
		self.text = text
		self.command = command
		self.anchor = anchor
		self.image = image

	def dump(self):
		print("HeadingProperties:")
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
	headprop = HeadingProperties("#0", "column name", command = do_something)
	##headprop.dump()
	
	headprop2 = HeadingProperties("#1", "other column name")
	##headprop2.dump()

	headings_list = [headprop, headprop2]
	
	for heading in headings_list:
		heading.dump()
