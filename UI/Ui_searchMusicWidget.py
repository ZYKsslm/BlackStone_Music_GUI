# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchMusicWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

from qfluentwidgets import (ComboBox, LineEdit, SearchLineEdit)

class Ui_searchWindow(object):
    def setupUi(self, searchWindow):
        if not searchWindow.objectName():
            searchWindow.setObjectName(u"searchWindow")
        searchWindow.resize(991, 585)
        self.bgLabel = QLabel(searchWindow)
        self.bgLabel.setObjectName(u"bgLabel")
        self.bgLabel.setGeometry(QRect(0, 0, 991, 585))
        self.bgLabel.setAlignment(Qt.AlignCenter)
        self.searchLineEdit = SearchLineEdit(searchWindow)
        self.searchLineEdit.setObjectName(u"searchLineEdit")
        self.searchLineEdit.setGeometry(QRect(149, 50, 551, 33))
        self.sourceBox = ComboBox(searchWindow)
        self.sourceBox.setObjectName(u"sourceBox")
        self.sourceBox.setGeometry(QRect(710, 50, 141, 32))
        icon = QIcon()
        icon.addFile(u"../Image/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.sourceBox.setIcon(icon)

        self.retranslateUi(searchWindow)

        QMetaObject.connectSlotsByName(searchWindow)
    # setupUi

    def retranslateUi(self, searchWindow):
        searchWindow.setWindowTitle("")
        self.bgLabel.setText("")
        self.searchLineEdit.setPlaceholderText(QCoreApplication.translate("searchWindow", u"\u8bf7\u8f93\u5165\u97f3\u4e50\u4fe1\u606f", None))
        self.sourceBox.setText(QCoreApplication.translate("searchWindow", u"\u9009\u62e9\u97f3\u6e90", None))
    # retranslateUi

