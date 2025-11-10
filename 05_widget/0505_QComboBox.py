# QComboBox

#   작은 공간을 차지하면서 여러 옵션 중 하나의 옵션을 선택할 수 있도록 하는 위젯

## Ex 5-5. QComboBox.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)

        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)

        cb.textActivated.connect(self.onActivated) #Qt6에서는 activated 대신 textActivated 사용, 따라서 [str] 표기 의무도 사라짐
        
        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
