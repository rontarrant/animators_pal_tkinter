import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initializeUI()
	
	def initializeUI(self):
		self.setGeometry(100, 100, 400, 300)
		self.setWindowTitle("Hello, PySide World!")
		self.show()

def main():
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec())
		
if __name__ == "__main__":
	main()
