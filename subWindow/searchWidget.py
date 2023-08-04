from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap, QAction
from qfluentwidgets import TableWidget, RoundMenu, MenuAnimationType

from UI.Ui_searchMusicWidget import Ui_searchWindow


class CustomTableWidget(TableWidget):
    def __init__(self, parent=None, download_music=None, download_lyric=None, source_state=""):
        super().__init__(parent)
        self.music_func = download_music
        self.lyric_func = download_lyric
        self.source_state = source_state
        
    def setMusicFunc(self, func):
        self.music_func = func
        
    def setLyricFunc(self, func):
        self.lyric_func = func
        
    def copyContent(self, content):
        clipboard = QApplication.clipboard()
        clipboard.setText(content)
        
    def contextMenuEvent(self, event):
        if self.rowCount() == 0 and self.columnCount() == 0:
            return
        menu = RoundMenu("", self)
        
        # 获取当前行数和内容
        current_row = self.currentRow()
        current_content = self.item(current_row, 0).text()
        
        music_action = QAction("下载音乐", self)
        lyric_action = QAction("下载歌词", self)
        copy_action = QAction("复制内容", self)
        
        music_action.triggered.connect(lambda: self.music_func(self.source_state, current_row, current_content))
        lyric_action.triggered.connect(lambda: self.lyric_func(self.source_state, current_row, current_content))
        copy_action.triggered.connect(lambda: self.copyContent(self.currentItem().text()))
        
        menu.addAction(music_action)
        menu.addAction(lyric_action)
        menu.addSeparator()
        menu.addAction(copy_action)
        menu.exec(event.globalPos(), MenuAnimationType.PULL_UP)


class SearchWindow(QWidget, Ui_searchWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
    
    def setupUi(self, searchWindow):
        super().setupUi(searchWindow)
        self.sourceBox.setIcon(QPixmap("source/Image/icon.ico"))
        self.sourceBox.addItem("酷狗音乐", "source/Image/kugou.jpg")
        self.sourceBox.addItem("酷我音乐", "source/Image/kuwo.png")
        self.sourceBox.addItem("QQ音乐", "source/Image/QQ.png")
        self.sourceBox.addItem("QQ音乐2", "source/Image/QQ.png")
        self.sourceBox.addItem("网易云音乐", "source/Image/wy.png")
        self.sourceBox.addItem("咪咕音乐", "source/Image/migu.png")
        self.sourceBox.addItem("铜钟音乐", "source/Image/tongzhong.png")
        self.sourceBox.addItem("MyFreeMP3", "source/Image/MyFreeMP3.ico")
        
        self.musicTable = CustomTableWidget(self, source_state="search")
        self.musicTable.setGeometry(30, 100, 931, 471)
        self.musicTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    
    def bind(self):
        self.sourceBox.currentIndexChanged.connect(self.setSource)
        
    def setSource(self):
        index = self.sourceBox.currentIndex()
        if index == 0:
            self.sourceBox.setIcon(QPixmap("source/Image/kugou.jpg"))
        elif index == 1:
            self.sourceBox.setIcon(QPixmap("source/Image/kuwo.png"))
        elif index == 2:
            self.sourceBox.setIcon(QPixmap("source/Image/QQ.png"))
        elif index == 3:
            self.sourceBox.setIcon(QPixmap("source/Image/QQ.png"))
        elif index == 4:
            self.sourceBox.setIcon(QPixmap("source/Image/wy.png"))
        elif index == 5:
            self.sourceBox.setIcon(QPixmap("source/Image/migu.png"))
        elif index == 6:
            self.sourceBox.setIcon(QPixmap("source/Image/tongzhong.png"))
        elif index == 7:
            self.sourceBox.setIcon(QPixmap("source/Image/MyFreeMP3.ico"))