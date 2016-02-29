import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from data import *
from Widgets import *
#Window initiation
def window():
    app = QApplication(sys.argv)
    win = install_widget()
    main = QWidget()
    cen = center(app)
    win.setGeometry(int(cen.width), int(cen.height),600,400)
    win.show()
    sys.exit(app.exec_())

#Main
if __name__ == '__main__':
 window()
