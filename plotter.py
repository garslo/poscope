#  plotter.py
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



import PyQt4.Qt as Qt
import PyQt4.Qwt5 as Qwt

class Plotter(Qwt.QwtPlot):
    def __init__(self):
        Qwt.QwtPlot.__init__(self)

        self.curve = Qwt.QwtPlotCurve()
        self.curve.attach(self)
        self.xs = None
        self.setAxisScale(self.xBottom, 0, 1000)
        self.setAxisScale(self.yLeft, -5, 5)
        self.setupGrid()

    def setupGrid(self):
        self.setCanvasBackground(Qt.QColor('White'))
        self.grid = Qwt.QwtPlotGrid()
        g_color = Qt.QColor('Green')
        g_color.setAlpha(100)
        self.grid.setMajPen(Qt.QPen(g_color, 0.5, Qt.Qt.DotLine))

        self.grid.attach(self)
        self.grid.show()

    def replotWith(self, ys, xs=None):
        if xs is not None:
            self.xs = xs
        self.curve.setData(self.xs, ys)
        self.replot()
