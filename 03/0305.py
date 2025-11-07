# 상태바 만들기
# 메인창은 메뉴바/툴바/상태바를 갖는 어플리케이션 창이다.
# 메뉴바-QMenuBar / 툴바-QToolBar(독 위젯 - QDockWidget, 센트럴 위젯)  / 상태바-QStatusBar

# QMainWindow 클래스를 이용해 메인 어플리케이션 창을 만들 수 있다.

# 상태바는 어플리케이션의 상태를 알려주기 위해 하단에 위치하는 위젯이다.
# 상태바에 텍스트 표기를 위해서 showMessage() 를 사용한다.
# 텍스트를 사라지게 하려면 clearMessage() 를 사용하거나, showMessage() 의 두 번째 인자에 밀리초 단위의 시간을 지정한다.
# 현재 상태바에 표시된 메세지 텍스트를 가져올 땐 currentMessage() 를 사용한다.
# QStatusBar 클래스는 상태바 메시지가 바뀔 때마다 messageChanged() 시그널을 발생시킨다.

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')  # 상태바에 메시지 표시

        self.setWindowTitle('Status Bar Example')  # 창 제목 설정
        self.setGeometry(300, 300, 400, 300)  # 창 위치와 크기 설정
        self.show()  # 창 띄우기

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())