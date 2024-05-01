screen_resolutions = { 
	"8k (7680x4320)": 
	{
		"width": 7680,
		"height": 4320,
		"ClassicTV (4:3)": 
		{
			"displacement": 960,
			"width": 5760,
			"height": 4320
		},
		"IMAX (19:10)": 
		{
			"displacement": 139,
			"width": 7680,
			"height": 4042
		},
		"HDTV (16:9)": 
		{
			"displacement": 0,
			"width": 7680,
			"height": 4320
		},
		"VistaVision (37:20)": 
		{
			"displacement": 84,
			"width": 7680,
			"height": 4151
		},
		"CinemaScope (21:9)":
		{
			"displacement": 514,
			"width": 7680,
			"height": 3291
		},
		"Anamorphic Widescreen(239:100)": 
		{
			"displacement": 553,
			"width": 7680,
			"height": 3213
		},
		"MGM 65 (69:25)": 
		{
			"displacement": 769,
			"width": 7680,
			"height": 2783
		}
	},
	"4k (3840x2160)": 
	{
		"width": 3840,
		"height": 2160,
		"ClassicTV (4:3)": 
		{
			"displacement": 480,
			"width": 2880,
			"height": 2160
		},
		"IMAX (19:10)": 
		{
			"displacement": 70,
			"width": 3088,
			"height": 2020
		},
		"HDTV (16:9)": 
		{
			"displacement": 0,
			"width": 3840,
			"height": 2160
		},
		"VistaVision (37:20)": 
		{
			"displacement": 42,
			"width": 3840,
			"height": 2076
		},
		"CinemaScope (21:9)": 
		{
			"displacement": 257,
			"width": 3840,
			"height": 1646
		},
		"Anamorphic Widescreen": 
		{
			"displacement": 277,
			"width": 3840,
			"height": 1607
		},
		"MGM 65 (69:25)": 
		{
			"displacement": 384,
			"width": 3840,
			"height": 1391
		}
	},
	"1080p (1920x1080)": 
	{
		"width": 1920,
		"height": 1080,
		"ClassicTV (4:3)": 
		{
			"displacement": 240,
			"width": 1440,
			"height": 1080
		},
		"IMAX (19:10)": 
		{
			"displacement": 35,
			"width": 1920,
			"height": 1010
		},
		"HDTV (16:9)": 
		{
			"displacement": 0,
			"width": 1920,
			"height": 1080
		},
		"VistaVision (37:20)": 
		{
			"displacement": 21,
			"width": 1920,
			"height": 1038
		},
		"CinemaScope (21:9)": 
		{
			"displacement": 129,
			"width": 1920,
			"height": 823
		},
		"Anamorphic Widescreen": 
		{
			"displacement": 138,
			"width": 1920,
			"height": 803
		},
		"MGM 65 (69:25)": 
		{
			"displacement": 192,
			"width": 1920,
			"height": 696
		}
	},
	"720p (1280x720)": 
	{
		"width": 1280,
		"height": 720,
		"ClassicTV (4:3)": 
		{
			"displacement": 160,
			"width": 960,
			"height": 720
		},
		"IMAX (19:10)": 
		{
			"displacement": 23,
			"width": 1280,
			"height": 674
		},
		"HDTV (16:9)": 
		{
			"displacement": 0,
			"width": 1280,
			"height": 720
		},
		"VistaVision (37:20)": 
		{
			"displacement": 14,
			"width": 1280,
			"height": 692
		},
		"CinemaScope (21:9)": 
		{
			"displacement": 86,
			"width": 1280,
			"height": 549
		},
		"Anamorphic Widescreen": 
		{
			"displacement": 92,
			"width": 1280,
			"height": 536
		},
		"MGM 65 (69:25)": 
		{
			"displacement": 128,
			"width": 1280,
			"height": 464
		}
	}
}

## testing
if __name__ == "__main__":

	for resolution, properties in screen_resolutions.items(): ## show the screen sizes
		print(resolution) ##  (8k, 4k, 1080p, 720p)
		
		for item, property in properties.items(): ## width, height, resolution (by name)
			if item == "width":
				print("\t" + item + ":", property)
			elif item == "height":
				print("\t" + item + ":", property)
			else: ## Projection Sizes
				print("\t" + item)

				for resolution_property, sub_property in property.items():
					print("\t\t" + resolution_property, sub_property) ## displacement, width, height


	## direct access
	print("direct access:")
	print("VistaVision (37:20) width @ 4k: ", screen_resolutions["4k (3840x2160)"]["VistaVision (37:20)"]["width"])
	## set a resolution
	resolution_key = "4k (3840x2160)"
	print("key: ", resolution_key)
	print(screen_resolutions[resolution_key])
	## find a resolution
	nested_dictionary = screen_resolutions[resolution_key]
	print("nested_dictionary: \n", nested_dictionary, "\n\n")
	projection_key = "CinemaScope (21:9)"
	
	new_dictionary = {projection_key: nested_dictionary[projection_key]}
	
	if list(new_dictionary.keys())[0] == projection_key:
		print("found it")
		print(new_dictionary)
	else:
		print("didn't found it")
	
	