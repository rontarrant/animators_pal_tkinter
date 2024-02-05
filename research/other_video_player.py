from kivy.app import App
from kivy.uix.video import Video

from kivy.lang import Builder

kv = """
BoxLayout:
	orientation: 'vertical'
	Player:
		id:player
	BoxLayout:
		size_hint_y: .1
		Button: 
			text: 'play'
			on_release: player.state = 'play' 
		
	
"""

video_list = ['IMG_1853.jpg',
			  'Hand Washing - 34091.mp4']

class Player(Video):
	def __init__(self, **kwargs):
		self.v = 0
		super().__init__(source=video_list[0], state='stop', **kwargs)

	def on_eos(self, *args):
		print(f'on_eos: {self.eos} loaded: {self.loaded}, state: {self.state}')
		if self.eos:
			self.v += 1
			if self.v == len(video_list):
				print('End of playlist')
				self.v = 0
				return
		self.source = video_list[self.v]
		self.state = 'play'  # must set state to play for video to be loaded

	def on_loaded(self, *args):
		# print('*' * 80)
		print(f'loaded: {self.loaded}')


class VideoPlayerApp(App):
	def build(self):
		return Builder.load_string(kv)


if __name__ == '__main__':
	VideoPlayerApp().run()
