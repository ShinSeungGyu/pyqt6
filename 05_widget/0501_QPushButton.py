# 푸시버튼 / 명령버튼
# 가장 흔하게 사용되고 중요한 위젯

# 자주 쓰이는 메서드
# setCheckable() : True 설정 시, 누른 상태와 그렇지 않은 상태를 구분
# toggle() : 상태를 바꿈
# setIcon() : 버튼에 아이콘 설정
# setEnabled() : False 설정 시, 버튼 비활성화
# isChecked() : 버튼의 선택 여부 반환
# setText() : 버튼에 쓰일 텍스트 설정
# text() : 버튼에 표시된 텍스트 반환

# 쓰이는 시그널
# clicked() : 버튼이 클릭되었을 때 발생
# pressed() : 버튼이 눌러졌을 때 발생
# released() : 버튼이 눌러졌다가 떼어졌을 때 발생
# toggled() : 버튼의 상태가 바뀌었을 때 발생

## Ex 5-1. QPushButton.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2') # 텍스트 설정

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False) # 버튼 비활성화

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
