# 입력 다이얼로그
# 사용자가 간단한 값을 입력할 때 사용하는 다이얼로그
# 입력값은 숫자, 문자열, 리스트에서 선택한 항목 등이 될 수 있다.
# 입력값의 형태에 따라 다섯개의 함수가 제공된다.

# getText()
# getMultiLineText()
# getInt()
# getDouble()
# getItem()

## Ex 6-1. QInputDialog.

import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(120, 35)

        self.setWindowTitle('Input dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
