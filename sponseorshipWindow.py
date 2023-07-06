from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap, QIcon


class sponsorshipWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self, Pixmap=QPixmap("Image/sponsorship.jpg"))
        self.setWindowTitle("打赏项目")
        self.setWindowIcon(QIcon("Image/icon.png"))
        self.setFixedSize(367, 500)