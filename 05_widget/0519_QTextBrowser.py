# 하이퍼텍스트 내비게이션을 포함하는 리치 텍스트 브라우저를 제공
# 읽기 전용이며, QTextEdit의 확장형으로 하이퍼텍스트 문서의 링크를 사용할 수 있다.
# 편집 가능한 텍스트 편집기를 사용하려면 QTextEdit을 사용해야 한다.
# 또한 네비게이션이 없는 텍스트 브라우저를 사용하려면, setReadOnly()를 사용해 편집을 불가능으로 한다.
# 짧은 리치 텍스트를 표시할땐 QLabel을 사용할 수 있다.

## Ex 5-19. QTextBrowser.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)

        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(self.clear_btn, 2)

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()

    def clear_text(self):
        self.tb.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
