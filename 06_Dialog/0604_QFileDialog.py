# 사용자가 파일 또는 경로를 선택할 수 있는 다이얼로그
# 사용자는 파일을 열어서 수정하거나 저장할 수 있다.

## Ex 6-4. QFileDialog.

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QFileDialog #Qt5 에서는 QtWidgets에 있던게 QtGui로 이동되었다.
from PyQt6.QtGui import QIcon, QAction

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            f = open(fname[0], 'r', encoding='utf-8') # 한국어가 포함된 파일을 읽으려고 할경우 디코딩 에러를 발생시킨다. 따라서 encoding 옵션을 추가하였다.

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
