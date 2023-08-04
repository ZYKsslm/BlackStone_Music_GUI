from PySide6.QtWidgets import *
from qfluentwidgets import FluentIcon

from UI.Ui_settingWidget import Ui_settingWindow


class SettingWindow(QWidget, Ui_settingWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def setupUi(self, settingWindow):
        super().setupUi(settingWindow)
        self.SegmentedWidget.addItem("样式设置", "样式设置", lambda: self.stackedWidget.setCurrentIndex(0), FluentIcon.BRUSH)
        self.SegmentedWidget.addItem("文件设置", "文件设置", lambda: self.stackedWidget.setCurrentIndex(1), FluentIcon.FOLDER)
        self.SegmentedWidget.addItem("下载设置", "下载设置", lambda: self.stackedWidget.setCurrentIndex(2), FluentIcon.DOWNLOAD)
        self.SegmentedWidget.setCurrentItem("样式设置")
        
        self.themeBox.addItems(["明亮", "暗黑", "系统"])
        self.opacitySlider.setMinimum(1)
        self.opacitySlider.setMaximum(10)
        self.opacitySlider.setSingleStep(1)
        
        self.horizontalFrame.setStyleSheet("#horizontalFrame { border: 1px solid black; border-radius: 10px; }")
        self.horizontalFrame_2.setStyleSheet("#horizontalFrame_2 { border: 1px solid black; border-radius: 10px; }")
        self.horizontalFrame_3.setStyleSheet("#horizontalFrame_3 { border: 1px solid black; border-radius: 10px; }")
        self.horizontalFrame_4.setStyleSheet("#horizontalFrame_4 { border: 1px solid black; border-radius: 10px; }")
        self.horizontalFrame1.setStyleSheet("#horizontalFrame1 { border: 1px solid black; border-radius: 10px; }")
        self.horizontalFrame_21.setStyleSheet("#horizontalFrame_21 { border: 1px solid black; border-radius: 10px; }")
        self.horizontalFrame_31.setStyleSheet("#horizontalFrame_31 { border: 1px solid black; border-radius: 10px; }")
        self.gridFrame_2.setStyleSheet("#gridFrame_2 { border: 1px solid black; border-radius: 10px; }")
        self.gridFrame_3.setStyleSheet("#gridFrame_3 { border: 1px solid black; border-radius: 10px; }")
        self.colorFrame.setStyleSheet("#colorFrame { border: 1px solid black; border-radius: 10px; }")
        self.horizontalFrame_5.setStyleSheet("#horizontalFrame_5 { border: 1px solid black; border-radius: 10px; }")
        self.horizontalFrame2.setStyleSheet("#horizontalFrame2 { border: 1px solid black; border-radius: 10px; }")
        
        self.bgBtn.setIcon(FluentIcon.IMAGE_EXPORT)
        self.openMusicPathBtn.setIcon(FluentIcon.FOLDER)
        self.openLyricPathBtn.setIcon(FluentIcon.FOLDER)
    