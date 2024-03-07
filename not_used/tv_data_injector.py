'''
treeview_data_stuffer.py
stuffs data into a Treeview
- make sure we have the right number of columns/headings for the data we're stuffing
- make sure the data types are right per column
- stuff the data

Proceedure:
- pass in a data_types tuple so we know what each column expects
- type enforcement for data_types tuple
- type enforcement for all data?
'''
_types: tuple[...] ## at compile time, don't know the length or types yet
