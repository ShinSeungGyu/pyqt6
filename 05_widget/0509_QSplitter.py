# QSplitter
# 스플리터 위젯을 구현한다.
# 경계를 드래그하여 자식 위젯의 크기를 조절할 수 있다.

## Ex 5-9. QSplitter.

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt6.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        top = QFrame()
        top.setFrameShape(QFrame.Shape.Box) # QFrame.Box > QFrame.Shape.Box

        midleft = QFrame()
        midleft.setFrameShape(QFrame.Shape.StyledPanel)  # QFrame.StyledPanel > QFrame.Shape.StyledPanel

        midright = QFrame()
        midright.setFrameShape(QFrame.Shape.Panel) # QFrame.Panel > QFrame.Shape.Panel

        bottom = QFrame()
        bottom.setFrameShape(QFrame.Shape.WinPanel) # QFrame.WinPanel > QFrame.Shape.WinPanel
        bottom.setFrameShadow(QFrame.Shadow.Sunken) # QFrame.Sunken > QFrame.Shadow.Sunken
        # 4개의 작은 영역을 설정한뒤

        splitter1 = QSplitter(Qt.Orientation.Horizontal) # Qt.Horizontal > Qt.Orientation.Horizontal
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)
        # splitter1에 수평으로 두개의 영역을 넣고(midleft, midright)

        splitter2 = QSplitter(Qt.Orientation.Vertical) # Qt.Vertical > Qt.Orientation.Vertical
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        # splitter2에 수직으로 top, splitter1, bottom 3개를 쌓는다.        
    
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
