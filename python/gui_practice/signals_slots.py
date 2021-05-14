import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QDialog()
    b1 = QPushButton(win)
    b1.setText("Button 1")
    b1.move(50,20)
    b1.clicked.connect(b1_clicked)

    b2 = QPushButton(win)
    b2 .setText("Button 2")
    b2.move(50,80)
    b2.clicked.connect(b2_clicked)

    win.setGeometry(100,100,200,150)
    win.setWindowTitle("PyQt5")
    win.show()
    sys.exit(app.exec_())

def b1_clicked():
    print("Button 1 clicked!")

def b2_clicked():
    print("Button 2 clicked!")

if __name__ == '__main__':
    window()

