
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from Pyqt5.QtGui import QIcon


class ExWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300,300,400,300)
        self.setWindowTitle("Main Window")
        self.show()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "QyQt5 simple window - pythonspot.com"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ExWindow()
    ex = App()
    sys.exit(app.exec_())

