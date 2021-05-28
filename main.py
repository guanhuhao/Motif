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
        # loop = asyncio.get_event_loop()
        # loop.run_forever()
        # asyncio.run(self.main())
        # self.RunBotton.icon

    def initUi(self):
        self.ui = windows.Ui_Form()
        self.ui.setupUi(self)

    async def main(self):
        # CPU = asyncio.create_task(self.manager.run_CPU())
        # GPU = asyncio.create_task(self.manager.run_GPU())
        UI = asyncio.create_task(self.UI())
        # asyncio.run(UI)
        # await CPU
        # await GPU
        # await UI
        await asyncio.gather(UI)

    def Run(self):
        loop = asyncio.get_event_loop()
        # loop.run_until_complete(asyncio.wait(self.UI))

    async def UI(self):
        print(123)
        r = open("./pipe.txt", "r")
        while (True):
            while(self.manager.info_que.qsize() == 0) :
                print(self.manager.info_que.qsize())
                await asyncio.sleep(1)
            contain = self.manager.info_que.get()
            code = {
                '0000': self.start_CPU_task
            }
            print(contain)
            self.start_CPU_task(contain)
            # method = code.get(contain[1])
            # method(contain)

    def start_CPU_task(self,contain):
        print(contain[2],"Runing")
        item = QTreeWidgetItem(self.ui.CPUTaskList)
        item.setText(0, contain[2])
        item.setText(1, 'Runing')


myapp = QApplication(sys.argv)
myapp.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
myDlg = Windows()
# myDlg.show()
loop = myDlg.UI()
asyncio.set_event_loop(loop)
myDlg.show()

loop.run_forever()