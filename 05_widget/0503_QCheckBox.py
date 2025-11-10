# QCheckBox 위젯
# on/off, 체크박스 형태를 제공한다.
# 체크박스가 선택되거나 해제될 때 stateChanged 시그널이 발생한다.
# 또한 체크박스의 선택 여부를 확인하기 위해 isChecked() 메서드를 제공한다.

# 일반적인 체크박스는 선택/해제 상태로 나뉘지만, setTristate 메서드는 변경없음 상태를 추가할 수 있다.
# 이 체크박스는 사용자에게 선택하거나 선택하지 않을 옵션을 줄 때 유용하다.

# 세 가지 상태를 가지는 체크박스를 만들려면 checkState 메서드를 사용한다. 선택/변경없음/해제 여부에 따라 2/1/0 값을 가진다.
# QButtonGroup 클래스를 통해 여러 버튼을 묶어 exclusive/non-exclusive 그룹으로 만들 수 있다.
# exclusive 그룹에서는 하나의 버튼만 선택할 수 있고, non-exclusive 그룹에서는 여러 버튼을 선택할 수 있다.

# QCheckBox 위젯에서 자주 쓰이는 메서드
# text() : 체크박스에 표시된 텍스트를 반환
# setText(text) : 체크박스에 표시될 텍스트를 설정
# isChecked() : 체크박스가 선택되었는지 여부를 반환
# checkState() : 체크박스의 현재 상태를 반환 (0: 해제, 1: 변경없음, 2: 선택)
# toggle() : 체크박스의 상태를 변경

# 자주 쓰이는 시그널
# pressed() : 체크박스를 누를 때 발생
# released() : 체크박스에서 뗄 때 신호 발생
# cliked() : 체크박스를 클릭할 때 발생
# stateCanged() : 체크박스의 상태가 변경될 때 발생

## Ex 5-3. QCheckBox.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt6.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.checkStateChanged.connect(self.changeTitle) #Qt6에서는 stateChanged 대신 checkStateChanged 사용

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.CheckState.Checked: #Qt6에서는 Qt.Checked 대신 Qt.CheckState.Checked 사용
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
