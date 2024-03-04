'''
CID Generator
Creates IDs for Treeview columns
Given an integer between 2 and 9, generates a list of cids.
'''

class CIDGenerator():
	def __init__(self, columns):
		## instance variables
		self.cids = []
		
		if columns > 1:
			if columns < 10:
				for i in range(columns):
					cid = "#" + str(i)
					self.cids.append(cid)
			else:
				print("Too many columns")
		else:
			print("Not enough columns")

## testing
if __name__ == "__main__":
	my_cid_gen = CIDGenerator(8)
	print(my_cid_gen.cids)

	my_other_cid_gen = CIDGenerator(4)
	print(my_other_cid_gen.cids)
	
	my_3rd_cid_gen = CIDGenerator(2)
	print(my_3rd_cid_gen.cids)
