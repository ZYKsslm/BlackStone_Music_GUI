# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

from qfluentwidgets import (ComboBox, LineEdit, Pivot, PrimaryPushButton,
    PushButton, SegmentedWidget, Slider, SwitchButton,
    ToolButton)

class Ui_settingWindow(object):
    def setupUi(self, settingWindow):
        if not settingWindow.objectName():
            settingWindow.setObjectName(u"settingWindow")
        settingWindow.resize(991, 585)
        self.bgLabel = QLabel(settingWindow)
        self.bgLabel.setObjectName(u"bgLabel")
        self.bgLabel.setGeometry(QRect(0, 0, 991, 585))
        self.bgLabel.setAlignment(Qt.AlignCenter)
        self.SegmentedWidget = SegmentedWidget(settingWindow)
        self.SegmentedWidget.setObjectName(u"SegmentedWidget")
        self.SegmentedWidget.setGeometry(QRect(20, 45, 461, 33))
        self.stackedWidget = QStackedWidget(settingWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 90, 951, 481))
        self.stackedWidget.setStyleSheet(u"")
        self.stylePage = QWidget()
        self.stylePage.setObjectName(u"stylePage")
        self.verticalLayoutWidget = QWidget(self.stylePage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 951, 481))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)

        self.horizontalFrame = QFrame(self.verticalLayoutWidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_1 = QLabel(self.horizontalFrame)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout.addWidget(self.label_1)

        self.themeBox = ComboBox(self.horizontalFrame)
        self.themeBox.setObjectName(u"themeBox")

        self.horizontalLayout.addWidget(self.themeBox)


        self.verticalLayout_3.addWidget(self.horizontalFrame)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)

        self.horizontalFrame_3 = QFrame(self.verticalLayoutWidget)
        self.horizontalFrame_3.setObjectName(u"horizontalFrame_3")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalFrame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_14 = QLabel(self.horizontalFrame_3)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_3.addWidget(self.label_14)

        self.opacitySlider = Slider(self.horizontalFrame_3)
        self.opacitySlider.setObjectName(u"opacitySlider")
        self.opacitySlider.setOrientation(Qt.Horizontal)
        self.opacitySlider.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_3.addWidget(self.opacitySlider)


        self.verticalLayout_3.addWidget(self.horizontalFrame_3)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_12)

        self.colorFrame = QFrame(self.verticalLayoutWidget)
        self.colorFrame.setObjectName(u"colorFrame")
        self.horizontalLayout_8 = QHBoxLayout(self.colorFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.colorFrame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)


        self.verticalLayout_3.addWidget(self.colorFrame)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.horizontalFrame_2 = QFrame(self.verticalLayoutWidget)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_13 = QLabel(self.horizontalFrame_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_2.addWidget(self.label_13)

        self.bgBtn = PrimaryPushButton(self.horizontalFrame_2)
        self.bgBtn.setObjectName(u"bgBtn")

        self.horizontalLayout_2.addWidget(self.bgBtn)


        self.verticalLayout_3.addWidget(self.horizontalFrame_2)

        self.bgViewLabel = QLabel(self.verticalLayoutWidget)
        self.bgViewLabel.setObjectName(u"bgViewLabel")

        self.verticalLayout_3.addWidget(self.bgViewLabel)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_13)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_15)

        self.horizontalFrame_4 = QFrame(self.verticalLayoutWidget)
        self.horizontalFrame_4.setObjectName(u"horizontalFrame_4")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_16 = QLabel(self.horizontalFrame_4)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16)

        self.resetBtn = PrimaryPushButton(self.horizontalFrame_4)
        self.resetBtn.setObjectName(u"resetBtn")

        self.horizontalLayout_4.addWidget(self.resetBtn)


        self.verticalLayout_3.addWidget(self.horizontalFrame_4)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_14)

        self.stackedWidget.addWidget(self.stylePage)
        self.filePage = QWidget()
        self.filePage.setObjectName(u"filePage")
        self.verticalLayoutWidget_2 = QWidget(self.filePage)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 951, 481))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridFrame_2 = QFrame(self.verticalLayoutWidget_2)
        self.gridFrame_2.setObjectName(u"gridFrame_2")
        self.gridLayout_2 = QGridLayout(self.gridFrame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.gridFrame_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_19, 5, 1, 1, 1)

        self.musicPathEdit = LineEdit(self.gridFrame_2)
        self.musicPathEdit.setObjectName(u"musicPathEdit")
        self.musicPathEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.musicPathEdit, 2, 1, 1, 1)

        self.musicPathBtn = PushButton(self.gridFrame_2)
        self.musicPathBtn.setObjectName(u"musicPathBtn")

        self.gridLayout_2.addWidget(self.musicPathBtn, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 6, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_17, 3, 1, 1, 1)

        self.openMusicPathBtn = ToolButton(self.gridFrame_2)
        self.openMusicPathBtn.setObjectName(u"openMusicPathBtn")

        self.gridLayout_2.addWidget(self.openMusicPathBtn, 2, 2, 1, 1)


        self.verticalLayout.addWidget(self.gridFrame_2)

        self.gridFrame_3 = QFrame(self.verticalLayoutWidget_2)
        self.gridFrame_3.setObjectName(u"gridFrame_3")
        self.gridLayout_3 = QGridLayout(self.gridFrame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_16, 1, 1, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_18, 5, 1, 1, 1)

        self.openLyricPathBtn = ToolButton(self.gridFrame_3)
        self.openLyricPathBtn.setObjectName(u"openLyricPathBtn")

        self.gridLayout_3.addWidget(self.openLyricPathBtn, 4, 2, 1, 1)

        self.lyricPathEdit = LineEdit(self.gridFrame_3)
        self.lyricPathEdit.setObjectName(u"lyricPathEdit")
        self.lyricPathEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lyricPathEdit, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 7, 1, 1, 1)

        self.lyricPathBtn = PushButton(self.gridFrame_3)
        self.lyricPathBtn.setObjectName(u"lyricPathBtn")

        self.gridLayout_3.addWidget(self.lyricPathBtn, 6, 1, 1, 1)

        self.label_2 = QLabel(self.gridFrame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 2, 1, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_20, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 4, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 4, 3, 1, 1)


        self.verticalLayout.addWidget(self.gridFrame_3)

        self.stackedWidget.addWidget(self.filePage)
        self.downloadPage = QWidget()
        self.downloadPage.setObjectName(u"downloadPage")
        self.verticalLayoutWidget_3 = QWidget(self.downloadPage)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 951, 481))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalFrame1 = QFrame(self.verticalLayoutWidget_3)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.horizontalFrame1)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.threadNumEdit = LineEdit(self.horizontalFrame1)
        self.threadNumEdit.setObjectName(u"threadNumEdit")

        self.horizontalLayout_5.addWidget(self.threadNumEdit)


        self.verticalLayout_2.addWidget(self.horizontalFrame1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.horizontalFrame_31 = QFrame(self.verticalLayoutWidget_3)
        self.horizontalFrame_31.setObjectName(u"horizontalFrame_31")
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalFrame_31)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.horizontalFrame_31)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.randomUaBtn = SwitchButton(self.horizontalFrame_31)
        self.randomUaBtn.setObjectName(u"randomUaBtn")

        self.horizontalLayout_7.addWidget(self.randomUaBtn)


        self.verticalLayout_2.addWidget(self.horizontalFrame_31)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.horizontalFrame_21 = QFrame(self.verticalLayoutWidget_3)
        self.horizontalFrame_21.setObjectName(u"horizontalFrame_21")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalFrame_21)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.horizontalFrame_21)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.selfUaEdit = LineEdit(self.horizontalFrame_21)
        self.selfUaEdit.setObjectName(u"selfUaEdit")

        self.horizontalLayout_6.addWidget(self.selfUaEdit)


        self.verticalLayout_2.addWidget(self.horizontalFrame_21)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.horizontalFrame2 = QFrame(self.verticalLayoutWidget_3)
        self.horizontalFrame2.setObjectName(u"horizontalFrame2")
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.horizontalFrame2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.checkNetworkBtn = SwitchButton(self.horizontalFrame2)
        self.checkNetworkBtn.setObjectName(u"checkNetworkBtn")

        self.horizontalLayout_10.addWidget(self.checkNetworkBtn)


        self.verticalLayout_2.addWidget(self.horizontalFrame2)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_21)

        self.horizontalFrame_5 = QFrame(self.verticalLayoutWidget_3)
        self.horizontalFrame_5.setObjectName(u"horizontalFrame_5")
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalFrame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.horizontalFrame_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.downloadTipBtn = SwitchButton(self.horizontalFrame_5)
        self.downloadTipBtn.setObjectName(u"downloadTipBtn")

        self.horizontalLayout_9.addWidget(self.downloadTipBtn)


        self.verticalLayout_2.addWidget(self.horizontalFrame_5)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_9)

        self.stackedWidget.addWidget(self.downloadPage)

        self.retranslateUi(settingWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(settingWindow)
    # setupUi

    def retranslateUi(self, settingWindow):
        settingWindow.setWindowTitle(QCoreApplication.translate("settingWindow", u"Form", None))
        self.bgLabel.setText("")
        self.label_1.setText(QCoreApplication.translate("settingWindow", u"\u66f4\u6362\u4e3b\u9898", None))
        self.label_14.setText(QCoreApplication.translate("settingWindow", u"\u8c03\u8282\u4e0d\u900f\u660e\u5ea6", None))
        self.label_6.setText(QCoreApplication.translate("settingWindow", u"\u66f4\u6362\u4e3b\u9898\u989c\u8272", None))
        self.label_13.setText(QCoreApplication.translate("settingWindow", u"\u66f4\u6362\u80cc\u666f", None))
        self.bgBtn.setText(QCoreApplication.translate("settingWindow", u"\u9009\u62e9\u56fe\u7247", None))
        self.bgViewLabel.setText("")
        self.label_16.setText(QCoreApplication.translate("settingWindow", u"\u9ed8\u8ba4\u6837\u5f0f", None))
        self.resetBtn.setText(QCoreApplication.translate("settingWindow", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.label.setText(QCoreApplication.translate("settingWindow", u"\u97f3\u4e50\u4fdd\u5b58\u76ee\u5f55", None))
        self.musicPathBtn.setText(QCoreApplication.translate("settingWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.lyricPathBtn.setText(QCoreApplication.translate("settingWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_2.setText(QCoreApplication.translate("settingWindow", u"\u6b4c\u8bcd\u4fdd\u5b58\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.horizontalFrame1.setToolTip(QCoreApplication.translate("settingWindow", u"\u51e0\u4e4e\u7528\u4e0d\u5230\uff0c\u8bf7\u89c6\u8bbe\u5907\u6027\u80fd\u586b\u5199", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("settingWindow", u"\u5927\u6587\u4ef6\u4e0b\u8f7d\u5e76\u53d1\u6570", None))
#if QT_CONFIG(tooltip)
        self.horizontalFrame_31.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("settingWindow", u"\u4f7f\u7528\u968f\u673aUA", None))
        self.randomUaBtn.setText(QCoreApplication.translate("settingWindow", u"\u5173", None))
        self.randomUaBtn.setOnText(QCoreApplication.translate("settingWindow", u"\u5f00", None))
        self.randomUaBtn.setOffText(QCoreApplication.translate("settingWindow", u"\u5173", None))
        self.label_5.setText(QCoreApplication.translate("settingWindow", u"\u81ea\u5b9a\u4e49UA", None))
#if QT_CONFIG(tooltip)
        self.horizontalFrame2.setToolTip(QCoreApplication.translate("settingWindow", u"\u5173\u95ed\u53ef\u52a0\u5feb\u542f\u52a8\u901f\u5ea6", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("settingWindow", u"\u6bcf\u6b21\u542f\u52a8\u524d\u90fd\u68c0\u6d4b\u7f51\u7edc\u8fde\u63a5", None))
        self.checkNetworkBtn.setOnText(QCoreApplication.translate("settingWindow", u"\u5f00", None))
        self.checkNetworkBtn.setOffText(QCoreApplication.translate("settingWindow", u"\u5173", None))
        self.label_7.setText(QCoreApplication.translate("settingWindow", u"\u6bcf\u6b21\u4e0b\u8f7d\u5b8c\u6210\u540e\u603b\u662f\u63d0\u793a", None))
        self.downloadTipBtn.setOnText(QCoreApplication.translate("settingWindow", u"\u5f00", None))
        self.downloadTipBtn.setOffText(QCoreApplication.translate("settingWindow", u"\u5173", None))
    # retranslateUi

