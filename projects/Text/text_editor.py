import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt

class Main(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self,parent)

        self.initUI()

    def initUI(self):

        #x and y coordinates on the screen, width, height
        self.setGeometry(100,100,1030,800)

        self.setWindowTitle("Writer")

    def main():

        app = QtWidgets.QApplication(sys.argv)

        main = Main()
        main.show()

        sys.exit(app.exec_())

    if __name__ == "__main__":
        main()
