import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 image'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 240
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create widget
        label = QLabel(self)
        image = QFileDialog.getOpenFileName(None,'OpenFile','',"Image file(*.png)")
        imagePath = image[0]
        pixmap = QPixmap(imagePath)
        #pixmap = QPixmap('TFmini.png')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
 
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())