'''
Spits out an error and several warnings, but still works.

[ERROR  ] [Image       ] Error loading <D:\Documents\Programming\PythonCode\tkinter\animators_pal\research\../image_sequence/lisa_turnaround.mp4>
[INFO   ] [GL          ] NPOT texture support is available

(python.exe:500): GStreamer-WARNING **: 07:45:59.838: Failed to load plugin 'C:\Users\ron\AppData\Local\Programs\Python\Python312\share\gstreamer\bin\gioopenssl.dll': 'C:\Users\ron\AppData\Local\Programs\Python\Python312\share\gstreamer\bin\gioopenssl.dll': The specified module could not be found.

(python.exe:500): GStreamer-WARNING **: 07:46:00.300: Failed to load plugin 'C:\Users\ron\AppData\Local\Programs\Python\Python312\share\gstreamer\bin\gstrtmp.dll': 'C:\Users\ron\AppData\Local\Programs\Python\Python312\share\gstreamer\bin\gstrtmp.dll': The specified module could not be found.

(python.exe:500): GStreamer-WARNING **: 07:46:00.984: Failed to load plugin 'C:\Users\ron\AppData\Local\Programs\Python\Python312\share\gstreamer\bin\librtmp-1.dll': 'C:\Users\ron\AppData\Local\Programs\Python\Python312\share\gstreamer\bin\librtmp-1.dll': The specified module could not be found.
[INFO   ] [Base        ] Leaving application in progress...
'''
import kivy
kivy.require('1.2.0')

from sys import argv
from os.path import dirname, join
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer

# check what formats are supported for your targeted devices
# for example try h264 video and acc audo for android using an mp4
# container


class VideoPlayerApp(App):

    def build(self):
        if len(argv) > 1:
            filename = argv[1]
        else:
            curdir = dirname(__file__)
            filename = join(curdir, '../image_sequence/lisa_turnaround.mp4')
        return VideoPlayer(source=filename, state='play')


if __name__ == '__main__':
    VideoPlayerApp().run()
