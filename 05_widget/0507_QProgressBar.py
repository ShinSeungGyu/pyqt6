# QProgressBar

# ProgressBar는 작업의 진행 상태를 시각적으로 표시하는 위젯이다.
# QProgressBar 위젯은 수평, 수직의 진행 표시줄을 제공한다. setMinimum()과 setMaximum() 메서드를 사용하여 진행 표시줄의 최소와 최대를 설정할 수 있으며,
# setRange() 메서드를 사용하여 한 번에 범위를 설정할 수 있다. 기본값으로는 0~99로 설정되어 있다.

# setValue() 메서드로 진행 표시줄의 진행 상태를 특정 값으로 설정할 수 있고, reset() 메서드는 초기상태로 되돌린다.

# 진행 표시줄의 최소와 최대를 모두 0으로 설정하면, 진행 상태를 알 수 없는 상태가 된다.

## Ex 5-7. QProgressBar.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt6.QtCore import QBasicTimer


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self) #전역변수 설정
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer() #진행 표시줄 활성화를 위한 타이머 객체
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e): #이벤트 핸들러, e는 QTimerEvent 객체를 의미한다.
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self) #첫번째 매개변수는 타이머 간격(단위는 ms), 두번째 매개변수는 타이머 이벤트를 받을 객체
            # 첫번째 매개변수의 숫자가 작을수록 타이머가 빨라지고, 숫자가 클수록 느려진다.
            # 100ms마다 timerEvent 메서드가 호출된다.
            self.btn.setText('Stop')
# 타이머가 active 상태이면 stop 메서드로 멈추고 / active 상태가 아닌데, clicked 시그널이 발생하면 start 메서드를 호출한다.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
