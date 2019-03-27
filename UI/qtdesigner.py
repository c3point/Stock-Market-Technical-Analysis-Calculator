# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table_Resize.ui'
#
# Created: Tue Mar 26 13:22:54 2019
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from scraper import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 569)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.widget_3 = QtGui.QWidget(self.splitter_3)
        self.widget_3.setStyleSheet(_fromUtf8("background:white;"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem = QtGui.QSpacerItem(168, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_9 = QtGui.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_7.addWidget(self.label_9)
        self.label_10 = QtGui.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_7.addWidget(self.label_10)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        spacerItem1 = QtGui.QSpacerItem(158, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.widget_4 = QtGui.QWidget(self.splitter_3)
        self.widget_4.setStyleSheet(_fromUtf8("background:white;"))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem2 = QtGui.QSpacerItem(198, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.label_12 = QtGui.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_9.addWidget(self.label_12)
        spacerItem3 = QtGui.QSpacerItem(218, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget_2 = QtGui.QWidget(self.splitter)
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_13 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_10.addWidget(self.label_13)
        spacerItem4 = QtGui.QSpacerItem(338, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.tableWidget_3 = QtGui.QTableWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy)
        self.tableWidget_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableWidget_3.setFrameShadow(QtGui.QFrame.Sunken)
        #self.tableWidget_3.setSizeAdjustPolicy(QtGui.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_3.setRowCount(4)
        self.tableWidget_3.setColumnCount(7)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        
 
 
        self.tableWidget_3.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        

        

        self.tableWidget_3.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()

        
        
        
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(111)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(35)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.widget = QtGui.QWidget(self.splitter_2)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_15 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout.addWidget(self.label_15)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.tableWidget_4 = QtGui.QTableWidget(self.splitter_2)
        self.tableWidget_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.tableWidget_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.tableWidget_4.setAlternatingRowColors(True)
        self.tableWidget_4.setRowCount(4)
        self.tableWidget_4.setColumnCount(7)
        self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_4.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        

 
        self.tableWidget_4.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        
        

        
      
        self.tableWidget_4.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setItem(3, 1, item)
        


        
        self.tableWidget_4.horizontalHeader().setVisible(False)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(111)
        self.tableWidget_4.horizontalHeader().setHighlightSections(True)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(35)
        

        self.layoutWidget = QtGui.QWidget(self.splitter_3)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_8.addWidget(self.label_11)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_8.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_9.setText(_translate("MainWindow", "Stock Market", None))
        self.label_10.setText(_translate("MainWindow", "Technical Analysis Calculator", None))
        self.label_12.setText(_translate("MainWindow", "US Stock Exchanges", None))
        self.label_13.setText(_translate("MainWindow", "New York Stock Exchange:", None))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        
        #new
        data = data_list()
        #new


        
        item = self.tableWidget_3.item(0, 0)
        item.setText(_translate("MainWindow", "Company:", None))
        item = self.tableWidget_3.item(0, 1)
        item.setText(_translate("MainWindow", "Ticker Symbol", None))
        item = self.tableWidget_3.item(0, 2)
        item.setText(_translate("MainWindow", "Market Cap", None))
        item = self.tableWidget_3.item(0, 3)
        item.setText(_translate("MainWindow", "P/E Ratio", None))
        item = self.tableWidget_3.item(0, 4)
        item.setText(_translate("MainWindow", "Div Yield", None))
        item = self.tableWidget_3.item(0, 5)
        item.setText(_translate("MainWindow", "52-Week High", None))
        item = self.tableWidget_3.item(0, 6)
        item.setText(_translate("MainWindow", "52-Week Low", None))
        item = self.tableWidget_3.item(1, 0)
        item.setText(_translate("MainWindow", "Boeing", None))
        item = self.tableWidget_3.item(1, 1)
        item.setText(_translate("MainWindow", "BA", None))
        item = self.tableWidget_3.item(2, 0)
        item.setText(_translate("MainWindow", "JP Morgan Chase", None))
        item = self.tableWidget_3.item(2, 1)
        item.setText(_translate("MainWindow", "JPM", None))
        item = self.tableWidget_3.item(3, 0)
        item.setText(_translate("MainWindow", "Verizon", None))
        item = self.tableWidget_3.item(3, 1)
        item.setText(_translate("MainWindow", "VZ", None))
        
        #start
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[0][0])
        self.tableWidget_3.setItem(1, 2, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[0][1])
        self.tableWidget_3.setItem(1, 3, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[0][2])
        self.tableWidget_3.setItem(1, 4, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[0][3])
        self.tableWidget_3.setItem(1, 5, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[0][4])
        self.tableWidget_3.setItem(1, 6, item)
        
        
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[1][0])
        self.tableWidget_3.setItem(2, 2, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[1][1])
        self.tableWidget_3.setItem(2, 3, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[1][2])
        self.tableWidget_3.setItem(2, 4, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[1][3])
        self.tableWidget_3.setItem(2, 5, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[1][4])
        self.tableWidget_3.setItem(2, 6, item)
        
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[2][0])
        self.tableWidget_3.setItem(3, 2, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[2][1])
        self.tableWidget_3.setItem(3, 3, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[2][2])
        self.tableWidget_3.setItem(3, 4, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[2][3])
        self.tableWidget_3.setItem(3, 5, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[2][4])
        self.tableWidget_3.setItem(3, 6, item)
        #end
        
        
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.label_15.setText(_translate("MainWindow", "Nasdaq Stock Exchange:", None))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        item = self.tableWidget_4.item(0, 0)
        item.setText(_translate("MainWindow", "Company:", None))
        item = self.tableWidget_4.item(0, 1)
        item.setText(_translate("MainWindow", "Ticker Symbol", None))
        item = self.tableWidget_4.item(0, 2)
        item.setText(_translate("MainWindow", "Market Cap", None))
        item = self.tableWidget_4.item(0, 3)
        item.setText(_translate("MainWindow", "P/E Ratio", None))
        item = self.tableWidget_4.item(0, 4)
        item.setText(_translate("MainWindow", "Div Yield", None))
        item = self.tableWidget_4.item(0, 5)
        item.setText(_translate("MainWindow", "52-Week High", None))
        item = self.tableWidget_4.item(0, 6)
        item.setText(_translate("MainWindow", "52-Week Low", None))
        item = self.tableWidget_4.item(1, 0)
        item.setText(_translate("MainWindow", "Apple", None))
        item = self.tableWidget_4.item(1, 1)
        item.setText(_translate("MainWindow", "AAPL", None))
        item = self.tableWidget_4.item(2, 0)
        item.setText(_translate("MainWindow", "Facebook", None))
        item = self.tableWidget_4.item(2, 1)
        item.setText(_translate("MainWindow", "FB", None))
        item = self.tableWidget_4.item(3, 0)
        item.setText(_translate("MainWindow", "Microsoft", None))
        item = self.tableWidget_4.item(3, 1)
        item.setText(_translate("MainWindow", "MSFT", None))
        
        #start
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[3][0])
        self.tableWidget_4.setItem(1, 2, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[3][1])
        self.tableWidget_4.setItem(1, 3, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[3][2])
        self.tableWidget_4.setItem(1, 4, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[3][3])
        self.tableWidget_4.setItem(1, 5, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[3][4])
        self.tableWidget_4.setItem(1, 6, item)
        
        
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[4][0])
        self.tableWidget_4.setItem(2, 2, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[4][1])
        self.tableWidget_4.setItem(2, 3, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[4][2])
        self.tableWidget_4.setItem(2, 4, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[4][3])
        self.tableWidget_4.setItem(2, 5, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[4][4])
        self.tableWidget_4.setItem(2, 6, item)
        
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[5][0])
        self.tableWidget_4.setItem(3, 2, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[5][1])
        self.tableWidget_4.setItem(3, 3, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[5][2])
        self.tableWidget_4.setItem(3, 4, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[5][3])
        self.tableWidget_4.setItem(3, 5, item)
        
        item = QtGui.QTableWidgetItem()
        item.setText(data[5][4])
        self.tableWidget_4.setItem(3, 6, item)
        #end

        
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        self.label_11.setText(_translate("MainWindow", "Stock Ticker Symbol:", None))
        self.pushButton_2.setText(_translate("MainWindow", "Submit", None))
        
        #new
        self.tableWidget_3.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tableWidget_4.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        #new
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

