# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1092, 680)
        self.Tab = QtWidgets.QTabWidget(Form)
        self.Tab.setGeometry(QtCore.QRect(10, 20, 1071, 491))
        self.Tab.setObjectName("Tab")
        self.CPU = QtWidgets.QWidget()
        self.CPU.setObjectName("CPU")
        self.CanvasBox_2 = QtWidgets.QGroupBox(self.CPU)
        self.CanvasBox_2.setGeometry(QtCore.QRect(222, 10, 651, 451))
        self.CanvasBox_2.setObjectName("CanvasBox_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.CanvasBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 19, 631, 421))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.PartitionLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.PartitionLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PartitionLayout_2.setObjectName("PartitionLayout_2")
        self.CPUTaskList = QtWidgets.QTreeWidget(self.CPU)
        self.CPUTaskList.setEnabled(False)
        self.CPUTaskList.setGeometry(QtCore.QRect(10, 10, 201, 161))
        self.CPUTaskList.setObjectName("CPUTaskList")
        self.CPUTaskList.header().setDefaultSectionSize(100)
        self.RuningDetail = QtWidgets.QTreeWidget(self.CPU)
        self.RuningDetail.setEnabled(False)
        self.RuningDetail.setGeometry(QtCore.QRect(880, 10, 181, 451))
        self.RuningDetail.setObjectName("RuningDetail")
        item_0 = QtWidgets.QTreeWidgetItem(self.RuningDetail)
        item_0 = QtWidgets.QTreeWidgetItem(self.RuningDetail)
        item_0 = QtWidgets.QTreeWidgetItem(self.RuningDetail)
        item_0 = QtWidgets.QTreeWidgetItem(self.RuningDetail)
        self.RuningDetail.header().setDefaultSectionSize(100)
        self.GraphDetail = QtWidgets.QTreeWidget(self.CPU)
        self.GraphDetail.setEnabled(False)
        self.GraphDetail.setGeometry(QtCore.QRect(10, 180, 201, 281))
        self.GraphDetail.setIndentation(0)
        self.GraphDetail.setObjectName("GraphDetail")
        self.GraphDetail.header().setDefaultSectionSize(40)
        self.Tab.addTab(self.CPU, "")
        self.GPU = QtWidgets.QWidget()
        self.GPU.setObjectName("GPU")
        self.CanvasBox = QtWidgets.QGroupBox(self.GPU)
        self.CanvasBox.setGeometry(QtCore.QRect(222, 10, 651, 451))
        self.CanvasBox.setObjectName("CanvasBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.CanvasBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 19, 631, 421))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.PartitionLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.PartitionLayout.setContentsMargins(0, 0, 0, 0)
        self.PartitionLayout.setObjectName("PartitionLayout")
        self.SelectPartition = QtWidgets.QTreeWidget(self.GPU)
        self.SelectPartition.setEnabled(False)
        self.SelectPartition.setGeometry(QtCore.QRect(10, 10, 201, 151))
        self.SelectPartition.setObjectName("SelectPartition")
        item_0 = QtWidgets.QTreeWidgetItem(self.SelectPartition)
        item_0 = QtWidgets.QTreeWidgetItem(self.SelectPartition)
        item_0 = QtWidgets.QTreeWidgetItem(self.SelectPartition)
        item_0 = QtWidgets.QTreeWidgetItem(self.SelectPartition)
        self.SelectPartition.header().setDefaultSectionSize(100)
        self.SelectIterator = QtWidgets.QTreeWidget(self.GPU)
        self.SelectIterator.setEnabled(False)
        self.SelectIterator.setGeometry(QtCore.QRect(10, 180, 201, 281))
        self.SelectIterator.setIndentation(0)
        self.SelectIterator.setObjectName("SelectIterator")
        self.SelectIterator.header().setDefaultSectionSize(40)
        self.SelectPartition_2 = QtWidgets.QTreeWidget(self.GPU)
        self.SelectPartition_2.setEnabled(False)
        self.SelectPartition_2.setGeometry(QtCore.QRect(880, 20, 181, 441))
        self.SelectPartition_2.setObjectName("SelectPartition_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.SelectPartition_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.SelectPartition_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.SelectPartition_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.SelectPartition_2)
        self.SelectPartition_2.header().setDefaultSectionSize(100)
        self.Tab.addTab(self.GPU, "")
        self.LogMessageBox = QtWidgets.QGroupBox(Form)
        self.LogMessageBox.setGeometry(QtCore.QRect(10, 510, 1071, 161))
        self.LogMessageBox.setObjectName("LogMessageBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.LogMessageBox)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 1051, 131))
        self.textBrowser.setObjectName("textBrowser")
        self.Run = QtWidgets.QPushButton(Form)
        self.Run.setGeometry(QtCore.QRect(1004, 9, 75, 23))
        self.Run.setObjectName("Run")

        self.retranslateUi(Form)
        self.Tab.setCurrentIndex(0)
        self.SelectIterator.itemClicked['QTreeWidgetItem*','int'].connect(Form.close)
        self.SelectPartition.itemClicked['QTreeWidgetItem*','int'].connect(Form.close)
        self.Run.clicked.connect(Form.Run)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GPUGraphX Log Browser"))
        self.CanvasBox_2.setTitle(_translate("Form", "View"))
        self.CPUTaskList.headerItem().setText(0, _translate("Form", "Task Name"))
        self.CPUTaskList.headerItem().setText(1, _translate("Form", "Status"))
        self.RuningDetail.headerItem().setText(0, _translate("Form", "Select Partition"))
        __sortingEnabled = self.RuningDetail.isSortingEnabled()
        self.RuningDetail.setSortingEnabled(False)
        self.RuningDetail.topLevelItem(0).setText(0, _translate("Form", "Partition 0"))
        self.RuningDetail.topLevelItem(1).setText(0, _translate("Form", "Partition 1"))
        self.RuningDetail.topLevelItem(2).setText(0, _translate("Form", "Partition 2"))
        self.RuningDetail.topLevelItem(3).setText(0, _translate("Form", "Partition 3"))
        self.RuningDetail.setSortingEnabled(__sortingEnabled)
        self.GraphDetail.headerItem().setText(0, _translate("Form", "Iter"))
        self.GraphDetail.headerItem().setText(1, _translate("Form", "Ver"))
        self.GraphDetail.headerItem().setText(2, _translate("Form", "Edge"))
        self.GraphDetail.headerItem().setText(3, _translate("Form", "Com"))
        self.GraphDetail.headerItem().setText(4, _translate("Form", "Act"))
        self.Tab.setTabText(self.Tab.indexOf(self.CPU), _translate("Form", "CPU"))
        self.CanvasBox.setTitle(_translate("Form", "View"))
        self.SelectPartition.headerItem().setText(0, _translate("Form", "Select Partition"))
        __sortingEnabled = self.SelectPartition.isSortingEnabled()
        self.SelectPartition.setSortingEnabled(False)
        self.SelectPartition.topLevelItem(0).setText(0, _translate("Form", "Partition 0"))
        self.SelectPartition.topLevelItem(1).setText(0, _translate("Form", "Partition 1"))
        self.SelectPartition.topLevelItem(2).setText(0, _translate("Form", "Partition 2"))
        self.SelectPartition.topLevelItem(3).setText(0, _translate("Form", "Partition 3"))
        self.SelectPartition.setSortingEnabled(__sortingEnabled)
        self.SelectIterator.headerItem().setText(0, _translate("Form", "Iter"))
        self.SelectIterator.headerItem().setText(1, _translate("Form", "Ver"))
        self.SelectIterator.headerItem().setText(2, _translate("Form", "Edge"))
        self.SelectIterator.headerItem().setText(3, _translate("Form", "Com"))
        self.SelectIterator.headerItem().setText(4, _translate("Form", "Act"))
        self.SelectPartition_2.headerItem().setText(0, _translate("Form", "Select Partition"))
        __sortingEnabled = self.SelectPartition_2.isSortingEnabled()
        self.SelectPartition_2.setSortingEnabled(False)
        self.SelectPartition_2.topLevelItem(0).setText(0, _translate("Form", "Partition 0"))
        self.SelectPartition_2.topLevelItem(1).setText(0, _translate("Form", "Partition 1"))
        self.SelectPartition_2.topLevelItem(2).setText(0, _translate("Form", "Partition 2"))
        self.SelectPartition_2.topLevelItem(3).setText(0, _translate("Form", "Partition 3"))
        self.SelectPartition_2.setSortingEnabled(__sortingEnabled)
        self.Tab.setTabText(self.Tab.indexOf(self.GPU), _translate("Form", "GPU"))
        self.LogMessageBox.setTitle(_translate("Form", "Log Message"))
        self.Run.setText(_translate("Form", "Run"))
