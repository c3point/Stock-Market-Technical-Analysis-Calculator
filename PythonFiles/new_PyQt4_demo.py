# -*- coding: utf-8 -*-
"""
Author: Travis Campos
Date: 03/21/2019

Spyder Editor

Stock Market
"""
#%%
from stock_market import *


import sys
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import random



class Window(QtGui.QDialog):
    def __init__(self):
        super(Window, self).__init__()

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        #self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QtGui.QVBoxLayout()
        #layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        # random data

        
        data = [random.random() for i in range(10)]

        # create an axis
        #ax = self.figure.add_subplot(111)

        # discards the old graph
        ax1.clear()
        ax2.clear()

        # plot data
        #ax.plot(data, '*-')
        
        ax1.plot(df.index, df['Adj Close'],color = 'Green')
        ax1.plot(df.index, df['100ma'], color = 'Blue')
        ax1.plot(df.index, df['200ma'], color = 'Red')
        ax2.bar(df.index, df['Volume'])

        # refresh canvas
        self.canvas.draw()
        
        
if __name__ == '__main__':
    
    if not QtGui.QApplication.instance():
        app = QtGui.QApplication(sys.argv)
    else:
        app = QtGui.QApplication.instance() 
        
    window = Window()
    window.show()
    
    window.setGeometry(250,125,800,500)
    window.setWindowTitle("Stock Market Technical Analysis")
    window.setWindowIcon(QtGui.QIcon("..\Images\LogoFinal.png"))
    sys.exit(app.exec_())
        



#%%
    
from stock_market import *
    
import sys
import time

import numpy as np

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5

if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
    
from matplotlib.figure import Figure


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)


        self.setGeometry(250,125,800,500)
        self.setWindowTitle("Stock Market Technical Analysis")
        self.setWindowIcon(QtWidgets.QIcon("..\Images\LogoFinal.png"))
    
    
        #self.static_canvas_1 = FigureCanvas(Figure(figsize=(5, 3)))
        #layout.addWidget(self.static_canvas_1)
        
        #self.static_canvas_2 = FigureCanvas(Figure(figsize=(5, 3)))
        #layout.addWidget(self.static_canvas_2) 
        
        #self.plot()
        
        self.label = QtWidgets.QLabel()
        self.label.move(200,0)
        pixmap = QtWidgets.QPixmap('chart.png')
        self.label.setPixmap(pixmap)

        
        layout.addWidget(self.label)
        
        

    def plot(self):
        self.ax1 = self.static_canvas_1.figure.subplots()
        self.ax2 = self.static_canvas_2.figure.subplots()
        #self.ax2 = self.static_canvas.figure.subplots()
        #t = np.linspace(0, 10, 501)
        #self._static_ax.plot(t, np.sin(t), ".")

        self.ax1.plot(df.index, df['Adj Close'],color = 'Green')
        self.ax1.plot(df.index, df['100ma'], color = 'Blue')
        self.ax1.plot(df.index, df['200ma'], color = 'Red')
        self.ax2.bar(df.index, df['Volume'])




if __name__ == "__main__":
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    window = Window()
    window.show()
    app.exec_()
    
#%%