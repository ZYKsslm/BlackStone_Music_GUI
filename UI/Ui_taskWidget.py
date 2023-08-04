# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidgetItem, QSizePolicy,
    QWidget)

from qfluentwidgets import ListWidget

class Ui_taskWindow(object):
    def setupUi(self, taskWindow):
        if not taskWindow.objectName():
            taskWindow.setObjectName(u"taskWindow")
        taskWindow.resize(991, 585)
        self.taskWidget = ListWidget(taskWindow)
        self.taskWidget.setObjectName(u"taskWidget")
        self.taskWidget.setGeometry(QRect(20, 80, 951, 481))
        self.bgLabel = QLabel(taskWindow)
        self.bgLabel.setObjectName(u"bgLabel")
        self.bgLabel.setGeometry(QRect(0, 0, 991, 585))
        self.bgLabel.setAlignment(Qt.AlignCenter)
        self.label = QLabel(taskWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 951, 21))
        self.label.setAlignment(Qt.AlignCenter)
        self.bgLabel.raise_()
        self.taskWidget.raise_()
        self.label.raise_()

        self.retranslateUi(taskWindow)

        QMetaObject.connectSlotsByName(taskWindow)
    # setupUi

    def retranslateUi(self, taskWindow):
        taskWindow.setWindowTitle(QCoreApplication.translate("taskWindow", u"Form", None))
        self.bgLabel.setText("")
        self.label.setText(QCoreApplication.translate("taskWindow", u"\u4e0b\u8f7d\u4efb\u52a1\uff1a\u6682\u65e0", None))
    # retranslateUi

