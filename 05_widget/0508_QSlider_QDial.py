# QSlider
# 수평 또는 수직 방향의 슬라이더를 제공
# 제한된 범위 내에서 값을 조절하는 위젯
# 슬라이더의 틱 간격을 조절하기 위해서 setTickInterval() 메서드를 사용
# 틱의 위치를 조절하기 위해서는 setTickPosition() 메서드를 사용, 픽셀이 아니라 값을 입력
# setTickPosition()의 입력값과 기능
# QSlider.NoTicks : 틱 없음 : 0
# QSlider.TicksAbove : 틱을 슬라이더 위쪽에 표시 : 1
# QSlider.TicksBelow : 틱을 슬라이더 아래쪽에 표시 : 2
# QSlider.TicksBothSides : 틱을 슬라이더 양쪽에 표시 : 3
# QSlider.TicksLeft : 틱을 슬라이더 왼쪽에 표시 : TicksAbove
# QSlider.TicksRight : 틱을 슬라이더 오른쪽에 표시 : TicksBelow


# QDial : 둥근 형태의 다이얼 위젯, 기본적으로 같은 시그널, 슬롯, 메서드를 공유한다.

# 자주 쓰이는 시그널
# valueChanged() : 슬라이더 값이 변할때
# sliderPressed() : 사용자가 슬라이더를 움직이기 시작할때
# sliderMoved() : 사용자가 슬라이더를 움직이면 발생
# sliderReleased() : 사용자가 슬라이더를 놓을때 발생

## Ex 5-8. QSlider & QDial.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt6.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider = QSlider(Qt.Orientation.Horizontal, self) #Qt6에서는 Qt.Horizontal이 Qt.Orientation.Horizontal 로 변경되었다.
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)

        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)

        btn = QPushButton('Default', self)
        btn.move(35, 160)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
