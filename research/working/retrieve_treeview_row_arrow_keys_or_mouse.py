from tkinter import *
from tkinter import ttk


class MainFrame(Tk):
	def __init__(self):
		Tk.__init__(self)

		self.geometry('500x300')
		self.title('Tkinter')

		self.tree  =  ttk.Treeview(self, height = 3)
		self.tree['columns']  =  ("#1", "#2", "#3")
		self.tree.place(relx = 0.02, y = 25, relwidth = 0.95, relheight = 0.6)

		self.tree.heading('#0', text = 'item')
		self.tree.heading('#1', text = 'cod')
		self.tree.heading('#2', text = 'name')
		self.tree.heading('#3', text = 'email')

		self.tree.column('#0', width = 50)
		self.tree.column('#1', width = 100)
		self.tree.column('#2', width = 100)
		self.tree.column('#3', width = 100)
		

		self.tree.insert('', END, text  =  'zero', values = ('0', 'nono0', 'a@x.com'))
		self.tree.insert('', END, text  =  'one', values = ('1', 'nono1', 'b@x.com'))
		self.tree.insert('', END, text  =  'two', values = ('2', 'nono2', 'c@x.com'))
		self.tree.insert('', END, text  =  'three', values = ('3', 'nono3', 'd@x.com'))
		self.tree.insert('', END, text  =  'four', values = ('4', 'nono4', 'e@x.com'))

		self.tree.bind('<<TreeviewSelect>>', self.tree_key)


		iid  =  self.tree.get_children()[0]
		self.tree.selection_set(iid)
		self.tree.focus_force()
		self.tree.focus(iid)
		self.tree.see(iid)
		return


	def tree_key(self, event = None):
		selected_iid  =  self.tree.selection()[0]
		current_idx  =  self.tree.index(selected_iid)
		item  =  self.tree.item(selected_iid, 'text')
		print("selected: ", selected_iid, ", item: ", item)

		print('Current Row:',current_idx)
		return


if __name__ == '__main__':
	app  =  MainFrame()
	app.mainloop()