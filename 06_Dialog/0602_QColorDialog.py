# 색상을 선택할 수 있는 다이얼로그

## Ex 6-2. QColorDialog.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt6.QtGui import QColor


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name()) #색상 선택 후 OK 버튼 시 True 반환, Cancel 버튼 시 False 반환
        self.frm.setGeometry(130, 35, 100, 100)

        self.setWindowTitle('Color Dialog')
        self.setGeometry(300, 300, 250, 180)
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name()) 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
