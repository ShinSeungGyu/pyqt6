# 그리드 레이아웃
# 가장 일반적인 레이아웃 클래스이다.
# 위젯의 공간을 행과 열로 구분한다.
# QGridLayout 클래스를 사용하여 그리드 레이아웃을 만든다.

## Ex 4-3. 그리드 레이아웃.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        #addWidget(위젯, 행, 열)
        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)
        #각 라벨을 첫번째 열에 수직으로 배치

        #두번째 열에 입력 위젯 배치
        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)
        #QTextEdit 위젯은 여러 줄의 텍스트를 입력할 수 있는 위젯

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
