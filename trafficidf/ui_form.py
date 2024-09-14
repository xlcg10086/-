# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_3 = QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.camlabel = QLabel(self.widget_4)
        self.camlabel.setObjectName(u"camlabel")
        font = QFont()
        font.setPointSize(48)
        self.camlabel.setFont(font)
        self.camlabel.setLayoutDirection(Qt.LeftToRight)
        self.camlabel.setAutoFillBackground(False)

        self.verticalLayout_3.addWidget(self.camlabel)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_4 = QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.cam_address = QLineEdit(self.widget_5)
        self.cam_address.setObjectName(u"cam_address")

        self.verticalLayout_4.addWidget(self.cam_address)

        self.widget_2 = QWidget(self.widget_5)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.connectcam = QPushButton(self.widget_2)
        self.connectcam.setObjectName(u"connectcam")

        self.gridLayout.addWidget(self.connectcam, 0, 0, 1, 1)

        self.startcheck = QPushButton(self.widget_2)
        self.startcheck.setObjectName(u"startcheck")

        self.gridLayout.addWidget(self.startcheck, 0, 1, 1, 1)

        self.roadlimit = QComboBox(self.widget_2)
        self.roadlimit.addItem("")
        self.roadlimit.addItem("")
        self.roadlimit.addItem("")
        self.roadlimit.addItem("")
        self.roadlimit.addItem("")
        self.roadlimit.setObjectName(u"roadlimit")

        self.gridLayout.addWidget(self.roadlimit, 0, 2, 1, 1)

        self.speedtop = QLineEdit(self.widget_2)
        self.speedtop.setObjectName(u"speedtop")

        self.gridLayout.addWidget(self.speedtop, 1, 0, 1, 1)

        self.speedtest = QPushButton(self.widget_2)
        self.speedtest.setObjectName(u"speedtest")

        self.gridLayout.addWidget(self.speedtest, 1, 1, 1, 1)

        self.lighlimit = QComboBox(self.widget_2)
        self.lighlimit.addItem("")
        self.lighlimit.addItem("")
        self.lighlimit.addItem("")
        self.lighlimit.addItem("")
        self.lighlimit.setObjectName(u"lighlimit")

        self.gridLayout.addWidget(self.lighlimit, 1, 2, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout_4.addWidget(self.widget_2)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.widget_5)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.widget_4)

        self.verticalLayout_2.setStretch(0, 2)

        self.horizontalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.warmingtext = QTextEdit(self.widget_3)
        self.warmingtext.setObjectName(u"warmingtext")

        self.verticalLayout.addWidget(self.warmingtext)


        self.horizontalLayout.addWidget(self.widget_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4ea4\u901a\u8fdd\u7ae0\u8bc6\u522b", None))
        self.camlabel.setText(QCoreApplication.translate("MainWindow", u"\u94fe\u63a5\u76f8\u673a......", None))
        self.connectcam.setText(QCoreApplication.translate("MainWindow", u"\u94fe\u63a5\u76f8\u673a", None))
        self.startcheck.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u68c0\u6d4b", None))
        self.roadlimit.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e0d\u9650\u884c", None))
        self.roadlimit.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e0a\u4fa7\u9650\u884c", None))
        self.roadlimit.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e0b\u4fa7\u9650\u884c", None))
        self.roadlimit.setItemText(3, QCoreApplication.translate("MainWindow", u"\u7981\u6b62\u53d8\u9053", None))
        self.roadlimit.setItemText(4, "")

        self.speedtop.setInputMask("")
        self.speedtop.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.speedtop.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6570\u5b57\u6574\u6570", None))
        self.speedtest.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u901f\u68c0\u6d4b", None))
        self.lighlimit.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7eff\u706f", None))
        self.lighlimit.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7ea2\u706f", None))
        self.lighlimit.setItemText(2, QCoreApplication.translate("MainWindow", u"\u9ec4\u706f", None))
        self.lighlimit.setItemText(3, "")

    # retranslateUi

