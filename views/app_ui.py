# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/app.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(1200, 900)
        App.setMinimumSize(QtCore.QSize(1200, 900))
        self.centralwidget = QtWidgets.QWidget(App)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.charts = QtWidgets.QVBoxLayout()
        self.charts.setSpacing(20)
        self.charts.setObjectName("charts")
        self.topCharts = QtWidgets.QHBoxLayout()
        self.topCharts.setSpacing(20)
        self.topCharts.setObjectName("topCharts")
        self.leftTopChartFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftTopChartFrame.sizePolicy().hasHeightForWidth())
        self.leftTopChartFrame.setSizePolicy(sizePolicy)
        self.leftTopChartFrame.setMinimumSize(QtCore.QSize(350, 500))
        self.leftTopChartFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftTopChartFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftTopChartFrame.setObjectName("leftTopChartFrame")
        self.topCharts.addWidget(self.leftTopChartFrame)
        self.rightTopChartFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightTopChartFrame.sizePolicy().hasHeightForWidth())
        self.rightTopChartFrame.setSizePolicy(sizePolicy)
        self.rightTopChartFrame.setMinimumSize(QtCore.QSize(350, 500))
        self.rightTopChartFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightTopChartFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightTopChartFrame.setObjectName("rightTopChartFrame")
        self.topCharts.addWidget(self.rightTopChartFrame)
        self.charts.addLayout(self.topCharts)
        self.bottomChartFrame = QtWidgets.QFrame(self.centralwidget)
        self.bottomChartFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottomChartFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottomChartFrame.setObjectName("bottomChartFrame")
        self.charts.addWidget(self.bottomChartFrame)
        self.horizontalLayout.addLayout(self.charts)
        self.tweetStreamFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tweetStreamFrame.sizePolicy().hasHeightForWidth())
        self.tweetStreamFrame.setSizePolicy(sizePolicy)
        self.tweetStreamFrame.setMinimumSize(QtCore.QSize(420, 0))
        self.tweetStreamFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tweetStreamFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tweetStreamFrame.setObjectName("tweetStreamFrame")
        self.horizontalLayout.addWidget(self.tweetStreamFrame)
        App.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(App)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        App.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(App)
        self.statusbar.setObjectName("statusbar")
        App.setStatusBar(self.statusbar)

        self.retranslateUi(App)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "MainWindow"))


