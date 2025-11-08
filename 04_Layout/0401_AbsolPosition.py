# 레이아웃
# 어플리케이션 창에 위젯들을 배치하는 방식
# 절대적 배치, 박스 레이아웃, 그리드 레이아웃 3가지로 나뉜다.

## 절대적 배치.
# 위젯의 위치와 크기를 픽셀 단위로 설정하여 배치
# 창 크기를 조절해도 위젯의 크기와 위치는 변하지 않는다.
# 플랫폼에 따라 어플리케이션이 다르게 보일 수 있다.
# 폰트를 바꾸면 레이아웃이 망가질 수 있다.
# 레이아웃 변경 시 완전 새로 고쳐야 하며 매우 번거롭다.

## Ex 4-1. 절대적 배치.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
