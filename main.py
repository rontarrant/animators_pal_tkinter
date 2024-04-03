'''
main.__init__()
	preview monkey
		file treeview
			()build_new_image_list()
				**APImageCollection**
			()ThumbnailFrame.preview_thumbnail()
		thumbnail canvas
			()ThumbnailFrame.preview_thumbnail()
				**APImageCollection**

	video monkey
		**APSettings**
		video settings
		video canvas
			()show_next_frame()
		video controls
			()VideoCanvas.show_next_frame()
				**APImageCollection**

	menubar
		file menubar
			add images
				()TreeFrame.build_new_image_list()
				()VideoCanvas.show_next_frame()
				**APImageCollection**
'''
