import sys
import time
import threading
from PySide6.QtCore import QObject, QEvent, QTimer, QCoreApplication, Qt
from PySide6.QtWidgets import *

class IdleRunner(QObject):
	def customEvent(self, e):
		QTimer.singleShot(int(e.delay * 1000), e.func)

_idle_runner = IdleRunner()
def run_on_idle(func, *args, delay = 0, **kwargs):
	e = QEvent(QEvent.User)
	e.delay, e.func = delay, lambda: func(*args, **kwargs)
	QCoreApplication.postEvent(_idle_runner, e)
	
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__(windowTitle = sys.argv[0])
		self.resize(400, 300)
		self.setAttribute(Qt.WA_DeleteOnClose, True)

		self.label = label = QLabel('aaa', alignment = Qt.AlignCenter)
		self.setCentralWidget(label)

		def thread_entry():
			time.sleep(1)
			run_on_idle(lambda: self.label.setText('bbb'))
			run_on_idle(self.close, delay = 1)
			
		self.thread = thread = threading.Thread(target = thread_entry)
		thread.start()
		
	def close(self):
		self.thread.join()
		super().close()

app = QApplication()
main_window = MainWindow()
main_window.show()
app.exec_()
