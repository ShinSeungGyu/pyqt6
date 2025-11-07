# 툴팁 나타내기
# 위젯의 기능을 설명하는 등의 말풍선 형태의 도움말
# setToolTip() 메서드 사용

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt6.QtGui import QFont

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10)) # 툴팁 폰트 설정
        self.setToolTip('This is a <b>QWidget</b> widget') # 창에 툴팁 설정

        btn = QPushButton('Button', self) # 버튼 생성
        btn.setToolTip('This is a <b>QPushButton</b> widget') # 버튼에 툴팁 설정
        btn.move(50, 50) # 버튼 위치 설정
        btn.resize(btn.sizeHint()) # 버튼 크기 설정

        self.setWindowTitle('Tooltips') # 창 제목 설정
        self.setGeometry(300, 300, 300, 200) # 앞 두 변수는 x, y 위치, 뒤 두 변수는 가로, 세로 크기
        self.show() # 창 띄우기

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())