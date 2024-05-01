from constants import *

projection_ratios = {
	"ClassicTV (4:3)": 
	{
		"ratio": "4:3",
	},
	"IMAX (19:10)": 
	{
		"ratio": "19:10",
	},
	"HDTV (16:9)": 
	{
		"ratio": "16:9",
	},
	"VistaVision (37:20)": 
	{
		"ratio": "37:20",
	},
	"CinemaScope (21:9)":
	{
		"ratio": "21:9",
	},
	"Anamorphic Widescreen(239:100)": 
	{
		"ratio": "239:100",
	},
	"MGM 65 (69:25)": 
	{
		"ratio": "69:25",
	}
}

## testing
if __name__ == "__main__":
	for ratio, properties in projection_ratios.items():
		print(ratio)
		
		for item, specs in properties.items():
			print("\t", item, ":", specs)

	## direct access
	print(projection_ratios["CinemaScope"]["ratio"])

	## direct access to numerator and denominator
	numerator, denominator = projection_ratios["CinemaScope"]["ratio"].split(":")
	print("numerator: ", numerator, ", denominator: ", denominator)
	## use of numerator and denominator
	result = int(numerator) / int(denominator)
	print("result: ", result)
	
	projection = "MGM 65"
	
	print("projection: ", projection)
	print("ratio: ", projection_ratios[projection]["ratio"])
