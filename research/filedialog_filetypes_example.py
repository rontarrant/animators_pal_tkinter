from tkinter import filedialog

py_exts = r"*.py  *.py3 *.pyc  *.pyo  *.pyw  *.pyx  *.pyd  *.pxd  *.pyi  *.pyi  *.pyz  *.pywz *.rpy  *.pyde *.pyp  *.pyt  *.xpy  *.ipynb"  

filename = filedialog.askopenfilename(title="Select a File", filetypes=(("python files", py_exts), ("all files", "*.*")))
