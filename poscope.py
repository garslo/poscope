#!/usr/bin/env python

#  poscope.py
#
#  Copyright 2013 Gary Slopsema
#
#  This file is part of poscope.
#
#  poscope is free software: you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  poscope is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with poscope. If not, see <http://www.gnu.org/licenses/>.


import sys
from PyQt4 import QtGui, QtCore
import numpy as np

from plotter import Plotter
from ui_mainwindow import Ui_MainWindow
from datasource import NI6009

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.rerun_btn.clicked.connect(self.rerun)

        self.source = NI6009()
        self.timer = QtCore.QTimer()
        self.redraw_interval = 50 # (ms)
        self.timer.timeout.connect(self.replot)

    def replot(self):
        self.ui.plotter.replotWith(xs=np.arange(0,1000),
                                   ys=self.source.data())
        self.timer.start()

    def rerun(self):
        self.timer.stop()
        self.source.reads_per_run = int(self.ui.num_reads.text())
        self.source.sample_rate = int(self.ui.num_samples.text())
        self.timer.start()

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec_()

if __name__ == '__main__':
    main()
