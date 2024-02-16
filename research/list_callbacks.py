import tkinter as tk

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
button.bind("<Button-1>", hi)
button.bind("<Button-1>", salutations, "+")
button.bind("<Button-1>", and_so_forth, "+")
commands = button._tclCommands

for command in commands:
	print(command[13:])
	
button.pack()
root.mainloop()

'''
['1608603056064bye', '1608602964416hi', '1608604064896salutations', '1608604065024and_so_forth']
'''