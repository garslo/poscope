# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Dec 06 16:55:06 2011
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

from plotter import Plotter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 573)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plotter = Plotter()
        self.plotter.setObjectName("plotter")
        self.verticalLayout_2.addWidget(self.plotter)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtGui.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.num_reads = QtGui.QLineEdit(self.splitter)
        self.num_reads.setObjectName("num_reads")
        self.num_reads.setText('1000')
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_3 = QtGui.QLabel(self.splitter_2)
        self.label_3.setObjectName("label_3")
        self.trigger = QtGui.QLineEdit(self.splitter_2)
        self.trigger.setObjectName("trigger")
        self.verticalLayout.addWidget(self.splitter_2)
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_2 = QtGui.QLabel(self.splitter_3)
        self.label_2.setObjectName("label_2")
        self.range = QtGui.QLineEdit(self.splitter_3)
        self.range.setObjectName("range")
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_4 = QtGui.QSplitter(self.centralwidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_4 = QtGui.QLabel(self.splitter_4)
        self.label_4.setObjectName("label_4")
        self.num_samples = QtGui.QLineEdit(self.splitter_4)
        self.num_samples.setObjectName("num_samples")
        self.num_samples.setText('10000')
        self.verticalLayout.addWidget(self.splitter_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.splitter_5 = QtGui.QSplitter(self.centralwidget)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.rerun_btn = QtGui.QPushButton(self.splitter_5)
        self.rerun_btn.setObjectName("rerun_btn")
        self.close_btn = QtGui.QPushButton(self.splitter_5)
        self.close_btn.setObjectName("close_btn")
        self.verticalLayout_2.addWidget(self.splitter_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Num. Reads", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Trigger", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Range", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Num. Samples", None, QtGui.QApplication.UnicodeUTF8))
        self.rerun_btn.setText(QtGui.QApplication.translate("MainWindow", "Rerun", None, QtGui.QApplication.UnicodeUTF8))
        self.close_btn.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import Qwt5
