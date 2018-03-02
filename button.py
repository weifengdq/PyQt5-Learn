import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,  QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):
     
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Button'
        self.left = 100
        self.top = 50
        self.width = 320
        self.height = 240
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100,90) 
        button.clicked.connect(self.on_click)
 
        self.statusBar().showMessage('Message in statusbar.')
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())