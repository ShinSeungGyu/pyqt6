# 메뉴 바 만들기
# File, Edit, View, Tools 등의 메뉴

## Ex 3-6. 메뉴바 만들기.

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QAction # QtWidgets에 있던 QAction은 QtGui로 이동됨
#from PyQt5.QtWidgets import qApp >> pyqt6에서는 삭제되었으며, qApp은 QApplication.instance()로 대체됨

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)  # 아이콘과 Exit 라벨을 갖는 하나의 동작(QAction)을 만들고
        exitAction.setShortcut('Ctrl+Q') # setShortcut : 단축키 설정
        exitAction.setStatusTip('Exit application') # 상태바에 표시될 툴팁 설정
       
        exitAction.triggered.connect(QApplication.instance().quit) #동작을 선택했을때 발생된(triggered) 시그널을 QApplication의 quit 메서드에 연결되어 종료

        self.statusBar() # 상태바 생성

        menubar = self.menuBar() # 메뉴바 생성
        menubar.setNativeMenuBar(False) 
        filemenu = menubar.addMenu('&File') #&는 단축키 설정, Alt + F로 File 메뉴 접근 가능
        filemenu.addAction(exitAction)

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
