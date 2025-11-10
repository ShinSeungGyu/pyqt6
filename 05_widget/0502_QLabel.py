# QLabel
# 텍스트나 이미지를 표시하는 위젯
# 사용자와 어떠한 상호작용을 제공하진 않는다.

# 기본적으로 수평방향으로는 왼쪽 / 수직 방향으로는 가운데 정렬이지만,
# setAlignment() 메서드를 사용하여 정렬 방식을 변경할 수 있다.

## Ex 5-2. QLabel 위젯 사용하기.
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter) #PyQt6에서는 Qt.AlignCenter 대신 Qt.AlignmentFlag.AlignCenter 사용

        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        font1 = label1.font() #label1의 폰트를 font1에 저장
        font1.setPointSize(20)

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        label1.setFont(font1) #변경된 font1을 label1에 설정
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())