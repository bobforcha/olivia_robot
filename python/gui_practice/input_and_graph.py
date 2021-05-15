import sys
import random
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width,height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Input and Graph")

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.canvas.axes.plot([0, 1, 2, 3, 4], [0, 10, 3, 40, 17])
        toolbar = NavigationToolbar(self.canvas, self)

        # create main layout placeholder widget
        central_widget = QWidget()
        # create placeholder widget for input section
        input_widget = QWidget()
        # create placeholder widget for plot section
        plot_widget = QWidget()

        # create main horizontal layout
        main_layout = QHBoxLayout()
        # create form layout for inputs
        input_layout = QFormLayout()
        # create vertical layout for plot menu
        plot_layout = QVBoxLayout()

        # add line edit to input layout
        self.max_input = QLineEdit()
        self.max_input.setValidator(QIntValidator())
        self.max_input.setMaxLength(4)
        input_layout.addRow("Max Random Value", self.max_input)
        self.max_input.editingFinished.connect(self.update_rand_max)

        # set input_widget layout
        input_widget.setLayout(input_layout)

        # add menu and plot to plot widget
        plot_layout.addWidget(toolbar)
        plot_layout.addWidget(self.canvas)

        # set plot_widget layout
        plot_widget.setLayout(plot_layout)

        # set main_layout
        main_layout.addWidget(input_widget)
        main_layout.addWidget(plot_widget)

        # set central_widget layout
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)
        
        # plot random data with max controlled by user
        n_data = 50
        self.rand_max = 10
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0,self.rand_max) for i in range(n_data)]
        # Call function to live update plot
        self.update_plot()

        # show main window
        self.show()

        # set timer to refresh plot
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        self.ydata = self.ydata[1:] + [random.randint(0,self.rand_max)]
        self.canvas.axes.cla()
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        self.canvas.draw()

    def update_rand_max(self):
        self.rand_max = int(self.max_input.text())

app = QApplication(sys.argv)
win = MainWindow()
app.exec_()

