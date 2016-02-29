import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#dimension Class
class dimension:
    def __init__(self, width, height):
        self.width = width
        self.height = height


#Center of the screen
def center(app):
    screen_resolution = app.desktop().screenGeometry()
    d = dimension ((int(screen_resolution.width()/3)), (int(screen_resolution.height()/3))) 
    return d 

#Custom form 
def inf_Layout(i):
    win = QWidget()
    for s in range (i):
        b = QPushButton("Button" + str(s))
        l = QLabel ("Label" + str(s))
        form.addRow(b,l)
    return win

#Custom form 2
def lines(i):
    win = QWidget()
    for p in range(i):
        s=QPushButton("hello")
        l=QLabel("World" + str(p))    
        form.addRow(s,l)
    win.setLayout(form)
    return win

#Add a scroll to a widget.
def scroll(widget):
    scroll=QScrollArea()
    scroll.setWidget(widget)
    scroll.setWidgetResizable(True)
    scroll.setFixedHeight(200)
    return scroll

#Custom Widget
class Widget1(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        layout = QGridLayout(self)
        for j in range (0,86,2):
            s = str(j)
            latitudeLabel = QPushButton("Install")
            longitudeLabel = QLabel(s)
            vLine=QFrame()
            layout.addWidget(latitudeLabel, j, 1)
            layout.addWidget(longitudeLabel, j, 0)
            layout.addWidget(vLine, j+1, 0)
            layout.addWidget(vLine, j+1, 1)            

        
#Window initiation
def window():
    app = QApplication(sys.argv)
    main = QWidget()
    palette = QPalette()
    win = QWidget()
    win1 = Widget1()
    win1 = scroll(win1)
    sub_layout = QVBoxLayout(win)
    sub_layout.addWidget(win1)
    palette.setColor(QPalette.Background,Qt.black)
    cen = center(app)
    win.setGeometry(int(cen.width), int(cen.height),300,200)
    win.setPalette(palette)
    win.show()
    sys.exit(app.exec_())

#Main
if __name__ == '__main__':
 window()
