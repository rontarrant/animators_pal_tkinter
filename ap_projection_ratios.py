from constants import *

projection_ratios = {
	"ClassicTV (4:3)": 
	{
		"ratio": "4:3",
	},
	"HDTV (16:9)": 
	{
		"ratio": "16:9",
	},
	"Anamorphic Widescreen (239:100)": 
	{
		"ratio": "239:100",
	},
}

## testing
if __name__ == "__main__":
	for ratio, properties in projection_ratios.items():
		print(ratio)
		
		for item, specs in properties.items():
			print("\t", item, ":", specs)

	## direct access
	print(projection_ratios["ClassicTV (4:3)"]["ratio"])

	## direct access to numerator and denominator
	numerator, denominator = projection_ratios["Anamorphic Widescreen (239:100)"]["ratio"].split(":")
	print("numerator: ", numerator, ", denominator: ", denominator)
	## use of numerator and denominator
	result = int(numerator) / int(denominator)
	print("result: ", result)
	
	projection = "ClassicTV (4:3)"
	
	print("projection: ", projection)
	print("ratio: ", projection_ratios[projection]["ratio"])
