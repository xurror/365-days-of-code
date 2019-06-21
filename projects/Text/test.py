from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

app = QApplication(sys.argv)

PushButton = QPushButton("Hello World")
PushButton.show()

sys.exit(app.exec_())