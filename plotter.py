#!/usr/bin/env python

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
