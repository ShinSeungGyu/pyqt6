# 사용자에게 정보를 제공하거나 질문과 대답을 할 수 있는 대화창을 제공
# 어떤 동작에 대해 확인이 필요한 경우 메시지박스를 사용한다.

## Ex 6-5. QMessageBox.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt6.QtGui import QCloseEvent


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def closeEvent(self, event:QCloseEvent): #event에 타입을 명시함으로써 하단에 메서드가 색상을 띔(없어도 동작한다.)
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No) # Qt5 에서는 QMessageBox.Yes/No
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec())
