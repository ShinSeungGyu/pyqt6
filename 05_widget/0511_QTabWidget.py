# QTabWidget

# 상단에 Tab이 있는 창을 볼 수 있다. 카테고리에 따라 분류할 수 있기에 유용하게 사용할 수 있다.

## Ex 5-11. QTabWidget.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 각 탭에 위치할 두 위젯
        tab1 = QWidget()
        tab2 = QWidget()

        # QTabWidget으로 탭을 설정하고, 위젯 두개를 addTab으로 등록
        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')

        # 수직박스 레이아웃을 만들어 tabs를 등록하고, 해당 레이아웃을 위젯의 레이아웃으로 설정
        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
