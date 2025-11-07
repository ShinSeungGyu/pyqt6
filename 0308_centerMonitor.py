## Ex 3-8. 창을 화면의 가운데로.

import sys
from PyQt6.QtWidgets import QApplication, QWidget #QDesktopWidget은 QScreen으로 대체되었다. QAppication.primaryScreen() 사용

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500, 350)
        self.center() #center 메서드 호출
        self.show()

    def center(self):
        qr = self.frameGeometry() #변수에 화면 상에서 위젯이 실제로 차지하는 공간의 정보를 가져온다.
        cp = QApplication.primaryScreen().availableGeometry().center() #화면의 가운데 위치 정보를 가져온다.
        # primaryScreen() : 기본 화면 정보를 가져온다.(주모니터)
        # availableGeometry() : 작업 표시줄을 제외한 화면의 사용 가능한 영역 정보를 가져온다.
        # center() : 영역의 가운데 위치 정보를 가져온다. (x, y 좌표)
        qr.moveCenter(cp) #qr의 x,y 좌표를 cp의 값으로 이동시킨다.
        self.move(qr.topLeft()) #현재 창을, 화면의 중심으로 이동했던 직사각형(qr)의 위치로 이동시킵니다.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
