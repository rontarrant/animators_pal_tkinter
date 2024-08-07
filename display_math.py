'''
Scale Image Size to Fit Projection Ratio
Math

Steps:
- get the display canvas size (1280x720)
- get the projection ratio from settings (TV, HDTV, or Widescreen)
- get the projection ratio dimensions that fit within the display canvas size (1280x720):
	- TV: 960x720
	- HDTV: 1280x720
	- Widescreen: 1280x536
- get the image ratio
- compare the image ratio to the projection ratio:
	- if image ratio > projection ratio (image is self.width_indexr):
		- divide image width by 1280 to get factor
		- divide image width and height by factor to get fitted dimensions
	- if image ratio < projection ratio (image is self.height_indexer):
		- divide image height by 720 to get factor
		- divide image width and height by factor to get fitted dimensions
	- if image ratio == projection ratio:
		- we're in HDTV; no matching necessary
		- no checkerboard needed
		- no letterboxing or pillarboxing needed
'''
class DisplayMath():
	def __init__(self, *args, **kwargs):
		## constants
		self.width_index = 0
		self.height_index = 1
		self.canvas_size = [1280, 720]
		self.projections = {	"ClassicTV (4:3)": [960, 720],
									"HDTV (16:9)": [1280, 720],
									"Anamorphic Widescreen (239:100)": [1280, 536]}

		self.projection_ratios = ["ClassicTV (4:3)", "HDTV (16:9)", "Anamorphic Widescreen (239:100)"]

		for j in range(3):
			projection_ratio = self.projection_ratios[j]
			print(f"Projection Ratio: {projection_ratio}\n")

			'''
			if projection_ratio == "ClassicTV (4:3)":
				projection_ratio_fit = [960, 720]
			elif projection_ratio == "HDTV (16:9)":
				projection_ratio_fit = [1280, 720]
			elif projection_ratio == "Anamorphic Widescreen (239:100)":
				projection_ratio_fit = [1280, 536]
			'''
			projection_ratio_fit = self.projections[projection_ratio]
			image_sizes = [[4556, 2244], ## manufactured widescreen
								[3281, 2445], ## still camera
								[1920, 1080], ## HDTV
								[3280, 1845]] ## HDTV

			for i in range(4):
				image_size = image_sizes[i]
				print(f"Image #{i} size: {image_size}")

				## Find out if the image is within 5% of a standard ratio

				image_ratio_decimal = image_size[self.width_index] / image_size[self.height_index]
				projection_ratio_decimal = projection_ratio_fit[self.width_index] / projection_ratio_fit[self.height_index]

				if image_ratio_decimal > projection_ratio_decimal:
					print("\timage is wider")
					print("\tfitting width\n\tcalculating height ")
					print(f"\t              image ratio:\t{round(image_ratio_decimal, 2)}")
					print(f"\t         projection ratio:\t{round(projection_ratio_decimal, 2)}")
					factor = image_size[self.width_index] / projection_ratio_fit[self.width_index]
					image_display_width = int(image_size[self.width_index] / factor)
					image_display_height = int(image_size[self.height_index] / factor)
				elif image_ratio_decimal < projection_ratio_decimal:
					print("\timage is higher")
					print("\tfitting height\n\tcalculating width ")
					print(f"\t              image ratio:\t{round(image_ratio_decimal, 2)}")
					print(f"\t         projection ratio:\t{round(projection_ratio_decimal, 2)}")
					factor = image_size_height = image_size[self.height_index] / projection_ratio_fit[self.height_index]
					image_display_width = int(image_size[self.width_index] / factor)
					image_display_height = int(image_size[self.height_index] / factor)
				else:
					## If the image ratio matches the projection ratio, we must be in HDTV
					print("\timage is the same height")
					print("\tno need to fit anything")
					print(f"\t              image ratio:\t{round(image_ratio_decimal, 2)}")
					print(f"\t         projection ratio:\t{round(projection_ratio_decimal, 2)}")
					factor = image_size_height = image_size[self.height_index] / projection_ratio_fit[self.height_index]
					image_display_width = int(image_size[self.width_index] / factor)
					image_display_height = int(image_size[self.height_index] / factor)

				print(f"\t        conversion factor:\t{factor}")
				print(f"\t             display size:\t{self.canvas_size[0]}\t{self.canvas_size[1]}")
				print(f"\tprojection_ratio_fit size:\t{projection_ratio_fit[0]}\t{projection_ratio_fit[1]}")
				print(f"\t       image display size:\t{image_display_width}\t{image_display_height}")
				print()
			print()

def main():
	display_math = DisplayMath()

if __name__ == "__main__":
	main()
