from ap_constants import *

projection_ratios = {
	"ClassicTV": 
	{
		"term1": 4,
		"term2": 3,
		"projection_width": 960,
		"projection_height": 720,
	},
	"FHD TV": 
	{
		"term1": 16,
		"term2": 9,
		"projection_width": 1280,
		"projection_height": 720,
	},
	"Anamorphic": 
	{
		"term1": 239,
		"term2": 100,
		"projection_width": 1280,
		"projection_height": 536,
	},
}

## testing
if __name__ == "__main__":
	print("everything:")
	for ratio, properties in projection_ratios.items():
		print(ratio)
		
		for item, specs in properties.items():
			print("\t", item, ":", specs)

	## direct access
	print("\ndirection access:")
	print(projection_ratios["ClassicTV"]["term2"])

	## direct access to antecedent and consequent
	print("\nantecedent and consequent:")
	antecedent = projection_ratios["Anamorphic"]["term1"]
	consequent = projection_ratios["Anamorphic"]["term2"]
	print("antecedent: ", antecedent, ", consequent: ", consequent)
	## use of numerator and denominator
	result = int(antecedent) / int(consequent)
	print("result: ", result)
	
	projection = "ClassicTV"
	
	print("projection: ", projection)
	print("term1: ", projection_ratios[projection]["term1"])

	value = "ClassicTV"
	
	print("as a passed values:")
	my_ratio = projection_ratios[value]["term1"], projection_ratios[value]["term2"]
	print(my_ratio)

	value = "Anamorphic"

	print("As a fitted projection:")
	my_fitted_projection = projection_ratios[value]["projection_width"], projection_ratios[value]["projection_height"]
	print(my_fitted_projection)