# 이번에는 mouseMoveEvent를 이용해서 마우스의 위치를 트래킹해서 출력해보겠습니다.

## Ex 7-4. 이벤트 핸들러 재구성하기2.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QMouseEvent


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x = 0
        y = 0

        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(20, 20)

        self.setMouseTracking(True)

        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mouseMoveEvent(self, e:QMouseEvent): #QMouseEvent 명시
        x = e.position().x() # PyQt5에서는 e.x()
        y = e.position().y() # PyQt5에서는 e.y()

        text = 'x: {0}, y: {1}'.format(x, y)
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
