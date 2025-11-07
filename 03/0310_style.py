## Ex 3-10. 스타일 꾸미기.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #3개의 라벨 생성, 괄호 안에는 텍스트
        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')

        lbl_red.setStyleSheet("color: red;" # 글자 색상 설정
                             "border-style: solid;" # 테두리 스타일 설정
                             "border-width: 2px;" # 테두리 두께 설정
                             "border-color: #FA8072;" # 테두리 색상 설정
                             "border-radius: 3px") # 테두리 둥글기 설정
        lbl_green.setStyleSheet("color: green;"
                                "background-color: #7FFFD4") # 배경 색상 설정
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
