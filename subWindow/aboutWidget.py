from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap, QDesktopServices
from qfluentwidgets import FluentIcon
from UI.Ui_aboutWidget import Ui_aboutWindow


class AboutWindow(QWidget, Ui_aboutWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setPixmap(QPixmap("source/Image/icon.ico"))
        self.SegmentedWidget.addItem("关于软件", "关于软件", lambda: self.stackedWidget.setCurrentIndex(0), FluentIcon.INFO)
        self.SegmentedWidget.addItem("软件更新", "软件更新", lambda: self.stackedWidget.setCurrentIndex(1), FluentIcon.UPDATE)
        self.SegmentedWidget.setCurrentItem("关于软件")
        
        self.githubBtn.setIcon(FluentIcon.GITHUB)
        self.githubBtn.clicked.connect(lambda: QDesktopServices.openUrl("https://github.com/ZYKsslm/BlackStone_Music_GUI"))
        self.updateBtn.setIcon(FluentIcon.UPDATE)