# -*- coding: utf-8 -*-
"""
Author: Travis Campos
Date: 03/21/2019

Spyder Editor

Stock Market
"""
#%%
#from stock_market import *

import sys
from PyQt4 import QtGui, QtCore

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import random



class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

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
        ax = self.figure.add_subplot(111)

        # discards the old graph
        ax.clear()

        # plot data
        ax.plot(data, '*-')

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
    window.setWindowIcon(QtGui.QIcon("C:\Users\Travis Campos\Documents\PIC10C-Final\LogoFinal.png"))
    sys.exit(app.exec_())
        



#%%