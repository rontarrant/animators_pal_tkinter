from ap_screen_resolutions import *

options = []

def build_options():
	for ratio, properties in screen_resolutions.items():
		option = ratio + " (" + str(properties["width"]) + "x" + str(properties["height"]) + ")"
		options.append(option)


build_options()
print(options)