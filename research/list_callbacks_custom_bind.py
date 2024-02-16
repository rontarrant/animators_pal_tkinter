import tkinter as tk

class CustomButton(tk.Button):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self._custom_bindings = []

	def bind(self, sequence = None, func = None, add = None):
		if func is None and add is None:
			return self._custom_bindings
		elif func is not None and add is None:
			self._custom_bindings = [func]
		elif func is not None and add is not None:
			self._custom_bindings.append(func)

		return super().bind(sequence = sequence, func = func, add = add)

def hi(event):
	print('hello')
	return hi

def bye():
	print('bye')
	return bye

def salutations(event):
	print('... and salutations...')
	return bye

def and_so_forth(event):
	print('... and so forth...')
	return bye

root = tk.Tk()
button = tk.Button(root, text = 'test', command = bye)
button.bind("<Button-1>", func = hi)
button.bind("<Button-1>", add = "+", func = salutations)
button.bind("<Button-1>", add = "+", func = and_so_forth)

button.pack()
callback_string = button.bind("<Button-1>")

line_count = 0
index = 0
commands_raw = {}
string = ""
commands = []

for character in callback_string:
	if character == '\n':
		commands_raw[index] = string
		string = ""
		line_count += 1
		index += 1
	else:
		string = string + character

for value in commands_raw.values():
	if value == "":
		continue
		
	temp = value[19:] ## chop off the first 19 characters -- if {"[xxxxxxxxxxxxx
	command_string_end = temp.find(" %#")
	command = temp[:command_string_end]
	commands.append(command)

for command in commands:
	print(command)

root.mainloop()

'''
if {"[2438675177600hi %# %b %f %h %k %s %t %w %x %y %A %E %K %N %W %T %X %Y %D]" == "break"} break

if {"[2438675177792salutations %# %b %f %h %k %s %t %w %x %y %A %E %K %N %W %T %X %Y %D]" == "break"} break

if {"[2438675177920and_so_forth %# %b %f %h %k %s %t %w %x %y %A %E %K %N %W %T %X %Y %D]" == "break"} break
'''