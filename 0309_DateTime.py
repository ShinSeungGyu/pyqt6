# QtCore 모듈의 QDate, QTime, QDateTime 클래스를 통해 날짜와 시간 표기 가능

# 날짜 : QDate 클래스 사용
from PyQt6.QtCore import QDate, Qt, QLocale

now = QDate.currentDate()  # 현재 날짜 가져오기
print(now.toString())  # 날짜를 문자열로 변환하여 출력
print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('ddd.MMMM.yyyy'))
print(now.toString(Qt.DateFormat.ISODate)) # QtPy5 에선 Qt.ISODate 사용
print(now.toString(QLocale(QLocale.system()).toString(now, QLocale.FormatType.LongFormat))) # QtPy5 에선 Qt.DefaultLocaleLongDate 사용

print("----------------------")
print("----------------------")

# 시간 : QTime 클래스 사용
from PyQt6.QtCore import QTime

time = QTime.currentTime()
print(time.toString())  # 시간을 문자열로 변환하여 출력
print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString('hh.mm.ss.zzz'))
print(time.toString(QLocale(QLocale.system()).toString(time, QLocale.FormatType.LongFormat))) #Qt.DefaultLocaleLongDate
print(time.toString(QLocale(QLocale.system()).toString(time, QLocale.FormatType.ShortFormat))) #Qt.DefaultLocaleShortDate

print("----------------------")
print("----------------------")

# 날짜와 시간 : QDateTime 클래스 사용
from PyQt6.QtCore import QDateTime

datetime = QDateTime.currentDateTime()
print(datetime.toString())  # 날짜와 시간을 문자열로 변환하여 출력
datetime = QDateTime.currentDateTime()
print(datetime.toString('d.M.yy hh:mm:ss'))
print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
print(datetime.toString(QLocale(QLocale.system()).toString(datetime, QLocale.FormatType.LongFormat))) #Qt.DefaultLocaleLongDate
print(datetime.toString(QLocale(QLocale.system()).toString(datetime, QLocale.FormatType.ShortFormat))) #Qt.DefaultLocaleShortDate

print("----------------------")
print("----------------------")

# 상태표시줄에 날짜 표시
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QDateTime, Qt

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        AppTime_str = self.date.toString(QLocale(QLocale.system()).toString(datetime, QLocale.FormatType.ShortFormat))
        self.statusBar().showMessage(AppTime_str)  # 상태바에 현재 날짜와 시간 표시

        self.setWindowTitle('DateTime in Status Bar')  # 창 제목 설정
        self.setGeometry(300, 300, 400, 300)  # 창 위치와 크기 설정
        self.show()  # 창 띄우기

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())