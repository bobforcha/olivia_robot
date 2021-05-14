import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width,height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.plot([0, 1, 2, 3, 4], [0, 10, 3, 40, 17])

        # create main layout placeholder widget
        central_widget = QtWidgets.QWidget()
        # create placeholder widget for input section
        input_widget = QtWidgets.QWidget()
        # create placeholder widget for plot section
        plot_widget = QtWidgets.QWidget()

        # create main horizontal layout
        main_layout = QtWidgets.QHBoxLayout()
        # create vertical layout for inputs
        input_layout = QtWidgets.QVBoxLayout()

        # add line edit and button to input layout
        input_layout.addWidget(QtWidgets.QLineEdit())
        input_layout.addWidget(QtWidgets.QPushButton("Update Max"))

        # set input_widget layout
        input_widget.setLayout(input_layout)

        # set main_layout
        main_layout.addWidget(input_widget)
        main_layout.addWidget(self.canvas)

        # set central_widget layout
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

        self.show()

app = QtWidgets.QApplication(sys.argv)
win = MainWindow()
app.exec_()

