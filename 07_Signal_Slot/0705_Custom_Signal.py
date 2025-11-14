# 지정된 시그널 외에도 새로운 시그널을 만들어 사용할 수 있다.
# pyqtSignal()을 이용해 사용자 정의 시그널을 만들어, 특정 이벤트 발생 시 시그널이 방출되도록 한다.

## Ex 7-5. 사용자 정의 시그널.

import sys
from PyQt6.QtCore import pyqtSignal, QObject
from PyQt6.QtWidgets import QApplication, QMainWindow


class Communicate(QObject): #Communicate 클래스 생성

    closeApp = pyqtSignal() #pyqtSignal을 사용해 Communicate 클래스의 속성으로 사용자정의 시그널을 생성


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close) # closeApp 시그널을 MyApp 클래스의  close 슬롯에 연결

        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, e):
        self.c.closeApp.emit() # mousePressEvent 핸들러를 사용해 마우스 클릭시 closeApp 시그널이 방출


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
