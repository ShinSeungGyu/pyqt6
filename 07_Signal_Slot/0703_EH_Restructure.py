# 이벤트 핸들러 재구성
# 자주 쓰이는 핸들러는 이미 만들어져 있는 경우들이 많다.
# 이벤트 핸들러를 수정해서 추가적인 기능을 구현할 수 있다.

## Ex 7-3. 이벤트 핸들러 재구성하기.

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QKeyEvent


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, e:QKeyEvent):
        if e.key() == Qt.Key.Key_Escape: #열거형으로 변경되어 Qt.Key 클래스에 존재한다.
            self.close()
        elif e.key() == Qt.Key.Key_F:
            self.showFullScreen()
        elif e.key() == Qt.Key.Key_N:
            self.showNormal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
