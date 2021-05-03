import UI.windows as UI
from control_model.assignment import Manager
import sys
from PyQt5.QtWidgets import QApplication,QDialog
import qdarkstyle

class Windows(QDialog):
    def __init__(self,parent=None):
        super(QDialog, self).__init__(parent)
        self.initUi()


        # self.RunBotton.icon

    def initUi(self):
        self.ui = UI.Ui_Form()
        self.ui.setupUi(self)

myapp = QApplication(sys.argv)
myapp.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
myDlg = Windows()
myDlg.exec()