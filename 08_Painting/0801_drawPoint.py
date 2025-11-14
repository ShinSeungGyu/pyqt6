# drawPoint() 메서드를 이용해 위젯에 점 그리기

## Ex 8-1-1. 점 그리기1 (drawPoint).

import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QPen, QPaintEvent #명시
from PyQt6.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e:QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp:QPainter):
        qp.setPen(QPen(Qt.GlobalColor.blue,  8)) #Qt.blue > Qt.GlobalColor.blue
        qp.drawPoint(self.width()//2, self.height()//2) #self.width()/2 > self.width()//2, darwPoint는 int형 좌표값을 받는다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
