resolution_sizes = { 
	"8k": 
	{
		"width": 7680,
		"height": 4320,
	},
	"6k": 
	{
		"width": 6144,
		"height": 3456,
	},
	"5k": 
	{
		"width": 5120,
		"height": 2880,
	},
	"4k": 
	{
		"width": 3840,
		"height": 2160,
	},
	"3k": 
	{
		"width": 2880,
		"height": 1620,
	},
	"2k": 
	{
		"width": 2048,
		"height": 1152,
	},
	"1080p": 
	{
		"width": 1920,
		"height": 1080,
	},
	"720p": 
	{
		"width": 1280,
		"height": 720,
	}
}

## testing
if __name__ == "__main__":
	for aspect_ratio, size in resolution_sizes.items():
		print(aspect_ratio)
		for dimension, value in size.items():
			print("\t" + dimension + ": " + str(value))

		