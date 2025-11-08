# 3-2. 어플리케이션 아이콘 넣기

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): # self는 myApp 객체를 가리킴
        self.setWindowTitle('Icon') # 창 제목 설정
        self.setWindowIcon(QIcon('icon.png')) # 어플리케이션 아이콘 설정
        self.setGeometry(300, 300, 300, 200) # 앞 두 변수는 x, y 위치, 뒤 두 변수는 가로, 세로 크기
        self.show() # 창 띄우기

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())