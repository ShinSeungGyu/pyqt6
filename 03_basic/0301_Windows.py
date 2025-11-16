## 3-1. 창띄우기
import sys
from PyQt6.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self): # self는 myApp 객체를 가리킴
        self.setWindowTitle('My First PyQt6 App') # 창 제목 설정
        self.move(300, 300) # 창 위치 설정
        self.resize(400, 200) # 창 크기 설정
        self.show() # 창 띄우기

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())