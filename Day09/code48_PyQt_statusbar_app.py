# https://wikidocs.net/21853
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QTime

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 메뉴바 - 액션
        actExit = QAction(QIcon('./Day09/exit.png'), 'Exit', self)
        actExit.setShortcut('Ctrl+Q')   # 단축기 지정
        actExit.setStatusTip('앱 종료@!')
        actExit.triggered.connect(qApp.quit)   # 클릭하면 종료

        actSave = QAction(QIcon('./Day09/save.png'),'Save', self)
        actSave.setShortcut('Ctrl+S')
        actSave.setStatusTip('저장')

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(actExit)

        # 툴바
        toolbar = self.addToolBar('MainToolBar')
        toolbar.addAction(actSave)
        toolbar.addAction(actExit)

        # 상태바
        now = QDate.currentDate()  # 현재 날짜
        time = QTime.currentTime()  # 현재 시간
        self.statusBar().showMessage(now.toString('yyyy-MM-dd-dddd') + ' ' + time.toString('hh:mm:ss'))
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        # GUI 화면 설정
        self.setWindowTitle('Bar Window')
        # self.move(1920 // 2 -200, 1080//2 - 200)  # 정중앙에 표시하는 방법
        self.resize(400, 200)
        self.setCenter()
        self.show()   # 핵심!!! 위젯을 화면에 보여줌

    # 화면 중심으로 셋팅
    def setCenter(self):
        qr = self.frameGeometry()  # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center()  # 모니터화면 중심잡기
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
