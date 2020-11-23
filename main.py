import sys
from random import randrange

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from Yellow import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pt = False
        self.pushButton.clicked.connect(self.paint)
        self.pushButton.setStyleSheet('QPushButton {background-color: #e32636; color: white; font-size: 17px;}')

    def run(self, qp):
        qp.setBrush(QColor('#ffcc00'))
        d = randrange(20, 400)
        x = randrange(0, 800 - d)
        y = randrange(0, 600 - d)
        qp.drawEllipse(x, y, d, d)

    def paint(self):
        self.pt = True
        self.repaint()

    def paintEvent(self, event):
        if self.pt:
            qp = QPainter()
            qp.begin(self)
            self.run(qp)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())