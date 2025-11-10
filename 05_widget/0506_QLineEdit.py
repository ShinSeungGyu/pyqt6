# QLineEdit
# 한 줄의 문자열을 입력 및 수정할 수 있도록 하는 위젯
# echoMode()를 설정함으로써 "쓰기 전용" 영역으로 사용할 수 있다.
# setEchoMode() 메서드로 모드를 설정할 수 있다.

# QLineEdit.Normal : 0 : 입력된 문자를 표시
# QLineEdit.NoEcho : 1 : 입력된 문자를 표시하지 않음(비밀번호의 글자수도 공개하지 않음)
# QLineEdit.Password : 2 : 입력된 문자를 별표(*)로 표시
# QLineEdit.PasswordEchoOnEdit : 3 : 편집하는 동안에는 문자를 표시하고, 편집이 끝나면 별표(*)로 표시

# maxLength() 메서드로 텍스트 최대 길이 제한 가능
# setValidator() 메서드로 입력되는 텍스트의 종류를 제한 가능

# setText() 또는 insert() 메서드로 텍스트를 편집할 수 있고, text() 메서드로 현재 텍스트를 가져올 수 있다.
# 만약 echoMode에 의해 입력되는 텍스트와 표시되는 텍스트가 다르다면, displayText() 메서드로 표시되는 텍스트를 가져올 수 있다.

# setSelection(), selectAll() 메서드로 텍스트를 선택하거나, cut(), copy(), paste() 메서드로 클립보드와 상호작용할 수 있다.
# setAlignment() 메서드로 텍스트의 정렬 방식을 설정할 수 있다.

# 텍스트가 변경되거나 커서가 움직일 때, textChanged, cursorPositionChanged 시그널이 발생한다.

# 자주 사용되는 시그널
# cursorPositionChanged(int, int) : 커서의 위치가 변경될 때 발생
# editingFinished() : 편집이 끝났을 때(Return/Enter 키를 눌렀을 때) 발생
# returnPressed() : Return/Enter 키를 눌렀을 때 발생
# selectionChanged() : 선택 영역이 바뀔 때 신호 발생
# textChanged(str) : 텍스트가 변경될 때 발생
# textEdited(str) : 텍스트를 편집할 때 발생

## Ex 5-6. QLineEdit.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self) # 라벨 객체 생성
        self.lbl.move(60, 40)

        qle = QLineEdit(self) # QLineEdit 객체 생성
        qle.move(60, 100)
        qle.textChanged.connect(self.onChanged) # 텍스트가 변경될 때(qle.textChanged.connect) onChanged 메서드 호출

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text) # 전달된 text를 라벨의 텍스트로 설정
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())

