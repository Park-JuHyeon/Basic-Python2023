# pxmap으로 고양이출력
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('./Day10/cat.png')

        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)
        lblsize = QLabel(str(pixmap.width()) + 'x' + str(pixmap.height()))
        lblsize.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Qt.AlignCenter 가능

        vbox = QVBoxLayout(self)
        vbox.addWidget(lblImage)
        vbox.addWidget(lblsize)

        self.setLayout(vbox)

        # 필수설정
        self.setWindowTitle('이미지위젯')
        # self.setGeometry(300,300,300,300)
        self.showFullScreen()   # self.show()
        # self.setCenter()

     # 화면 중심으로 셋팅
    def setCenter(self):
        qr = self.frameGeometry()  # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center()  # 모니터화면 중심잡기
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())



    

    