screen_resolutions = { 
	"8k": 
	{
		"resolution width": 7680,
		"resolution height": 4320,
		"ClassicTV": 
		{
			"h_offset": 960,
			"v_offset": 0,
			"projection width": 5760,
			"projection height": 4320
		},
		"FHD TV": 
		{
			"h_offset": 0,
			"v_offset": 0,
			"projection width": 7680,
			"projection height": 4320
		},
		"Anamorphic": 
		{
			"h_offset": 0,
			"v_offset": 553,
			"projection width": 7680,
			"projection height": 3213
		},
	},
	"4k": 
	{
		"resolution width": 3840,
		"resolution height": 2160,
		"ClassicTV": 
		{
			"h_offset": 480,
			"v_offset": 0,
			"projection width": 2880,
			"projection height": 2160
		},
		"FHD TV": 
		{
			"h_offset": 0,
			"v_offset": 0,
			"projection width": 3840,
			"projection height": 2160
		},
		"Anamorphic": 
		{
			"h_offset": 0,
			"v_offset": 277,
			"projection width": 3840,
			"projection height": 1607
		},
	},
	"1080p": 
	{
		"resolution width": 1920,
		"resolution height": 1080,
		"ClassicTV": 
		{
			"h_offset": 240,
			"v_offset": 0,
			"projection width": 1440,
			"projection height": 1080
		},
		"FHD TV": 
		{
			"h_offset": 0,
			"v_offset": 0,
			"projection width": 1920,
			"projection height": 1080
		},
		"Anamorphic": 
		{
			"h_offset": 0,
			"v_offset": 138,
			"projection width": 1920,
			"projection height": 803
		},
	},
	"720p": 
	{
		"resolution width": 1280,
		"resolution height": 720,
		"ClassicTV": 
		{
			"h_offset": 160,
			"v_offset": 0,
			"projection width": 960,
			"projection height": 720
		},
		"FHD TV": 
		{
			"h_offset": 0,
			"v_offset": 0,
			"projection width": 1280,
			"projection height": 720
		},
		"Anamorphic": 
		{
			"h_offset": 0,
			"v_offset": 92,
			"projection width": 1280,
			"projection height": 536
		},
	}
}

## testing
if __name__ == "__main__":

	for resolution, properties in screen_resolutions.items(): ## show the screen sizes
		print("resolution:", resolution) ##  (8k, 4k, 1080p, 720p)
		
		for item, property in properties.items(): ## width, height, resolution (by name)
			if item == "resolution width":
				print("\t" + item + ":", property)
			elif item == "resolution height":
				print("\t" + item + ":", property)
			else: ## Projection Sizes
				print("\t" + item)

				for resolution_property, sub_property in property.items():
					print("\t\t" + resolution_property, sub_property) ## displacement, width, height


	## direct access
	print("direct access:")
	print("HDTV (16:9) width @ 4k: ", screen_resolutions["4k"]["FHD TV"]["projection width"])
	## set a resolution
	resolution_key = "4k"
	print("key: ", resolution_key)
	print(screen_resolutions[resolution_key])
	## find a resolution
	nested_dictionary = screen_resolutions[resolution_key]
	print("nested_dictionary: \n", nested_dictionary, "\n\n")
	projection_key = "Anamorphic"
	
	new_dictionary = {projection_key: nested_dictionary[projection_key]}
	
	if list(new_dictionary.keys())[0] == projection_key:
		print("found it")
		print(new_dictionary)
	else:
		print("didn't found it")
	
	