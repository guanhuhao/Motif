import UI.windows as windows
from control_model.assignment import Manager
import sys
from PyQt5.QtWidgets import QApplication,QDialog,QTreeWidgetItem
import qdarkstyle
import asyncio
from queue import Queue

class Windows(QDialog):
    def __init__(self,parent=None):
        super(QDialog, self).__init__(parent)
        self.initUi()
        self.manager = Manager(is_test=1)
        # asyncio.run(self.main())
        # self.RunBotton.icon

    def initUi(self):
        self.ui = windows.Ui_Form()
        self.ui.setupUi(self)

    async def main(self):
        # CPU = asyncio.create_task(self.manager.run_CPU())
        # GPU = asyncio.create_task(self.manager.run_GPU())
        UI = asyncio.create_task(self.UI())

        # await CPU
        # await GPU
        await UI

    def Run(self):
        asyncio.run(self.main())

    async def UI(self):
        r = open("./pipe.txt", "r")
        while (True):
            print(self.manager.info_que.qsize())
            contain = await self.manager.info_que.get()
            # q = Queue()
            # q.
            code = {
                '0000': self.start_CPU_task
            }
            print(contain)
            method = code.get(contain[1])
            method(contain)

    def start_CPU_task(self,contain):
        print(contain[2],"Runing")
        item = QTreeWidgetItem(self.ui.CPUTaskList)
        item.setText(0, contain[2])
        item.setText(1, 'Runing')


myapp = QApplication(sys.argv)
myapp.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
myDlg = Windows()
myDlg.exec()