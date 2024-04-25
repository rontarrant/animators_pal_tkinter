screen_resolutions = { 
	"8k": 
	{
		"width": 7680,
		"height": 4320,
		"ClassicTV": 
		{
			"displacement": 960,
			"width": 5760,
			"height": 4320
		},
		"IMAX": 
		{
			"displacement": 139,
			"width": 7680,
			"height": 4042
		},
		"HDTV": 
		{
			"displacement": 0,
			"width": 7680,
			"height": 4320
		},
		"VistaVision": 
		{
			"displacement": 84,
			"width": 7680,
			"height": 4151
		},
		"CinemaScope":
		{
			"displacement": 514,
			"width": 7680,
			"height": 3291
		},
		"Anamorphic Widescreen": 
		{
			"displacement": 553,
			"width": 7680,
			"height": 3213
		},
		"MGM 65": 
		{
			"displacement": 769,
			"width": 7680,
			"height": 2783
		}
	},
	"4k": 
	{
		"width": 3840,
		"height": 2160,
		"ClassicTV": 
		{
			"displacement": 480,
			"width": 2880,
			"height": 2160
		},
		"IMAX": 
		{
			"displacement": 70,
			"width": 3088,
			"height": 2020
		},
		"HDTV": 
		{
			"displacement": 0,
			"width": 3840,
			"height": 2160
		},
		"VistaVision": 
		{
			"displacement": 42,
			"width": 3840,
			"height": 2076
		},
		"CinemaScope": 
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
		"MGM 65": 
		{
			"displacement": 384,
			"width": 3840,
			"height": 1391
		}
	},
	"1080p": 
	{
		"width": 1920,
		"height": 1080,
		"ClassicTV": 
		{
			"displacement": 240,
			"width": 1440,
			"height": 1080
		},
		"IMAX": 
		{
			"displacement": 35,
			"width": 1920,
			"height": 1010
		},
		"HDTV": 
		{
			"displacement": 0,
			"width": 1920,
			"height": 1080
		},
		"VistaVision": 
		{
			"displacement": 21,
			"width": 1920,
			"height": 1038
		},
		"CinemaScope": 
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
		"MGM 65": 
		{
			"displacement": 192,
			"width": 1920,
			"height": 696
		}
	},
	"720p": 
	{
		"width": 1280,
		"height": 720,
		"ClassicTV": 
		{
			"displacement": 160,
			"width": 960,
			"height": 720
		},
		"IMAX": 
		{
			"displacement": 23,
			"width": 1280,
			"height": 674
		},
		"HDTV": 
		{
			"displacement": 0,
			"width": 1280,
			"height": 720
		},
		"VistaVision": 
		{
			"displacement": 14,
			"width": 1280,
			"height": 692
		},
		"CinemaScope": 
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
		"MGM 65": 
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
	print("VistaVision width @ 4k: ", screen_resolutions["4k"]["VistaVision"]["width"])
	## set a resolution
	resolution = "4k"
	print("key: ", resolution)
	print(screen_resolutions[resolution])