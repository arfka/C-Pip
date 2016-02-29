import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class dimension:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def center(app):
    screen_resolution = app.desktop().screenGeometry()
    d = dimension ((int(screen_resolution.width()/3)), (int(screen_resolution.height()/3))) 
    return d 

def inf_Layout(form, i):
    b = QPushButton("Button" + str(i))
    l = QLabel ("Label" + str(i))
    form.addRow(b,l)
    return form
def infinite_form(vbox, i):
    form = QFormLayout()
    for s in range(i):
        b = QPushButton("Button " + str(s))
        l = QLabel ("Label " + str(s))
        form.addRow(b,l)
    vbox.addLayout(form)
    vbox.addStretch()
    return vbox

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win2 = QWidget()
    mygroupbox = QGroupBox('groupbox')
    vbox1 = QVBoxLayout()
    a = QLabel ("This is My Program")
    vbox1.addWidget(a)
    vbox1.addStretch()
    win2.setLayout(vbox1)
    form=QFormLayout()
    vbox = QVBoxLayout()
    hbox = QHBoxLayout()
    b1=QPushButton("Button1")
    l1=QLabel("Hello")
    hbox.addWidget(b1)
    hbox.addWidget(l1)
    vbox.addLayout(hbox)
    vbox.addStretch()
    vbox = infinite_form(vbox,28)
    mygroupbox.setLayout(vbox)
    scroll = QScrollArea()
    scroll.setWidget(mygroupbox)
    scroll.setWidgetResizable(True)
    scroll.setFixedHeight(400)
    layout = QVBoxLayout(win)
    layout.addWidget(win2)
    layout.addWidget(scroll)
    win.setWindowTitle("PyQt")
    cen = center(app)
    win.setGeometry(int(cen.width), int(cen.height),300,200)
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
 window()
