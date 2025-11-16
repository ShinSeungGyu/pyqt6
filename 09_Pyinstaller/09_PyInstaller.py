# 1. PyInstaller 설치
# 아래 명령어를 통해 패키지 설치
# pip install pyinstaller
# -------------------------------------------------------------------------
# 2. 실행파일 만들기
# Python 파일이 있는 폴더로 이동 후, 아래 명령어를 입력해 해당 폴더에 실행파일 생성
# pyinstaller qtextbrowser_advanced.py
# 
# 만들어진 폴더에서 dist로 이동해 한번 더 들어가면 실행파일을 찾을 수 있다.
# 더블 클릭해 실행해보면 콘솔창이 함께 출력된다.
# -------------------------------------------------------------------------
# 3. 콘솔창 출력되지 않도록 하기
# 콘솔창이 안나오게 하려면 명령어에서 -w 또는 --windowed 를 추가한다.
# pyinstaller -w qtextbrowser_advanced.py
# pyinstaller --windowed qtextbrowser_advanced.py

# -------------------------------------------------------------------------
# 4. 실행파일 하나만 생성하기
# 실행파일 하나만 생성하기 위해서는 -F 또는 -onefile 을 추가한다.
# pyinstaller -w -F qtextbrowser_advanced.py

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QTextBrowser, QLabel
from PyQt6.QtCore import Qt
import requests
from bs4 import BeautifulSoup

class MyApp(QMainWindow): # QMainWindow를 상속받아야 GUI가 정상 작동합니다.
    def __init__(self):
        super().__init__() # QMainWindow의 __init__ 호출
        self.initUI()
        self.show() # QMainWindow를 화면에 표시

    def initUI(self):
        # 기존 코드 시작
        self.le = QLineEdit()
        self.le.setPlaceholderText('Enter your search word')
        self.le.returnPressed.connect(self.crawl_news)

        self.btn = QPushButton('Search')
        self.btn.clicked.connect(self.crawl_news)
        # 기존 코드 끝

        # ---- GUI가 작동하기 위해 추가/수정된 부분 ----
        self.setWindowTitle('뉴스 검색기')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # self.news_display 위젯 정의
        self.news_display = QTextBrowser() 
        self.news_display.setOpenExternalLinks(True)

        main_layout.addWidget(QLabel('<b>뉴스 검색 키워드:</b>'))
        main_layout.addWidget(self.le)
        main_layout.addWidget(self.btn)
        main_layout.addWidget(QLabel('<b>검색 결과:</b>'))
        main_layout.addWidget(self.news_display)
        # ---------------------------------------------

    def crawl_news(self):
        query = self.le.text().strip()
        print(f"[DEBUG] 검색어: '{query}'")
        
        if not query:
            if hasattr(self, 'news_display'):
                self.news_display.setHtml("<p style='color: red;'>검색어를 입력해주세요!</p>")
            else:
                print("[ERROR] 'self.news_display' 위젯이 정의되지 않아 GUI에 메시지를 표시할 수 없습니다.")
            return

        if hasattr(self, 'news_display'):
            self.news_display.setHtml(f"<p><b>'{query}'</b>에 대한 뉴스 검색 중...</p>")
            QApplication.processEvents()
        else:
            print("[DEBUG] 'self.news_display' 위젯이 정의되지 않았습니다. GUI 업데이트를 건너뜀.")
        
        print(f"[DEBUG] 뉴스 검색을 시작합니다: '{query}'")

        try:
            url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={query}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            
            print(f"[DEBUG] 요청 URL: {url}")
            response = requests.get(url, headers=headers, timeout=10)
            print(f"[DEBUG] HTTP 응답 코드: {response.status_code}")
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            print("[DEBUG] HTML 파싱 완료.")

            # ---- 이 부분을 아래와 같이 수정합니다. ----
            news_items = soup.select('a[data-heatmap-target*=".tit"]') # <a class="news_tit"> 태그를 직접 찾습니다.
            # ----------------------------------------
            
            print(f"[DEBUG] 찾은 뉴스 항목 수: {len(news_items)}개")
            
            if not news_items:
                if hasattr(self, 'news_display'):
                    self.news_display.setHtml(f"<p style='color: orange;'><b>'{query}'</b>에 대한 뉴스 결과를 찾을 수 없습니다.</p>")
                else:
                    print(f"[DEBUG] '{query}'에 대한 뉴스 결과를 찾을 수 없습니다. (GUI 미표시)")
                return

            items_html = "\n".join([
                f"<li><a href='{item.get('href')}'>{item.get_text()}</a></li>"
                for item in news_items
            ])
            results_html = f"<p><b>'{query}'</b>에 대한 뉴스 검색 결과:</p><ul>{items_html}</ul>"
            
            if hasattr(self, 'news_display'):
                self.news_display.setHtml(results_html)
            else:
                print("[DEBUG] 검색 결과 (GUI 미표시):\n", results_html)

        except requests.exceptions.Timeout:
            error_msg = "<p style='color: red;'>뉴스 서버 응답 시간이 초과되었습니다. 네트워크 상태를 확인하거나 잠시 후 다시 시도해주세요.</p>"
            if hasattr(self, 'news_display'):
                self.news_display.setHtml(error_msg)
            print(f"[ERROR] Timeout: {error_msg}")
        except requests.exceptions.RequestException as e:
            error_msg = f"<p style='color: red;'>네트워크 연결 또는 요청 중 오류가 발생했습니다: {e}</p>"
            if hasattr(self, 'news_display'):
                self.news_display.setHtml(error_msg)
            print(f"[ERROR] RequestException: {e}")
        except Exception as e:
            error_msg = f"<p style='color: red;'>뉴스 데이터를 처리하는 중 예상치 못한 오류가 발생했습니다: {e}</p>"
            if hasattr(self, 'news_display'):
                self.news_display.setHtml(error_msg)
            print(f"[ERROR] Unexpected Error: {e}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())