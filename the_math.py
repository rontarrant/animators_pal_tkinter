## The Math
if projection == "ClassicTV":
	projection_ratio = "4:3"
	displacement_direction = AP_HORIZONTAL
	## these are drawn from ap_screen_resolutions.py
	projection_displacment = 480
	projection_width = 2880
	projection_height = 2160

if screen_resolution == "4k":
	screen_width = 3840
	screen_height = 2160

## assign values to Pillar Displacement & Letterbox Displacement
if displacement_direction == AP_HORIZONTAL:
	pillar_displacement = projection_displacment
	letterbox_displacement = 0
elif displacement_direction == AP_VERTICAL:
	pillar_displacement = 0
	letterbox_displacement = projection_displacment

## 