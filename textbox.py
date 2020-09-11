import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, \
    QAction, QLineEdit, QMessageBox, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PIL import ImageGrab
from turnToText import makeText

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'MMOCR'
        self.left = 10
        self.top = 10
        self.width = 700
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QPlainTextEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(660, 280)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 300)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        #textboxValue = self.textbox.text()
        img = ImageGrab.grabclipboard()

        try:
            text, image, gray = makeText(img)
        except:
            text = "ah, try again. i don't think you had a valid image in your clipboard."

        self.textbox.setPlainText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())