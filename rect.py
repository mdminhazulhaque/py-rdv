import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CustomWindow(QMainWindow):
    def paintEvent(self, event=None):
        painter = QPainter(self)

        painter.setOpacity(0.1)
        painter.setBrush(Qt.white)
        painter.setPen(QPen(Qt.white))   
        painter.drawRect(self.rect())

app = QApplication(sys.argv)
window = CustomWindow()

window.setAttribute(Qt.WA_NoSystemBackground, True)
window.setAttribute(Qt.WA_TranslucentBackground, True)

pushButton = QPushButton(window)
pushButton.setText("Start Sharing")
pushButton.clicked.connect(app.quit)

window.setGeometry(QRect(100, 100, 400, 300))
window.show()

x, y, w, h = window.geometry().x(), window.geometry().y(), window.geometry().width(), window.geometry().height()
app.exec_()
