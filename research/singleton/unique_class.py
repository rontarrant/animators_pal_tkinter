## Unique class example
class Unique:
	## define some static variables here
	x = 1
	
	@classmethod
	def init(cls):
		## define any computation performed when assigning to a "new"
		## object
		return cls

## testing
if __name__ == "__main__":
	A = Unique.init()
	B = Unique.init()
	
	print("At first, B.x = {} and A.x = {}".format(B.x, A.x))
	A.x = 2
	print("After A.x = 2...")
	print("Now both B.x = {} and A.x = {}\n".format(B.x, A.x))
