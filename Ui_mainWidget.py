# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QStackedWidget, QTextBrowser,
    QToolButton, QVBoxLayout, QWidget)

class Ui_mainWidget(object):
    def setupUi(self, mainWidget):
        if not mainWidget.objectName():
            mainWidget.setObjectName(u"mainWidget")
        mainWidget.setWindowModality(Qt.NonModal)
        mainWidget.resize(1040, 585)
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        mainWidget.setFont(font)
        icon = QIcon()
        icon.addFile(u"Image/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        mainWidget.setWindowIcon(icon)
        self.iconLabel = QLabel(mainWidget)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setGeometry(QRect(108, 13, 64, 71))
        self.iconLabel.setStyleSheet(u"background-color: transparent")
        self.iconLabel.setPixmap(QPixmap(u"Image/icon.png"))
        self.iconLabel.setAlignment(Qt.AlignCenter)
        self.line = QFrame(mainWidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 80, 241, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(mainWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(280, 20, 20, 541))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.searchLineEdit = QLineEdit(mainWidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setGeometry(QRect(430, 20, 491, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.searchLineEdit.setFont(font1)
        self.searchLineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")
        self.searchBtn = QPushButton(mainWidget)
        self.searchBtn.setObjectName(u"searchBtn")
        self.searchBtn.setGeometry(QRect(940, 20, 71, 41))
        self.searchBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        icon1 = QIcon()
        icon1.addFile(u"Image/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchBtn.setIcon(icon1)
        self.horizontalFrame = QFrame(mainWidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setGeometry(QRect(310, 70, 711, 41))
        self.horizontalFrame.setStyleSheet(u"background-color: transparent")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.source_1 = QRadioButton(self.horizontalFrame)
        self.source_1.setObjectName(u"source_1")
        self.source_1.setStyleSheet(u"background-color: rgba(30, 144, 255, 100);\n"
"color: white")

        self.horizontalLayout_2.addWidget(self.source_1, 0, Qt.AlignHCenter)

        self.source_2 = QRadioButton(self.horizontalFrame)
        self.source_2.setObjectName(u"source_2")
        self.source_2.setStyleSheet(u"background-color: rgba(255, 215, 0, 100);\n"
"color: #3CB371")

        self.horizontalLayout_2.addWidget(self.source_2, 0, Qt.AlignHCenter)

        self.source_3 = QRadioButton(self.horizontalFrame)
        self.source_3.setObjectName(u"source_3")
        self.source_3.setStyleSheet(u"background-color: rgba(255, 215, 0, 100);\n"
"color: #3CB371")

        self.horizontalLayout_2.addWidget(self.source_3, 0, Qt.AlignHCenter)

        self.source_4 = QRadioButton(self.horizontalFrame)
        self.source_4.setObjectName(u"source_4")
        self.source_4.setStyleSheet(u"background-color: rgba(255, 0, 0, 100);\n"
"color: white")

        self.horizontalLayout_2.addWidget(self.source_4, 0, Qt.AlignHCenter)

        self.source_5 = QRadioButton(self.horizontalFrame)
        self.source_5.setObjectName(u"source_5")
        self.source_5.setStyleSheet(u"background-color: rgba(255, 20, 147, 100);\n"
"color: white")

        self.horizontalLayout_2.addWidget(self.source_5, 0, Qt.AlignHCenter)

        self.source_6 = QRadioButton(self.horizontalFrame)
        self.source_6.setObjectName(u"source_6")
        self.source_6.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);\n"
"color: #00BFFF")

        self.horizontalLayout_2.addWidget(self.source_6)

        self.horizontalFrame_2 = QFrame(mainWidget)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalFrame_2.setGeometry(QRect(10, 530, 261, 51))
        self.horizontalFrame_2.setStyleSheet(u"background-color: transparent")
        self.horizontalLayout = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verLabel = QLabel(self.horizontalFrame_2)
        self.verLabel.setObjectName(u"verLabel")
        self.verLabel.setStyleSheet(u"background-color: transparent;")

        self.horizontalLayout.addWidget(self.verLabel)

        self.updateCheckBtn = QPushButton(self.horizontalFrame_2)
        self.updateCheckBtn.setObjectName(u"updateCheckBtn")
        self.updateCheckBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        icon2 = QIcon()
        icon2.addFile(u"Image/update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateCheckBtn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.updateCheckBtn, 0, Qt.AlignRight)

        self.menuStacked = QStackedWidget(mainWidget)
        self.menuStacked.setObjectName(u"menuStacked")
        self.menuStacked.setGeometry(QRect(10, 138, 261, 381))
        self.menuStacked.setStyleSheet(u"background-color: transparent")
        self.taskPage = QWidget()
        self.taskPage.setObjectName(u"taskPage")
        self.taskPage.setStyleSheet(u"background-color: transparent")
        self.taskList = QListWidget(self.taskPage)
        self.taskList.setObjectName(u"taskList")
        self.taskList.setGeometry(QRect(20, 40, 221, 331))
        self.taskList.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")
        self.label_14 = QLabel(self.taskPage)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 0, 221, 41))
        self.label_14.setPixmap(QPixmap(u"Image/task.png"))
        self.label_14.setAlignment(Qt.AlignCenter)
        self.menuStacked.addWidget(self.taskPage)
        self.stylePage = QWidget()
        self.stylePage.setObjectName(u"stylePage")
        self.stylePage.setStyleSheet(u"background-color: transparent")
        self.formFrame = QFrame(self.stylePage)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setGeometry(QRect(0, 0, 261, 331))
        self.formFrame.setStyleSheet(u"background-color: transparent")
        self.formLayout = QFormLayout(self.formFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.FieldRole, self.verticalSpacer_4)

        self.label = QLabel(self.formFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: transparent")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.comboBox = QComboBox(self.formFrame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.FieldRole, self.verticalSpacer_6)

        self.label_2 = QLabel(self.formFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: transparent")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.bgBtn = QPushButton(self.formFrame)
        self.bgBtn.setObjectName(u"bgBtn")
        self.bgBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        icon3 = QIcon()
        icon3.addFile(u"Image/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bgBtn.setIcon(icon3)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.bgBtn)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.FieldRole, self.verticalSpacer_7)

        self.label_3 = QLabel(self.formFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: transparent")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.visSlider = QSlider(self.formFrame)
        self.visSlider.setObjectName(u"visSlider")
        self.visSlider.setStyleSheet(u"background-color: transparent")
        self.visSlider.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.visSlider)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(6, QFormLayout.FieldRole, self.verticalSpacer_8)

        self.formFrame_2 = QFrame(self.stylePage)
        self.formFrame_2.setObjectName(u"formFrame_2")
        self.formFrame_2.setGeometry(QRect(0, 330, 261, 51))
        self.formFrame_2.setStyleSheet(u"background-color: transparent")
        self.formLayout_2 = QFormLayout(self.formFrame_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.resetBtn = QPushButton(self.formFrame_2)
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        icon4 = QIcon()
        icon4.addFile(u"Image/reset.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resetBtn.setIcon(icon4)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.resetBtn)

        self.label_4 = QLabel(self.formFrame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: transparent")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.menuStacked.addWidget(self.stylePage)
        self.filePage = QWidget()
        self.filePage.setObjectName(u"filePage")
        self.filePage.setStyleSheet(u"background-color: transparent")
        self.gridFrame = QFrame(self.filePage)
        self.gridFrame.setObjectName(u"gridFrame")
        self.gridFrame.setGeometry(QRect(0, 0, 261, 381))
        self.gridFrame.setStyleSheet(u"background-color: transparent")
        self.gridLayout = QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.lyricPathBtn = QPushButton(self.gridFrame)
        self.lyricPathBtn.setObjectName(u"lyricPathBtn")
        self.lyricPathBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        icon5 = QIcon()
        icon5.addFile(u"Image/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lyricPathBtn.setIcon(icon5)

        self.gridLayout.addWidget(self.lyricPathBtn, 7, 0, 1, 1)

        self.label_5 = QLabel(self.gridFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: transparent")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.musicPathBtn = QPushButton(self.gridFrame)
        self.musicPathBtn.setObjectName(u"musicPathBtn")
        self.musicPathBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        self.musicPathBtn.setIcon(icon5)

        self.gridLayout.addWidget(self.musicPathBtn, 3, 0, 1, 1)

        self.label_6 = QLabel(self.gridFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: transparent")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1, Qt.AlignHCenter)

        self.lyricOpenBtn = QPushButton(self.gridFrame)
        self.lyricOpenBtn.setObjectName(u"lyricOpenBtn")
        self.lyricOpenBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        icon6 = QIcon()
        icon6.addFile(u"Image/music_folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lyricOpenBtn.setIcon(icon6)

        self.gridLayout.addWidget(self.lyricOpenBtn, 6, 1, 1, 1)

        self.musicOpenBtn = QPushButton(self.gridFrame)
        self.musicOpenBtn.setObjectName(u"musicOpenBtn")
        self.musicOpenBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        self.musicOpenBtn.setIcon(icon6)

        self.gridLayout.addWidget(self.musicOpenBtn, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 8, 0, 1, 1)

        self.musicPathLineEdit = QLineEdit(self.gridFrame)
        self.musicPathLineEdit.setObjectName(u"musicPathLineEdit")
        self.musicPathLineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")

        self.gridLayout.addWidget(self.musicPathLineEdit, 2, 0, 1, 1)

        self.lyricPathLineEdit = QLineEdit(self.gridFrame)
        self.lyricPathLineEdit.setObjectName(u"lyricPathLineEdit")
        self.lyricPathLineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")

        self.gridLayout.addWidget(self.lyricPathLineEdit, 6, 0, 1, 1)

        self.menuStacked.addWidget(self.filePage)
        self.downloadPage = QWidget()
        self.downloadPage.setObjectName(u"downloadPage")
        self.downloadPage.setStyleSheet(u"background-color: transparent")
        self.verticalFrame = QFrame(self.downloadPage)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalFrame.setGeometry(QRect(0, 0, 261, 381))
        self.verticalFrame.setStyleSheet(u"background-color: transparent")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_10)

        self.frame = QFrame(self.verticalFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: transparent")
        self.formLayout_5 = QFormLayout(self.frame)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.threadLineEdit = QLineEdit(self.frame)
        self.threadLineEdit.setObjectName(u"threadLineEdit")
        self.threadLineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.threadLineEdit)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: transparent")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.threadBtn = QPushButton(self.frame)
        self.threadBtn.setObjectName(u"threadBtn")
        self.threadBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.threadBtn)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.randomUaCheck = QCheckBox(self.verticalFrame)
        self.randomUaCheck.setObjectName(u"randomUaCheck")
        self.randomUaCheck.setStyleSheet(u"background-color: transparent")
        self.randomUaCheck.setChecked(True)
        self.randomUaCheck.setTristate(False)

        self.verticalLayout.addWidget(self.randomUaCheck)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_12)

        self.menuStacked.addWidget(self.downloadPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.aboutPage.setStyleSheet(u"background-color: transparent")
        self.formFrame_4 = QFrame(self.aboutPage)
        self.formFrame_4.setObjectName(u"formFrame_4")
        self.formFrame_4.setGeometry(QRect(0, 0, 261, 381))
        self.formFrame_4.setStyleSheet(u"background-color: transparent")
        self.formLayout_6 = QFormLayout(self.formFrame_4)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.projectText = QTextBrowser(self.formFrame_4)
        self.projectText.setObjectName(u"projectText")
        self.projectText.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")

        self.formLayout_6.setWidget(1, QFormLayout.SpanningRole, self.projectText)

        self.licenseText = QTextBrowser(self.formFrame_4)
        self.licenseText.setObjectName(u"licenseText")
        self.licenseText.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")

        self.formLayout_6.setWidget(2, QFormLayout.SpanningRole, self.licenseText)

        self.label_10 = QLabel(self.formFrame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background-color: transparent")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.label_7 = QLabel(self.formFrame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")
        self.label_7.setTextFormat(Qt.RichText)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setOpenExternalLinks(True)

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.label_7)

        self.label_11 = QLabel(self.formFrame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: transparent")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.sponserBtn = QPushButton(self.formFrame_4)
        self.sponserBtn.setObjectName(u"sponserBtn")
        self.sponserBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        icon7 = QIcon()
        icon7.addFile(u"Image/sponsorship.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sponserBtn.setIcon(icon7)

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.sponserBtn)

        self.label_9 = QLabel(self.formFrame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u"Image/about.png"))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.formLayout_6.setWidget(0, QFormLayout.SpanningRole, self.label_9)

        self.menuStacked.addWidget(self.aboutPage)
        self.impBtn = QToolButton(mainWidget)
        self.impBtn.setObjectName(u"impBtn")
        self.impBtn.setEnabled(True)
        self.impBtn.setGeometry(QRect(320, 20, 91, 41))
        self.impBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        icon8 = QIcon()
        icon8.addFile(u"Image/imp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.impBtn.setIcon(icon8)
        self.impBtn.setPopupMode(QToolButton.MenuButtonPopup)
        self.impBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.impBtn.setAutoRaise(False)
        self.bgLabel = QLabel(mainWidget)
        self.bgLabel.setObjectName(u"bgLabel")
        self.bgLabel.setEnabled(True)
        self.bgLabel.setGeometry(QRect(0, 0, 1040, 585))
        self.mainStacked = QStackedWidget(mainWidget)
        self.mainStacked.setObjectName(u"mainStacked")
        self.mainStacked.setGeometry(QRect(309, 110, 711, 451))
        self.mainStacked.setFont(font1)
        self.mainStacked.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")
        self.mainPage = QWidget()
        self.mainPage.setObjectName(u"mainPage")
        self.mainStacked.addWidget(self.mainPage)
        self.searchResPage = QWidget()
        self.searchResPage.setObjectName(u"searchResPage")
        self.musicListWidget = QListWidget(self.searchResPage)
        self.musicListWidget.setObjectName(u"musicListWidget")
        self.musicListWidget.setGeometry(QRect(80, 30, 551, 401))
        font2 = QFont()
        font2.setPointSize(10)
        self.musicListWidget.setFont(font2)
        self.musicListWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
"QListWidget::item {\n"
"        color: black;\n"
"}")
        self.musicListWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.musicListWidget.setViewMode(QListView.ListMode)
        self.label_13 = QLabel(self.searchResPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 0, 711, 30))
        self.label_13.setStyleSheet(u"background-color: transparent")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.verticalFrame1 = QFrame(self.searchResPage)
        self.verticalFrame1.setObjectName(u"verticalFrame1")
        self.verticalFrame1.setGeometry(QRect(-1, 29, 81, 401))
        self.verticalFrame1.setStyleSheet(u"background-color: transparent")
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.qCheck_1 = QCheckBox(self.verticalFrame1)
        self.qCheck_1.setObjectName(u"qCheck_1")

        self.verticalLayout_3.addWidget(self.qCheck_1, 0, Qt.AlignHCenter)

        self.qCheck_2 = QCheckBox(self.verticalFrame1)
        self.qCheck_2.setObjectName(u"qCheck_2")
        self.qCheck_2.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_3.addWidget(self.qCheck_2, 0, Qt.AlignHCenter)

        self.qCheck_3 = QCheckBox(self.verticalFrame1)
        self.qCheck_3.setObjectName(u"qCheck_3")
        self.qCheck_3.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_3.addWidget(self.qCheck_3, 0, Qt.AlignHCenter)

        self.qCheck_4 = QCheckBox(self.verticalFrame1)
        self.qCheck_4.setObjectName(u"qCheck_4")
        self.qCheck_4.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_3.addWidget(self.qCheck_4, 0, Qt.AlignHCenter)

        self.musicDownBtn = QPushButton(self.searchResPage)
        self.musicDownBtn.setObjectName(u"musicDownBtn")
        self.musicDownBtn.setGeometry(QRect(650, 30, 41, 121))
        icon9 = QIcon()
        icon9.addFile(u"Image/download.png", QSize(), QIcon.Normal, QIcon.Off)
        self.musicDownBtn.setIcon(icon9)
        self.lyricDownBtn = QPushButton(self.searchResPage)
        self.lyricDownBtn.setObjectName(u"lyricDownBtn")
        self.lyricDownBtn.setGeometry(QRect(650, 170, 41, 121))
        icon10 = QIcon()
        icon10.addFile(u"Image/lyric.png", QSize(), QIcon.Normal, QIcon.Off)
        self.lyricDownBtn.setIcon(icon10)
        self.musicResClearBtn = QPushButton(self.searchResPage)
        self.musicResClearBtn.setObjectName(u"musicResClearBtn")
        self.musicResClearBtn.setGeometry(QRect(650, 310, 41, 121))
        self.mainStacked.addWidget(self.searchResPage)
        self.importPage = QWidget()
        self.importPage.setObjectName(u"importPage")
        self.musicImportListWidget = QListWidget(self.importPage)
        self.musicImportListWidget.setObjectName(u"musicImportListWidget")
        self.musicImportListWidget.setGeometry(QRect(80, 30, 551, 401))
        self.musicImportListWidget.setFont(font2)
        self.musicImportListWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);\n"
"QListWidget::item {\n"
"        color: black;\n"
"}")
        self.musicImportListWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.musicImportListWidget.setViewMode(QListView.ListMode)
        self.label_15 = QLabel(self.importPage)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 0, 711, 30))
        self.label_15.setStyleSheet(u"background-color: transparent")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.importLyricDownBtn = QPushButton(self.importPage)
        self.importLyricDownBtn.setObjectName(u"importLyricDownBtn")
        self.importLyricDownBtn.setGeometry(QRect(650, 170, 41, 121))
        self.importLyricDownBtn.setIcon(icon10)
        self.importMusicDownBtn = QPushButton(self.importPage)
        self.importMusicDownBtn.setObjectName(u"importMusicDownBtn")
        self.importMusicDownBtn.setGeometry(QRect(650, 30, 41, 121))
        self.importMusicDownBtn.setIcon(icon9)
        self.verticalFrame_2 = QFrame(self.importPage)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        self.verticalFrame_2.setGeometry(QRect(0, 30, 81, 401))
        self.verticalFrame_2.setStyleSheet(u"background-color: transparent")
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.qCheck_5 = QCheckBox(self.verticalFrame_2)
        self.qCheck_5.setObjectName(u"qCheck_5")

        self.verticalLayout_4.addWidget(self.qCheck_5, 0, Qt.AlignHCenter)

        self.qCheck_6 = QCheckBox(self.verticalFrame_2)
        self.qCheck_6.setObjectName(u"qCheck_6")
        self.qCheck_6.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_4.addWidget(self.qCheck_6, 0, Qt.AlignHCenter)

        self.qCheck_7 = QCheckBox(self.verticalFrame_2)
        self.qCheck_7.setObjectName(u"qCheck_7")
        self.qCheck_7.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_4.addWidget(self.qCheck_7, 0, Qt.AlignHCenter)

        self.qCheck_8 = QCheckBox(self.verticalFrame_2)
        self.qCheck_8.setObjectName(u"qCheck_8")
        self.qCheck_8.setStyleSheet(u"background-color: transparent")

        self.verticalLayout_4.addWidget(self.qCheck_8, 0, Qt.AlignHCenter)

        self.importMusicClearBtn = QPushButton(self.importPage)
        self.importMusicClearBtn.setObjectName(u"importMusicClearBtn")
        self.importMusicClearBtn.setGeometry(QRect(650, 310, 41, 121))
        self.mainStacked.addWidget(self.importPage)
        self.updatePage = QWidget()
        self.updatePage.setObjectName(u"updatePage")
        self.label_16 = QLabel(self.updatePage)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 0, 711, 30))
        self.label_16.setStyleSheet(u"background-color: transparent")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.latestInfo = QTextBrowser(self.updatePage)
        self.latestInfo.setObjectName(u"latestInfo")
        self.latestInfo.setGeometry(QRect(80, 30, 551, 331))
        self.updateBtn = QPushButton(self.updatePage)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setGeometry(QRect(80, 400, 551, 31))
        self.updateBtn.setIcon(icon2)
        self.updateLabel = QLabel(self.updatePage)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setGeometry(QRect(80, 366, 551, 21))
        self.updateLabel.setStyleSheet(u"background-color: transparent")
        self.updateLabel.setAlignment(Qt.AlignCenter)
        self.mainStacked.addWidget(self.updatePage)
        self.downloadBtn = QPushButton(mainWidget)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setGeometry(QRect(170, 100, 40, 23))
        self.downloadBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        self.fileBtn = QPushButton(mainWidget)
        self.fileBtn.setObjectName(u"fileBtn")
        self.fileBtn.setGeometry(QRect(124, 100, 40, 23))
        self.fileBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        self.aboutBtn = QPushButton(mainWidget)
        self.aboutBtn.setObjectName(u"aboutBtn")
        self.aboutBtn.setGeometry(QRect(216, 100, 40, 23))
        self.aboutBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        self.styleBtn = QPushButton(mainWidget)
        self.styleBtn.setObjectName(u"styleBtn")
        self.styleBtn.setGeometry(QRect(78, 100, 40, 23))
        self.styleBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        self.taskBtn = QPushButton(mainWidget)
        self.taskBtn.setObjectName(u"taskBtn")
        self.taskBtn.setGeometry(QRect(32, 100, 40, 23))
        self.taskBtn.setStyleSheet(u"background-color: rgba(220, 220, 220, 100);")
        self.bgLabel.raise_()
        self.iconLabel.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.searchLineEdit.raise_()
        self.searchBtn.raise_()
        self.horizontalFrame.raise_()
        self.horizontalFrame_2.raise_()
        self.menuStacked.raise_()
        self.impBtn.raise_()
        self.mainStacked.raise_()
        self.downloadBtn.raise_()
        self.fileBtn.raise_()
        self.aboutBtn.raise_()
        self.styleBtn.raise_()
        self.taskBtn.raise_()

        self.retranslateUi(mainWidget)

        self.menuStacked.setCurrentIndex(0)
        self.mainStacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWidget)
    # setupUi

    def retranslateUi(self, mainWidget):
        mainWidget.setWindowTitle(QCoreApplication.translate("mainWidget", u"BlackStone_Music_GUI", None))
        self.iconLabel.setText("")
        self.searchBtn.setText(QCoreApplication.translate("mainWidget", u"\u641c\u7d22", None))
        self.source_1.setText(QCoreApplication.translate("mainWidget", u"\u9177\u72d7\u97f3\u4e50", None))
        self.source_2.setText(QCoreApplication.translate("mainWidget", u"QQ\u97f3\u4e50", None))
        self.source_3.setText(QCoreApplication.translate("mainWidget", u"QQ\u97f3\u4e50_2", None))
        self.source_4.setText(QCoreApplication.translate("mainWidget", u"\u7f51\u6613\u4e91\u97f3\u4e50", None))
        self.source_5.setText(QCoreApplication.translate("mainWidget", u"\u54aa\u5495\u97f3\u4e50", None))
        self.source_6.setText(QCoreApplication.translate("mainWidget", u"MyFreeMP3", None))
        self.verLabel.setText(QCoreApplication.translate("mainWidget", u"version x.x.x", None))
        self.updateCheckBtn.setText(QCoreApplication.translate("mainWidget", u"\u68c0\u67e5\u66f4\u65b0", None))
#if QT_CONFIG(tooltip)
        self.menuStacked.setToolTip(QCoreApplication.translate("mainWidget", u"\u4e0b\u8f7d\u4efb\u52a1", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText("")
        self.label.setText(QCoreApplication.translate("mainWidget", u"\u66f4\u6362\u4e3b\u9898", None))
        self.label_2.setText(QCoreApplication.translate("mainWidget", u"\u66f4\u6362\u80cc\u666f", None))
        self.bgBtn.setText(QCoreApplication.translate("mainWidget", u"\u9009\u62e9\u56fe\u7247", None))
        self.label_3.setText(QCoreApplication.translate("mainWidget", u"\u8c03\u8282\u900f\u660e\u5ea6", None))
        self.resetBtn.setText(QCoreApplication.translate("mainWidget", u"\u6062\u590d\u9ed8\u8ba4", None))
        self.label_4.setText(QCoreApplication.translate("mainWidget", u"\u9ed8\u8ba4\u6837\u5f0f", None))
        self.lyricPathBtn.setText(QCoreApplication.translate("mainWidget", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_5.setText(QCoreApplication.translate("mainWidget", u"\u97f3\u4e50\u4fdd\u5b58\u76ee\u5f55", None))
        self.musicPathBtn.setText(QCoreApplication.translate("mainWidget", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_6.setText(QCoreApplication.translate("mainWidget", u"\u6b4c\u8bcd\u4fdd\u5b58\u76ee\u5f55", None))
        self.lyricOpenBtn.setText(QCoreApplication.translate("mainWidget", u"\u6253\u5f00", None))
        self.musicOpenBtn.setText(QCoreApplication.translate("mainWidget", u"\u6253\u5f00", None))
#if QT_CONFIG(tooltip)
        self.threadLineEdit.setToolTip(QCoreApplication.translate("mainWidget", u"\u4e0b\u8f7d\u5e76\u53d1\u6570\u5728\u591a\u7ebf\u7a0b\u5e76\u53d1\u4e0b\u8f7d\u65f6\u8d77\u6548\uff0c\u8bf7\u89c6\u673a\u5668\u6027\u80fd\u586b\u5199", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("mainWidget", u"\u66f4\u6539\u4e0b\u8f7d\u5e76\u53d1\u6570", None))
        self.threadBtn.setText(QCoreApplication.translate("mainWidget", u"\u5b8c\u6210", None))
        self.randomUaCheck.setText(QCoreApplication.translate("mainWidget", u"\u4f7f\u7528\u968f\u673aUA", None))
        self.projectText.setHtml(QCoreApplication.translate("mainWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700; font-style:italic;\">BlackStone_Music_GUI</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:700; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:"
                        "0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">Author</span> ZYKsslm</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">Description </span>\u4e00\u4e2a\u7b80\u6613\u7684\u97f3\u4e50\u4e0b\u8f7d\u5de5\u5177\uff0c\u4ec5\u4f9b\u4ea4\u6d41\u5b66\u4e60\u4f7f\u7528\uff01</p></body></html>", None))
        self.licenseText.setMarkdown(QCoreApplication.translate("mainWidget", u"                                 Apache License\n"
"\n"
"                           Version 2.0, January 2004\n"
"\n"
"                        http://www.apache.org/licenses/\n"
"\n"
"   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n"
"\n"
"   1. Definitions.\n"
"\n"
"      \"License\" shall mean the terms and conditions for use, reproduction,\n"
"\n"
"      and distribution as defined by Sections 1 through 9 of this document.\n"
"\n"
"      \"Licensor\" shall mean the copyright owner or entity authorized by\n"
"\n"
"      the copyright owner that is granting the License.\n"
"\n"
"      \"Legal Entity\" shall mean the union of the acting entity and all\n"
"\n"
"      other entities that control, are controlled by, or are under common\n"
"\n"
"      control with that entity. For the purposes of this definition,\n"
"\n"
"      \"control\" means (i) the power, direct or indirect, to cause the\n"
"\n"
"      direction or management of such entity, whether by contract or\n"
"\n"
"      otherwise, or"
                        " (ii) ownership of fifty percent (50%) or more of the\n"
"\n"
"      outstanding shares, or (iii) beneficial ownership of such entity.\n"
"\n"
"      \"You\" (or \"Your\") shall mean an individual or Legal Entity\n"
"\n"
"      exercising permissions granted by this License.\n"
"\n"
"      \"Source\" form shall mean the preferred form for making modifications,\n"
"\n"
"      including but not limited to software source code, documentation\n"
"\n"
"      source, and configuration files.\n"
"\n"
"      \"Object\" form shall mean any form resulting from mechanical\n"
"\n"
"      transformation or translation of a Source form, including but\n"
"\n"
"      not limited to compiled object code, generated documentation,\n"
"\n"
"      and conversions to other media types.\n"
"\n"
"      \"Work\" shall mean the work of authorship, whether in Source or\n"
"\n"
"      Object form, made available under the License, as indicated by a\n"
"\n"
"      copyright notice that is included in or attached to the work\n"
"\n"
"     "
                        " (an example is provided in the Appendix below).\n"
"\n"
"      \"Derivative Works\" shall mean any work, whether in Source or Object\n"
"\n"
"      form, that is based on (or derived from) the Work and for which the\n"
"\n"
"      editorial revisions, annotations, elaborations, or other modifications\n"
"\n"
"      represent, as a whole, an original work of authorship. For the purposes\n"
"\n"
"      of this License, Derivative Works shall not include works that remain\n"
"\n"
"      separable from, or merely link (or bind by name) to the interfaces of,\n"
"\n"
"      the Work and Derivative Works thereof.\n"
"\n"
"      \"Contribution\" shall mean any work of authorship, including\n"
"\n"
"      the original version of the Work and any modifications or additions\n"
"\n"
"      to that Work or Derivative Works thereof, that is intentionally\n"
"\n"
"      submitted to Licensor for inclusion in the Work by the copyright owner\n"
"\n"
"      or by an individual or Legal Entity authorized to submit on behalf of\n"
""
                        "\n"
"      the copyright owner. For the purposes of this definition, \"submitted\"\n"
"\n"
"      means any form of electronic, verbal, or written communication sent\n"
"\n"
"      to the Licensor or its representatives, including but not limited to\n"
"\n"
"      communication on electronic mailing lists, source code control systems,\n"
"\n"
"      and issue tracking systems that are managed by, or on behalf of, the\n"
"\n"
"      Licensor for the purpose of discussing and improving the Work, but\n"
"\n"
"      excluding communication that is conspicuously marked or otherwise\n"
"\n"
"      designated in writing by the copyright owner as \"Not a Contribution.\"\n"
"\n"
"      \"Contributor\" shall mean Licensor and any individual or Legal Entity\n"
"\n"
"      on behalf of whom a Contribution has been received by Licensor and\n"
"\n"
"      subsequently incorporated within the Work.\n"
"\n"
"   2. Grant of Copyright License. Subject to the terms and conditions of\n"
"\n"
"      this License, each Contributor "
                        "hereby grants to You a perpetual,\n"
"\n"
"      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n"
"\n"
"      copyright license to reproduce, prepare Derivative Works of,\n"
"\n"
"      publicly display, publicly perform, sublicense, and distribute the\n"
"\n"
"      Work and such Derivative Works in Source or Object form.\n"
"\n"
"   3. Grant of Patent License. Subject to the terms and conditions of\n"
"\n"
"      this License, each Contributor hereby grants to You a perpetual,\n"
"\n"
"      worldwide, non-exclusive, no-charge, royalty-free, irrevocable\n"
"\n"
"      (except as stated in this section) patent license to make, have made,\n"
"\n"
"      use, offer to sell, sell, import, and otherwise transfer the Work,\n"
"\n"
"      where such license applies only to those patent claims licensable\n"
"\n"
"      by such Contributor that are necessarily infringed by their\n"
"\n"
"      Contribution(s) alone or by combination of their Contribution(s)\n"
"\n"
"      with the Work to which such "
                        "Contribution(s) was submitted. If You\n"
"\n"
"      institute patent litigation against any entity (including a\n"
"\n"
"      cross-claim or counterclaim in a lawsuit) alleging that the Work\n"
"\n"
"      or a Contribution incorporated within the Work constitutes direct\n"
"\n"
"      or contributory patent infringement, then any patent licenses\n"
"\n"
"      granted to You under this License for that Work shall terminate\n"
"\n"
"      as of the date such litigation is filed.\n"
"\n"
"   4. Redistribution. You may reproduce and distribute copies of the\n"
"\n"
"      Work or Derivative Works thereof in any medium, with or without\n"
"\n"
"      modifications, and in Source or Object form, provided that You\n"
"\n"
"      meet the following conditions:\n"
"\n"
"      (a) You must give any other recipients of the Work or\n"
"\n"
"          Derivative Works a copy of this License; and\n"
"\n"
"      (b) You must cause any modified files to carry prominent notices\n"
"\n"
"          stating that You changed t"
                        "he files; and\n"
"\n"
"      (c) You must retain, in the Source form of any Derivative Works\n"
"\n"
"          that You distribute, all copyright, patent, trademark, and\n"
"\n"
"          attribution notices from the Source form of the Work,\n"
"\n"
"          excluding those notices that do not pertain to any part of\n"
"\n"
"          the Derivative Works; and\n"
"\n"
"      (d) If the Work includes a \"NOTICE\" text file as part of its\n"
"\n"
"          distribution, then any Derivative Works that You distribute must\n"
"\n"
"          include a readable copy of the attribution notices contained\n"
"\n"
"          within such NOTICE file, excluding those notices that do not\n"
"\n"
"          pertain to any part of the Derivative Works, in at least one\n"
"\n"
"          of the following places: within a NOTICE text file distributed\n"
"\n"
"          as part of the Derivative Works; within the Source form or\n"
"\n"
"          documentation, if provided along with the Derivative Works; or,\n"
"\n"
"    "
                        "      within a display generated by the Derivative Works, if and\n"
"\n"
"          wherever such third-party notices normally appear. The contents\n"
"\n"
"          of the NOTICE file are for informational purposes only and\n"
"\n"
"          do not modify the License. You may add Your own attribution\n"
"\n"
"          notices within Derivative Works that You distribute, alongside\n"
"\n"
"          or as an addendum to the NOTICE text from the Work, provided\n"
"\n"
"          that such additional attribution notices cannot be construed\n"
"\n"
"          as modifying the License.\n"
"\n"
"      You may add Your own copyright statement to Your modifications and\n"
"\n"
"      may provide additional or different license terms and conditions\n"
"\n"
"      for use, reproduction, or distribution of Your modifications, or\n"
"\n"
"      for any such Derivative Works as a whole, provided Your use,\n"
"\n"
"      reproduction, and distribution of the Work otherwise complies with\n"
"\n"
"      the conditions sta"
                        "ted in this License.\n"
"\n"
"   5. Submission of Contributions. Unless You explicitly state otherwise,\n"
"\n"
"      any Contribution intentionally submitted for inclusion in the Work\n"
"\n"
"      by You to the Licensor shall be under the terms and conditions of\n"
"\n"
"      this License, without any additional terms or conditions.\n"
"\n"
"      Notwithstanding the above, nothing herein shall supersede or modify\n"
"\n"
"      the terms of any separate license agreement you may have executed\n"
"\n"
"      with Licensor regarding such Contributions.\n"
"\n"
"   6. Trademarks. This License does not grant permission to use the trade\n"
"\n"
"      names, trademarks, service marks, or product names of the Licensor,\n"
"\n"
"      except as required for reasonable and customary use in describing the\n"
"\n"
"      origin of the Work and reproducing the content of the NOTICE file.\n"
"\n"
"   7. Disclaimer of Warranty. Unless required by applicable law or\n"
"\n"
"      agreed to in writing, Licensor provide"
                        "s the Work (and each\n"
"\n"
"      Contributor provides its Contributions) on an \"AS IS\" BASIS,\n"
"\n"
"      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or\n"
"\n"
"      implied, including, without limitation, any warranties or conditions\n"
"\n"
"      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A\n"
"\n"
"      PARTICULAR PURPOSE. You are solely responsible for determining the\n"
"\n"
"      appropriateness of using or redistributing the Work and assume any\n"
"\n"
"      risks associated with Your exercise of permissions under this License.\n"
"\n"
"   8. Limitation of Liability. In no event and under no legal theory,\n"
"\n"
"      whether in tort (including negligence), contract, or otherwise,\n"
"\n"
"      unless required by applicable law (such as deliberate and grossly\n"
"\n"
"      negligent acts) or agreed to in writing, shall any Contributor be\n"
"\n"
"      liable to You for damages, including any direct, indirect, special,\n"
"\n"
"      incidental, or con"
                        "sequential damages of any character arising as a\n"
"\n"
"      result of this License or out of the use or inability to use the\n"
"\n"
"      Work (including but not limited to damages for loss of goodwill,\n"
"\n"
"      work stoppage, computer failure or malfunction, or any and all\n"
"\n"
"      other commercial damages or losses), even if such Contributor\n"
"\n"
"      has been advised of the possibility of such damages.\n"
"\n"
"   9. Accepting Warranty or Additional Liability. While redistributing\n"
"\n"
"      the Work or Derivative Works thereof, You may choose to offer,\n"
"\n"
"      and charge a fee for, acceptance of support, warranty, indemnity,\n"
"\n"
"      or other liability obligations and/or rights consistent with this\n"
"\n"
"      License. However, in accepting such obligations, You may act only\n"
"\n"
"      on Your own behalf and on Your sole responsibility, not on behalf\n"
"\n"
"      of any other Contributor, and only if You agree to indemnify,\n"
"\n"
"      defend, and hold ea"
                        "ch Contributor harmless for any liability\n"
"\n"
"      incurred by, or claims asserted against, such Contributor by reason\n"
"\n"
"      of your accepting any such warranty or additional liability.\n"
"\n"
"   END OF TERMS AND CONDITIONS\n"
"\n"
"   APPENDIX: How to apply the Apache License to your work.\n"
"\n"
"      To apply the Apache License to your work, attach the following\n"
"\n"
"      boilerplate notice, with the fields enclosed by brackets \"[]\"\n"
"\n"
"      replaced with your own identifying information. (Don't include\n"
"\n"
"      the brackets!)  The text should be enclosed in the appropriate\n"
"\n"
"      comment syntax for the file format. We also recommend that a\n"
"\n"
"      file or class name and description of purpose be included on the\n"
"\n"
"      same \"printed page\" as the copyright notice for easier\n"
"\n"
"      identification within third-party archives.\n"
"\n"
"   Copyright [yyyy] [name of copyright owner]\n"
"\n"
"   Licensed under the Apache License, Version 2.0 (t"
                        "he \"License\");\n"
"\n"
"   you may not use this file except in compliance with the License.\n"
"\n"
"   You may obtain a copy of the License at\n"
"\n"
"       http://www.apache.org/licenses/LICENSE-2.0\n"
"\n"
"   Unless required by applicable law or agreed to in writing, software\n"
"\n"
"   distributed under the License is distributed on an \"AS IS\" BASIS,\n"
"\n"
"   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n"
"\n"
"   See the License for the specific language governing permissions and\n"
"\n"
"   limitations under the License.\n"
"\n"
"", None))
        self.licenseText.setHtml(QCoreApplication.translate("mainWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">                                 Apache License</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">                           Version 2.0, January 2004</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0"
                        "px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">                        http://www.apache.org/licenses/</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   1. Definitions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -"
                        "qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      &quot;License&quot; shall mean the terms and conditions for use, reproduction,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      and distribution as defined by Sections 1 through 9 of this document.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      &quot;Licensor&quot; shall mean the copyright owner or entity authorized by</span></p>\n"
"<p style=\" margin-top:0px; margin"
                        "-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      the copyright owner that is granting the License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      &quot;Legal Entity&quot; shall mean the union of the acting entity and all</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      other entities that control, are controlled by, or are under common</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      control w"
                        "ith that entity. For the purposes of this definition,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      &quot;control&quot; means (i) the power, direct or indirect, to cause the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      direction or management of such entity, whether by contract or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      otherwise, or (ii) ownership of fifty percent (50%) or more of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      outstanding shares, or (iii) beneficial ownership of such entity.</span"
                        "></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      &quot;You&quot; (or &quot;Your&quot;) shall mean an individual or Legal Entity</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      exercising permissions granted by this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      &quot;Source&quot; form shall"
                        " mean the preferred form for making modifications,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      including but not limited to software source code, documentation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      source, and configuration files.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      &quot;Object&quot; form shall mean any form resulting from mechanical</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      transformation or translation of a Source form, including but</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      not limited to compiled object code, generated documentation,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      and conversions to other media types.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      &quot;Work&quot; shall mean the work of authorship, whether in Source or</span></p>\n"
"<p style=\""
                        " margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      Object form, made available under the License, as indicated by a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      copyright notice that is included in or attached to the work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      (an example is provided in the Appendix below).</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      &quot"
                        ";Derivative Works&quot; shall mean any work, whether in Source or Object</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      form, that is based on (or derived from) the Work and for which the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      editorial revisions, annotations, elaborations, or other modifications</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      represent, as a whole, an original work of authorship. For the purposes</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      of this License, Derivative Works shall not i"
                        "nclude works that remain</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      separable from, or merely link (or bind by name) to the interfaces of,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      the Work and Derivative Works thereof.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      &quot;Contribution&quot; shall mean any work of authorship, including</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-"
                        "indent:0px;\"><span style=\" font-size:6pt;\">      the original version of the Work and any modifications or additions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      to that Work or Derivative Works thereof, that is intentionally</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      submitted to Licensor for inclusion in the Work by the copyright owner</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      or by an individual or Legal Entity authorized to submit on behalf of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      the "
                        "copyright owner. For the purposes of this definition, &quot;submitted&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      means any form of electronic, verbal, or written communication sent</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      to the Licensor or its representatives, including but not limited to</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      communication on electronic mailing lists, source code control systems,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      and issue tracking systems that are managed "
                        "by, or on behalf of, the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      Licensor for the purpose of discussing and improving the Work, but</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      excluding communication that is conspicuously marked or otherwise</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      designated in writing by the copyright owner as &quot;Not a Contribution.&quot;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      &quot;Contributor&quot; shall mean Licensor and any individual or Legal Entity</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      on behalf of whom a Contribution has been received by Licensor and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      subsequently incorporated within the Work.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   2. Grant of Copyright License. Subject to the terms and "
                        "conditions of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      this License, each Contributor hereby grants to You a perpetual,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      worldwide, non-exclusive, no-charge, royalty-free, irrevocable</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      copyright license to reproduce, prepare Derivative Works of,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      publicly display, publicly perform, sublicense, and distribute the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0p"
                        "x; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      Work and such Derivative Works in Source or Object form.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   3. Grant of Patent License. Subject to the terms and conditions of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      this License, each Contributor hereby grants to You a perpetual,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      worldwide, non-exclusive, "
                        "no-charge, royalty-free, irrevocable</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      (except as stated in this section) patent license to make, have made,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      use, offer to sell, sell, import, and otherwise transfer the Work,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      where such license applies only to those patent claims licensable</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      by such Contributor that are necessarily infringed by their</span></p>\n"
"<p style=\" ma"
                        "rgin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      Contribution(s) alone or by combination of their Contribution(s)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      with the Work to which such Contribution(s) was submitted. If You</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      institute patent litigation against any entity (including a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      cross-claim or counterclaim in a lawsuit) alleging that the Work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      or a Contribution incorporated within the Work constitutes direct</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      or contributory patent infringement, then any patent licenses</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      granted to You under this License for that Work shall terminate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      as of the date such litigation is filed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p styl"
                        "e=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   4. Redistribution. You may reproduce and distribute copies of the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      Work or Derivative Works thereof in any medium, with or without</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      modifications, and in Source or Object form, provided that You</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      meet the following conditions:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bloc"
                        "k-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      (a) You must give any other recipients of the Work or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          Derivative Works a copy of this License; and</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      (b) You must cause any modified files to carry prominent notices</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><span style=\" font-size:6pt;\">          stating that You changed the files; and</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      (c) You must retain, in the Source form of any Derivative Works</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          that You distribute, all copyright, patent, trademark, and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          attribution notices from the Source form of the Work,</span></p>\n"
"<p style=\" margin-top"
                        ":0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          excluding those notices that do not pertain to any part of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          the Derivative Works; and</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      (d) If the Work includes a &quot;NOTICE&quot; text file as part of its</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          distribution, then any"
                        " Derivative Works that You distribute must</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          include a readable copy of the attribution notices contained</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          within such NOTICE file, excluding those notices that do not</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          pertain to any part of the Derivative Works, in at least one</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          of the following places: within a NOTICE text file distributed</span></p>\n"
"<p style="
                        "\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          as part of the Derivative Works; within the Source form or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          documentation, if provided along with the Derivative Works; or,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          within a display generated by the Derivative Works, if and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          wherever such third-party notices normally appear. The contents</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          of the NOTICE file are for informational purposes only and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          do not modify the License. You may add Your own attribution</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          notices within Derivative Works that You distribute, alongside</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          or as an addendum to the NOTICE text from the Work, provided</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"
                        "6pt;\">          that such additional attribution notices cannot be construed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">          as modifying the License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      You may add Your own copyright statement to Your modifications and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      may provide additional or different license terms and conditions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      for use, reproduction, or distribution of Your modifications, or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      for any such Derivative Works as a whole, provided Your use,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      reproduction, and distribution of the Work otherwise complies with</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      the conditions stated in this License.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></"
                        "p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   5. Submission of Contributions. Unless You explicitly state otherwise,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      any Contribution intentionally submitted for inclusion in the Work</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      by You to the Licensor shall be under the terms and conditions of</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      this License, without any additional terms or conditions.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      Notwithstanding the above, nothing herein shall supersede or modify</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      the terms of any separate license agreement you may have executed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      with Licensor regarding such Contributions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   6. Trademarks. This License does not grant permission to"
                        " use the trade</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      names, trademarks, service marks, or product names of the Licensor,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      except as required for reasonable and customary use in describing the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      origin of the Work and reproducing the content of the NOTICE file.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-"
                        "indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   7. Disclaimer of Warranty. Unless required by applicable law or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      agreed to in writing, Licensor provides the Work (and each</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      Contributor provides its Contributions) on an &quot;AS IS&quot; BASIS,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      implied"
                        ", including, without limitation, any warranties or conditions</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      PARTICULAR PURPOSE. You are solely responsible for determining the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      appropriateness of using or redistributing the Work and assume any</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      risks associated with Your exercise of permissions under this License.<"
                        "/span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   8. Limitation of Liability. In no event and under no legal theory,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      whether in tort (including negligence), contract, or otherwise,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      unless required by applicable law (such as deliberate and grossly</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                        "\"><span style=\" font-size:6pt;\">      negligent acts) or agreed to in writing, shall any Contributor be</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      liable to You for damages, including any direct, indirect, special,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      incidental, or consequential damages of any character arising as a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      result of this License or out of the use or inability to use the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      Work (including but no"
                        "t limited to damages for loss of goodwill,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      work stoppage, computer failure or malfunction, or any and all</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      other commercial damages or losses), even if such Contributor</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      has been advised of the possibility of such damages.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block"
                        "-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   9. Accepting Warranty or Additional Liability. While redistributing</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      the Work or Derivative Works thereof, You may choose to offer,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      and charge a fee for, acceptance of support, warranty, indemnity,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      or other liability obligations and/or rights consistent with this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      L"
                        "icense. However, in accepting such obligations, You may act only</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      on Your own behalf and on Your sole responsibility, not on behalf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      of any other Contributor, and only if You agree to indemnify,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      defend, and hold each Contributor harmless for any liability</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      incurred by, or claims asserted against, such Contributor by reason</span><"
                        "/p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      of your accepting any such warranty or additional liability.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   END OF TERMS AND CONDITIONS</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   APPENDIX: How to apply the Apache License to your work.</span></p>\n"
"<p s"
                        "tyle=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      To apply the Apache License to your work, attach the following</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      boilerplate notice, with the fields enclosed by brackets &quot;[]&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      replaced with your own identifying information. (Don't include</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style="
                        "\" font-size:6pt;\">      the brackets!)  The text should be enclosed in the appropriate</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      comment syntax for the file format. We also recommend that a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      file or class name and description of purpose be included on the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      same &quot;printed page&quot; as the copyright notice for easier</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">      identification within third-party archives.</span"
                        "></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   Copyright [yyyy] [name of copyright owner]</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   you may not use this file except in compliance w"
                        "ith the License.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   You may obtain a copy of the License at</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">       http://www.apache.org/licenses/LICENSE-2.0</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:6pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   Unless required by applicable law or agreed to in writin"
                        "g, software</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   distributed under the License is distributed on an &quot;AS IS&quot; BASIS,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   See the License for the specific language governing permissions and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">   limitations under the License.</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("mainWidget", u"\u9879\u76ee\u4ed3\u5e93", None))
        self.label_7.setText(QCoreApplication.translate("mainWidget", u"<html><head/><body><p><a href=\"https://github.com/ZYKsslm/BlackStone_Music_GUI\"><span style=\" text-decoration: underline; color:#0000ff;\">\u524d\u5f80Github</span></a></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("mainWidget", u"\u9879\u76ee\u6253\u8d4f", None))
        self.sponserBtn.setText(QCoreApplication.translate("mainWidget", u"\u6253\u8d4f\u9879\u76ee", None))
        self.label_9.setText("")
        self.impBtn.setText(QCoreApplication.translate("mainWidget", u"\u5bfc\u5165\u6b4c\u5355", None))
        self.bgLabel.setText("")
        self.label_13.setText(QCoreApplication.translate("mainWidget", u"\u641c\u7d22\u7ed3\u679c", None))
        self.qCheck_1.setText(QCoreApplication.translate("mainWidget", u"\u6bcd\u5e26", None))
        self.qCheck_2.setText(QCoreApplication.translate("mainWidget", u"\u65e0\u635f", None))
        self.qCheck_3.setText(QCoreApplication.translate("mainWidget", u"HQ", None))
        self.qCheck_4.setText(QCoreApplication.translate("mainWidget", u"\u6807\u51c6", None))
        self.musicDownBtn.setText(QCoreApplication.translate("mainWidget", u"\u4e0b\n"
"\u8f7d\n"
"\u97f3\n"
"\u4e50", None))
#if QT_CONFIG(tooltip)
        self.lyricDownBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lyricDownBtn.setText(QCoreApplication.translate("mainWidget", u"\u4e0b\n"
"\u8f7d\n"
"\u6b4c\n"
"\u8bcd", None))
        self.musicResClearBtn.setText(QCoreApplication.translate("mainWidget", u"\u6e05\n"
"\u7a7a", None))
        self.label_15.setText(QCoreApplication.translate("mainWidget", u"\u5bfc\u5165\u7ed3\u679c", None))
        self.importLyricDownBtn.setText(QCoreApplication.translate("mainWidget", u"\u4e0b\n"
"\u8f7d\n"
"\u6b4c\n"
"\u8bcd", None))
        self.importMusicDownBtn.setText(QCoreApplication.translate("mainWidget", u"\u4e0b\n"
"\u8f7d\n"
"\u97f3\n"
"\u4e50", None))
        self.qCheck_5.setText(QCoreApplication.translate("mainWidget", u"\u6bcd\u5e26", None))
        self.qCheck_6.setText(QCoreApplication.translate("mainWidget", u"\u65e0\u635f", None))
        self.qCheck_7.setText(QCoreApplication.translate("mainWidget", u"HQ", None))
        self.qCheck_8.setText(QCoreApplication.translate("mainWidget", u"\u6807\u51c6", None))
        self.importMusicClearBtn.setText(QCoreApplication.translate("mainWidget", u"\u6e05\n"
"\u7a7a", None))
        self.label_16.setText(QCoreApplication.translate("mainWidget", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.updateBtn.setText(QCoreApplication.translate("mainWidget", u"\u66f4\u65b0", None))
        self.updateLabel.setText("")
        self.downloadBtn.setText(QCoreApplication.translate("mainWidget", u"\u4e0b\u8f7d", None))
        self.fileBtn.setText(QCoreApplication.translate("mainWidget", u"\u6587\u4ef6", None))
        self.aboutBtn.setText(QCoreApplication.translate("mainWidget", u"\u5173\u4e8e", None))
        self.styleBtn.setText(QCoreApplication.translate("mainWidget", u"\u6837\u5f0f", None))
        self.taskBtn.setText(QCoreApplication.translate("mainWidget", u"\u4efb\u52a1", None))
    # retranslateUi

