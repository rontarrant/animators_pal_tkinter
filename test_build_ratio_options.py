from ap_projection_sizes import *

options = []

def build_options():
	
	for ratio, properties in projection_ratios.items():
		option = ratio + " (" + properties["ratio"] + ")"
		options.append(option)

build_options()
print(options)