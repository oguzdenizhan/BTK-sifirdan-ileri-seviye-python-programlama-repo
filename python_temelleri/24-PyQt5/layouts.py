import sys
import typing

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtGui import QPalette,QColor


class Color(QWidget):
    def __init__(self,color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__() 
        self.setGeometry(100,100,500,500)  
#1 horizonal and vertical
        # layout = QtWidgets.QVBoxLayout() 
        # layout = QtWidgets.QHBoxLayout() 

        # layout.addWidget(Color("red"))
        # layout.addWidget(Color("blue"))
        # layout.addWidget(Color("green"))
        # layout.addWidget(Color("yellow"))

        # widget= QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)

#2 horizonal and vertical using them together

        hlayout1 = QtWidgets.QHBoxLayout()

        hlayout1.addWidget(Color("red"))
        hlayout1.addWidget(Color("blue"))
        hlayout1.addWidget(Color("green"))
        # hlayout1.setContentsMargins(20,30,0,30)
        hlayout1.setSpacing(50)

        hlayout2 = QtWidgets.QHBoxLayout()
        
        hlayout2.addWidget(Color("red"))
        hlayout2.addWidget(Color("blue"))
        hlayout2.setSpacing(20)


        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        widget= QWidget()
        widget.setLayout(vlayout)       
        self.setCentralWidget(widget)

#3 grid 
        # layout = QtWidgets.QGridLayout()

        # layout.addWidget(Color("red"),0,0)
        # layout.addWidget(Color("blue"),1,0)
        # layout.addWidget(Color("green"),0,2)
        # layout.addWidget(Color("yellow"),3,3)

        # widget =QWidget()
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)



def app():
    app =QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()


