'''
(This is a test module. Once everything's worked out, the function
will be included in APImage as a method.)

Display Math needs to provide two bits of information:
- whether or not the image needs a checkerboard behind it, and
- the dimensions the image will be resized to for viewing.

inputs:
- image width & height
- selected projection ratio

outputs:
- checkerboard on/off
- image display width & height

external data needed to do calculations:
- original image size (arg)
- the dictionary of projection ratios to look up:
	- width & height of projection ratio fitted to the display canvas
- the size of the display canvas (1280x720 for now)
- 

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

	def get_image_projection(self, image_size, projection_ratio):
		projection_ratio_fit = self.projections[projection_ratio]
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
			factor = image_size[self.height_index] / projection_ratio_fit[self.height_index]
			image_display_width = int(image_size[self.width_index] / factor)
			image_display_height = int(image_size[self.height_index] / factor)
		else:
			## If the image ratio matches the projection ratio, we must be in HDTV
			print("\timage is the same height")
			print("\tno need to fit anything")
			print(f"\t              image ratio:\t{round(image_ratio_decimal, 2)}")
			print(f"\t         projection ratio:\t{round(projection_ratio_decimal, 2)}")
			factor = image_size[self.height_index] / projection_ratio_fit[self.height_index]
			image_display_width = int(image_size[self.width_index] / factor)
			image_display_height = int(image_size[self.height_index] / factor)

		print(f"\t        conversion factor:\t{factor}")
		print(f"\t             display size:\t{self.canvas_size[0]}\t{self.canvas_size[1]}")
		print(f"\tprojection_ratio_fit size:\t{projection_ratio_fit[0]}\t{projection_ratio_fit[1]}")
		return (image_display_width, image_display_height)

def main():
	display_math = DisplayMath()

	projection_ratios = ["ClassicTV (4:3)", "HDTV (16:9)", "Anamorphic Widescreen (239:100)"]

	for j in range(3):
		projection_ratio = projection_ratios[j]
		print(f"Projection Ratio: {projection_ratio}\n")

		image_sizes = [[4556, 2244], ## manufactured widescreen
							[3281, 2445], ## still camera
							[1920, 1080], ## HDTV
							[3280, 1845]] ## HDTV

		for i in range(4):
			image_size = image_sizes[i]
			print(f"Image #{i} size: {image_size}")
			width, height = display_math.get_image_projection(image_size, projection_ratio)
			print(f"\t         image_projection:\t{width}\t{height}")
			print()

			
if __name__ == "__main__":
	main()