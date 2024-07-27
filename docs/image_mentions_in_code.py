ap_image.py (75 hits)
  Line  20:     self._pillow_image = None
  Line  21:     self._image_4_display = None
  Line  22:     self._cv_image = None
  Line  38:     self.pillow_image = PIL.Image.open(os.path.join(self.path, self.file_name))
  Line  39:     self.cv_image = cv2.imread(os.path.join(self.path, self.file_name))
  Line  42:     shape = self.cv_image.shape
  Line  49:     self.image_4_display = self.build_image_4_display()
  Line  61:   def calculate_display_size(self, image_width, image_height):
  Line  64:       divisor = image_width / self.canvas_width ## always assume we're downsizing
  Line  65:       self.display_height = int(image_height / divisor)
  Line  68:       divisor = image_height / self.canvas_height
  Line  69:       self.display_width = int(image_width / divisor)
  Line  74:   def set_image_placement(self):
  Line  82:   def build_image_4_display(self):
  Line  84:     image_width, image_height = self.dimensions
  Line  88:     self.calculate_display_size(image_width, image_height)
  Line  89:     resized_original = self.pillow_image.resize((self.display_width, self.display_height))
  Line  92:     self.set_image_placement()
  Line  95:     composite_image = PIL.Image.new("RGB", (self.canvas_width, self.canvas_height), color = 'black')
  Line  96:     composite_image.paste(resized_original, (int(self.pillarboxing_width), int(self.letterboxing_height)))
  Line  97:     self.image_4_display = PIL.ImageTk.PhotoImage(composite_image)
  Line 100:   def pillow_image(self):
  Line 101:     return self._pillow_image
  Line 103:   @pillow_image.setter
  Line 104:   def pillow_image(self, value):
  Line 106:       self._pillow_image = value
  Line 109:   def image_4_display(self):
  Line 110:     return self._image_4_display
  Line 112:   @image_4_display.setter
  Line 113:   def image_4_display(self, value):
  Line 116:       self._image_4_display = value
  Line 119:   def cv_image(self):
  Line 120:     return self._cv_image
  Line 122:   @cv_image.setter
  Line 123:   def cv_image(self, value):
  Line 126:       self._cv_image = value

pvw_vw_thumbnail_canvas.py (44 hits)
  Line  47:   def calculate_thumbnail_size(self, image_width, image_height):
  Line  50:       divisor = image_width / self.canvas_width ## always assume we're downsizing
  Line  51:       self.thumb_height = int(image_height / divisor)
  Line  54:       divisor = image_height / self.canvas_height
  Line  55:       self.thumb_width = int(image_width / divisor)
  Line  60:   def set_image_placement(self):
  Line  70:   def preview_thumbnail(self, image_number):
  Line  74:     image = self.ap_image_collection.images[image_number]
  Line  78:     image_width, image_height = image.dimensions
  Line  81:     self.ratio_flag = image.ratio_flag
  Line  85:     self.calculate_thumbnail_size(image_width, image_height)
  Line  87:     self.set_image_placement()
  Line  90:     self.pillow_thumbnail_image = image.pillow_image.resize((self.thumb_width, self.thumb_height))
  Line  92:     self.thumbnail_image = PIL.ImageTk.PhotoImage(self.pillow_thumbnail_image)
  Line  95:     self.create_image(self.pillars, self.letters, anchor = 'nw', image = self.thumbnail_image)
  Line 100:   image_collection = APImageCollection()

vdo_vw_canvas.py (9 hits)
  Line 63:     self.create_image(0, 0, anchor = "nw", image = self.ap_image_collection.images[frame_num].image_4_display)
