from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.widget import Widget



class VideoWindow(App):
	def build(self):

		video = Video(source='images/lisa_turnaround_via_py.mp4')
		video.state = 'play'
		video.options = {'eos': 'loop'}


		video.allow_stretch = True
		return video




if __name__ == "__main__":
	window = VideoWindow()
	window.run()
