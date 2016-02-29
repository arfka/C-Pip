import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from data import *

#dimension Class
class dimension:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def color (r,g,b):
    palette = QPalette()
    palette.setColor(QPalette.Background, QColor.fromRgb(r,g,b))
    return palette


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
    return scroll


#Custom Widget
class Widget1(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        layout = QGridLayout(self)
        pack = data_extractor ("installed.txt")
        j = 0
        for p in pack:
            s = str(p.n)+ " : " + str(p.d)
            latitude = QPushButton("Install")
            latitude.setFixedWidth(110)
            longitude = QLabel(s)
            vline = QFrame()
            layout.addWidget(latitude, j, 1)
            layout.addWidget(longitude, j, 0)
            layout.addWidget(vline, j+1, 0)
            layout.addWidget(vline, j+1, 1)
            j += 2

        
#Window initiation
def window():
    app = QApplication(sys.argv)
    main = QWidget()
    # Widget1
    win = QWidget()
    
    sub_win = Widget1()
    sub_win = scroll(sub_win)
    sub_win.setPalette(color(190, 190, 180))
    sub_layout = QVBoxLayout(win)
    sub_layout.addWidget(sub_win)
    cen = center(app)
    win.setGeometry(int(cen.width), int(cen.height),600,400)

    win.show()
    sys.exit(app.exec_())

#Main
if __name__ == '__main__':
 window()
