'''
main.__init__()
	preview_monkey_frame
		file_treeview
			()build_new_image_list()
				**APImageCollection**
			()ThumbnailFrame.preview_thumbnail()
		thumbnail_canvas
			()preview_thumbnail()
				**APImageCollection**

	video_monkey_frame
		**APSettings**
		video_settings
		video_canvas
			()show_next_frame()
		video_controls
			()VideoCanvas.show_next_frame()
				**APImageCollection**

	menubar
		file menubar
			add images
				()TreeFrame.build_new_image_list()
				()VideoCanvas.show_next_frame()
				**APImageCollection**
'''
