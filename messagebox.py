import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 Messagebox'
        self.left = 100
        self.top = 100
        self.width = 320
        self.height = 200
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # QMessageBox.Cancel	QMessageBox.Ok	QMessageBox.Help
        # QMessageBox.Open	QMessageBox.Save	QMessageBox.SaveAll
        # QMessageBox.Discard	QMessageBox.Close	QMessageBox.Apply
        # QMessageBox.Reset	QMessageBox.Yes	QMessageBox.YesToAll
        # QMessageBox.No	QMessageBox.NoToAll	QMessageBox.NoButton
        # QMessageBox.RestoreDefaults	QMessageBox.Abort	QMessageBox.Retry
        # QMessageBox.Ignore
 
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
        print(buttonReply)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
        if buttonReply == QMessageBox.No:
            print('No clicked.')
        if buttonReply == QMessageBox.Cancel:
            print('Cancel clicked.')
 
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())