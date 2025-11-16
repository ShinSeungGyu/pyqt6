# 창 닫기

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): # self는 myApp 객체를 가리킴
        btn = QPushButton('Quit', self) # 버튼 생성
        btn.move(50, 50) # 버튼 위치 설정
        btn.resize(btn.sizeHint()) # 버튼 크기 설정
        btn.clicked.connect(QCoreApplication.instance().quit) # 버튼 클릭 시 어플리케이션 종료

        self.setWindowTitle('Quit Button') # 창 제목 설정
        self.setGeometry(300, 300, 300, 200) # 앞 두 변수는 x, y 위치, 뒤 두 변수는 가로, 세로 크기
        self.show() # 창 띄우기

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())