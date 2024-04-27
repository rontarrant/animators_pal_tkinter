from constants import *

projection_ratios = {
	"ClassicTV": 
	{
		"ratio": "4:3",
	},
	"IMAX": 
	{
		"ratio": "19:10",
	},
	"HDTV": 
	{
		"ratio": "16:9",
	},
	"VistaVision": 
	{
		"ratio": "37:20",
	},
	"CinemaScope":
	{
		"ratio": "21:9",
	},
	"Anamorphic Widescreen": 
	{
		"ratio": "239:100",
	},
	"MGM 65": 
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
