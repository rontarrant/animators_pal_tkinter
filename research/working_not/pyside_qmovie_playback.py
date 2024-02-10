import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaMetaData
from PySide6.QtMultimediaWidgets import QVideoWidget


class MainWin(QMainWindow):
	def __init__(self, file_path):
		super(MainWin, self).__init__()
		self.cent_wid = QVideoWidget()
		self.setCentralWidget(self.cent_wid)
		self.player = QMediaPlayer()
		self.player.setVideoOutput(self.cent_wid)
		
		metadata = self.player.QMediaMetaData()
		metadata_keys = metadata.keys()
		#current_speed = metadata_keys[]
		print(metadata.keys()) #QMediaMetaData.VideoFrameRate
		#print("current_speed:", current_speed)
		## calculate new playback speed
		playback_ratio = 24 / 15
		speed = 1 / playback_ratio
		self.player.setPlaybackRate(speed)
		self.file_path = file_path

	def showEvent(self, a0) -> None:
		super(MainWin, self).showEvent(a0)
		self.player.setSource(QUrl.fromLocalFile(self.file_path))
		self.player.play()

if __name__ == '__main__':
	app = QApplication([])
	##frm = MainWin(sys.argv[1])
	frm = MainWin("images/RemoteDog.mp4")
	frm.show()
	app.exec()
	