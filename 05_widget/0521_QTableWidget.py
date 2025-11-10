# 테이블 형태로 항목을 배치하고 다룬다.

## Ex 5-21. QTableWidget.

import sys
from PyQt6.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20) #테이블의 행 개수를 지정
        self.tableWidget.setColumnCount(4) #테이블의 열 개수 지정

        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers) # Qt5에서는 QAbstractItemView.NoEditTriggers / 편집 불가
        # self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.DoubleClicked) #QAbstractItemView.DoubleClicked / 더블 클릭시 편집 가능
        # self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.AllEditTriggers) #QAbstractItemView.AllEditTriggers / 클릭, 더블 클릭등 모든 액션을 통해 편집 가능

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) #QHeaderView.Stretch / 헤더의 폭이 위젯의 폭에 맞춰지도록
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents) #QHeaderView.ResizeToContents / 헤더의 폭이 값의 폭에 맞춰지도록
        # horizontalHeader : 수평 헤더를 반환
        # setSectionResizeMode : 헤더의 크기를 조절
        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(i+j)))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
