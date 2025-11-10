# QRadioButton

# 사용자가 선택할 수 있는 버튼을 만들때 사용
# 체크박스와 마찬가지로 텍스트 라벨이 포함된다.

# 여러 옵션 중 하나의 옵션을 선택할 때 사용되며, 한 위젯 안에 여러 라디오 버튼은 기본적으로 auto-exclusive 속성이 적용된다.
# 하나의 버튼을 선택하면 나머지 버튼은 선택이 해제된다.

# 여러 버튼을 선택할 수 있도록 하려면 setAutoExclusive(False) 메서드를 사용한다.
# 한 위젯 안에 여러 그룹의 라디오 버튼을 만들려면 QButtonGroup 클래스를 사용한다.

# 체크박스와 마찬가지로 버튼의 상태가 바뀔 때, toggled 시그널이 발생한다.
# 또한 특정 버튼의 상태를 가져오고 싶을 때 isChecked() 메서드를 사용한다.

# 자주 쓰는 메서드
#text() : 버튼의 텍스트 반환
#setText(text) : 버튼의 텍스트 설정
#isChecked() : 버튼이 선택되었는지 여부 반환
#setChecked(bool) : 버튼의 선택 상태 설정
#toggle() : 버튼의 상태를 변경

# 자주 쓰이는 시그널
#pressed() : 버튼을 누를 때 발생
#released() : 버튼에서 뗄 때 발생
#clicked() : 버튼을 클릭할 때 발생
#toggled() : 버튼의 상태가 변경될 때 발생

## Ex 5-4. QRadioButton.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rbtn1 = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
