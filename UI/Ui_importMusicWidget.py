# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'importMusicWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QSizePolicy, QSpacerItem, QStackedWidget, QWidget)

from qfluentwidgets import (ComboBox, LineEdit, Pivot, SearchLineEdit,
    SegmentedWidget)

class Ui_importWindow(object):
    def setupUi(self, importWindow):
        if not importWindow.objectName():
            importWindow.setObjectName(u"importWindow")
        importWindow.resize(991, 585)
        self.importLineEdit = SearchLineEdit(importWindow)
        self.importLineEdit.setObjectName(u"importLineEdit")
        self.importLineEdit.setGeometry(QRect(149, 50, 551, 33))
        self.bgLabel = QLabel(importWindow)
        self.bgLabel.setObjectName(u"bgLabel")
        self.bgLabel.setGeometry(QRect(0, 0, 991, 585))
        self.bgLabel.setAlignment(Qt.AlignCenter)
        self.sourceBox = ComboBox(importWindow)
        self.sourceBox.setObjectName(u"sourceBox")
        self.sourceBox.setGeometry(QRect(710, 50, 141, 32))
        icon = QIcon()
        icon.addFile(u"../Image/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.sourceBox.setIcon(icon)
        self.stackedWidget = QStackedWidget(importWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(39, 140, 921, 421))
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.frame = QFrame(self.infoPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 921, 421))
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.nameLabel = QLabel(self.frame)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.nameLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.verticalSpacer)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.createrLabel = QLabel(self.frame)
        self.createrLabel.setObjectName(u"createrLabel")
        self.createrLabel.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.createrLabel)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.contentLabel = QLabel(self.frame)
        self.contentLabel.setObjectName(u"contentLabel")
        self.contentLabel.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.contentLabel)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_7)

        self.numLabel = QLabel(self.frame)
        self.numLabel.setObjectName(u"numLabel")
        self.numLabel.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.numLabel)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_9)

        self.peopleLabel = QLabel(self.frame)
        self.peopleLabel.setObjectName(u"peopleLabel")
        self.peopleLabel.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.peopleLabel)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_11)

        self.tagLabel = QLabel(self.frame)
        self.tagLabel.setObjectName(u"tagLabel")
        self.tagLabel.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.tagLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(6, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(8, QFormLayout.LabelRole, self.verticalSpacer_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(10, QFormLayout.LabelRole, self.verticalSpacer_5)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(12, QFormLayout.LabelRole, self.verticalSpacer_6)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_7)

        self.stackedWidget.addWidget(self.infoPage)
        self.musicPage = QWidget()
        self.musicPage.setObjectName(u"musicPage")
        self.stackedWidget.addWidget(self.musicPage)
        self.SegmentedWidget = SegmentedWidget(importWindow)
        self.SegmentedWidget.setObjectName(u"SegmentedWidget")
        self.SegmentedWidget.setGeometry(QRect(40, 90, 211, 41))
        self.bgLabel.raise_()
        self.importLineEdit.raise_()
        self.sourceBox.raise_()
        self.stackedWidget.raise_()
        self.SegmentedWidget.raise_()

        self.retranslateUi(importWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(importWindow)
    # setupUi

    def retranslateUi(self, importWindow):
        importWindow.setWindowTitle(QCoreApplication.translate("importWindow", u"Form", None))
        self.importLineEdit.setPlaceholderText(QCoreApplication.translate("importWindow", u"\u8bf7\u8f93\u5165\u6b4c\u5355\u94fe\u63a5\u6216ID", None))
        self.bgLabel.setText("")
        self.sourceBox.setText(QCoreApplication.translate("importWindow", u"\u9009\u62e9\u97f3\u6e90", None))
        self.label.setText(QCoreApplication.translate("importWindow", u"\u6b4c\u5355\u540d", None))
        self.nameLabel.setText("")
        self.label_3.setText(QCoreApplication.translate("importWindow", u"\u521b\u5efa\u8005", None))
        self.createrLabel.setText("")
        self.label_5.setText(QCoreApplication.translate("importWindow", u"\u7b80\u4ecb", None))
        self.contentLabel.setText("")
        self.label_7.setText(QCoreApplication.translate("importWindow", u"\u603b\u6b4c\u6570", None))
        self.numLabel.setText("")
        self.label_9.setText(QCoreApplication.translate("importWindow", u"\u6d4f\u89c8\u4eba\u6570", None))
        self.peopleLabel.setText("")
        self.label_11.setText(QCoreApplication.translate("importWindow", u"\u6807\u7b7e", None))
        self.tagLabel.setText("")
    # retranslateUi

