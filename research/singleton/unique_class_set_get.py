## Unique class example
## doesn't work as a regular class
## Setters and getters need to refer to attributes
## with their full names which includes the class name.
class Unique:
	## define some static variables here
	x = 1
	
	@classmethod
	def init(cls):
		## define any computation performed when assigning to a "new"
		## object
		return cls
		
	def set(value):
		Unique.x = value
		
	def get():
		return Unique.x

## testing
if __name__ == "__main__":
	A = Unique.init()
	B = Unique.init()
	
	print("B.x = {}, A.x = {}".format(B.get(), A.get()))
	A.set(2)
	print("After A.set(2)...")
	print("B.x = {}, A.x = {}".format(B.get(), A.get()))
