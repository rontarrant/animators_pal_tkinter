def check_number(num, num_set):
	match num:
		case _ if num < num_set[0]:
			print("Number is less than the first number in the set")
		case _ if num < num_set[1]:
			print("Number is less than the second number in the set")
		case _ if num < num_set[2]:
			print("Number is less than the third number in the set")
		case _:
			print("Number is not less than any number in the set")

# Example usage:
num_set = [10, 20, 30]
check_number(15, num_set)