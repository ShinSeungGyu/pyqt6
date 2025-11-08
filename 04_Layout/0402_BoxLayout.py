# 박스 레이아웃
# 훨씬 유연하고 실용적인 레이아웃
# 여러 위젯을 수평으로 정렬하는 레이아웃 클래스 : QHBoxLayout, QVBoxLayout
# 수평, 수직의 박스를 하나 만드는데, 다른 레이아웃 박스나 위젯을 배치할 수 있다.

## Ex 4-2. 박스 레이아웃.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 두개의 버튼 생성
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        # 수평 박스를 만들고 앞뒤에 공백을 추가
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)
        # addStretch()는 신축성 있는 빈 공간을 제공하여, 창의 크기가 변화해도 두 빈공간이 동일하게 유지된다.
        # 이를 통해 버튼들이 창의 가운데에 위치하게 된다.

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        # 수평 박스를 수직 박스에 넣고 위 아래에 공백을 3:1 비율로 추가한다.

        self.setLayout(vbox) #이 수직 박스를 창의 레이아웃으로 설정

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
