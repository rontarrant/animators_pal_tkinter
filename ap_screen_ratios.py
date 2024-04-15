screen_ratios = {
	"ClassicTV": 
	{
		"ratio": "4:3",
		"fraction": "1.33:1",
	},
	"IMAX": 
	{
		"ratio": "22:16",
		"fraction": "1.9:1",
	},
	"HDTV": 
	{
		"ratio": "16:9",
		"fraction": "1.78:1",
	},
	"VistaVision": 
	{
		"ratio": "37:20",
		"fraction": "1.85:1",
	},
	"CinemaScope":
	{
		"ratio": "21:9",
		"fraction": "2.35:1",
	},
	"Anamorphic Widescreen": 
	{
		"ratio": "239:100",
		"fraction": "2.39:1",
	},
	"MGM 65": 
	{
		"ratio": "69:25",
		"fraction": "2.76:1"
	}
}

## testing
for ratio, properties in screen_ratios.items():
	print(ratio)
	
	for item, specs in properties.items():
		print("\t", item, ":", specs)
