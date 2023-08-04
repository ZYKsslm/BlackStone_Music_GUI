from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from qfluentwidgets import FluentIcon

from UI.Ui_importMusicWidget import Ui_importWindow
from subWindow.searchWidget import CustomTableWidget


class ImportWindow(QWidget, Ui_importWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
    
    def setupUi(self, importWindow):
        super().setupUi(importWindow)
        self.sourceBox.setIcon(QPixmap("source/Image/icon.ico"))
        self.sourceBox.addItem("QQ音乐", "source/Image/QQ.png")
        self.SegmentedWidget.addItem("歌单信息", "歌单信息", lambda: self.stackedWidget.setCurrentIndex(0), FluentIcon.INFO)
        self.SegmentedWidget.addItem("歌单内容", "歌单内容", lambda: self.stackedWidget.setCurrentIndex(1), FluentIcon.BOOK_SHELF)
        self.SegmentedWidget.setCurrentItem("歌单信息")
        
        self.frame.setStyleSheet("#frame { border: 1px solid black; border-radius: 10px; }")
        
        self.musicTable = CustomTableWidget(self.musicPage, source_state="import")
        self.musicTable.resize(921, 421)
        self.musicTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

    def bind(self):
        self.sourceBox.currentIndexChanged.connect(self.setSource)
        
    def setSource(self):
        index = self.sourceBox.currentIndex()
        if index == 0:
            self.sourceBox.setIcon(QPixmap("source/Image/QQ.png"))