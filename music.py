# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'music.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SimpleMusiPlayer(object):
    def setupUi(self, SimpleMusiPlayer):
        SimpleMusiPlayer.setObjectName("SimpleMusiPlayer")
        SimpleMusiPlayer.resize(717, 481)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/images/CD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SimpleMusiPlayer.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SimpleMusiPlayer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 127);\n"
"selection-background-color: rgb(255, 255, 82);\n"
"selection-color: rgb(66, 66, 66);")
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setStyleSheet("background-color: rgb(222, 222, 222);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.volumeSlider = QtWidgets.QSlider(self.frame_5)
        self.volumeSlider.setMinimumSize(QtCore.QSize(250, 0))
        self.volumeSlider.setMaximumSize(QtCore.QSize(250, 16777215))
        self.volumeSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setSingleStep(1)
        self.volumeSlider.setProperty("value", 50)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setInvertedAppearance(False)
        self.volumeSlider.setInvertedControls(False)
        self.volumeSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_4.addWidget(self.volumeSlider)
        self.volume_label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.volume_label.setFont(font)
        self.volume_label.setObjectName("volume_label")
        self.horizontalLayout_4.addWidget(self.volume_label)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_2 = QtWidgets.QFrame(self.frame_6)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addWidget(self.frame)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.start_time_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.start_time_label.setFont(font)
        self.start_time_label.setObjectName("start_time_label")
        self.horizontalLayout_3.addWidget(self.start_time_label)
        self.musicSlider = QtWidgets.QSlider(self.frame_4)
        self.musicSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.musicSlider.setOrientation(QtCore.Qt.Horizontal)
        self.musicSlider.setObjectName("musicSlider")
        self.horizontalLayout_3.addWidget(self.musicSlider)
        self.end_time_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.end_time_label.setFont(font)
        self.end_time_label.setObjectName("end_time_label")
        self.horizontalLayout_3.addWidget(self.end_time_label)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_6)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.playpushButton = QtWidgets.QPushButton(self.frame_3)
        self.playpushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playpushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("utils/images/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playpushButton.setIcon(icon1)
        self.playpushButton.setIconSize(QtCore.QSize(24, 24))
        self.playpushButton.setFlat(True)
        self.playpushButton.setObjectName("playpushButton")
        self.horizontalLayout_2.addWidget(self.playpushButton)
        self.pausepushButton = QtWidgets.QPushButton(self.frame_3)
        self.pausepushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pausepushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/images/Pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pausepushButton.setIcon(icon2)
        self.pausepushButton.setIconSize(QtCore.QSize(24, 24))
        self.pausepushButton.setFlat(True)
        self.pausepushButton.setObjectName("pausepushButton")
        self.horizontalLayout_2.addWidget(self.pausepushButton)
        self.stoppushButton = QtWidgets.QPushButton(self.frame_3)
        self.stoppushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stoppushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/images/Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stoppushButton.setIcon(icon3)
        self.stoppushButton.setIconSize(QtCore.QSize(24, 24))
        self.stoppushButton.setFlat(True)
        self.stoppushButton.setObjectName("stoppushButton")
        self.horizontalLayout_2.addWidget(self.stoppushButton)
        self.previouspushButton = QtWidgets.QPushButton(self.frame_3)
        self.previouspushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previouspushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/images/Previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previouspushButton.setIcon(icon4)
        self.previouspushButton.setIconSize(QtCore.QSize(24, 24))
        self.previouspushButton.setFlat(True)
        self.previouspushButton.setObjectName("previouspushButton")
        self.horizontalLayout_2.addWidget(self.previouspushButton)
        self.nextpushButton = QtWidgets.QPushButton(self.frame_3)
        self.nextpushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextpushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/images/Next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextpushButton.setIcon(icon5)
        self.nextpushButton.setIconSize(QtCore.QSize(24, 24))
        self.nextpushButton.setFlat(True)
        self.nextpushButton.setObjectName("nextpushButton")
        self.horizontalLayout_2.addWidget(self.nextpushButton)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_6)
        SimpleMusiPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SimpleMusiPlayer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menuMenu.setFont(font)
        self.menuMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuMenu.setObjectName("menuMenu")
        SimpleMusiPlayer.setMenuBar(self.menubar)
        self.actionAdd_Songs = QtWidgets.QAction(SimpleMusiPlayer)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/images/Create.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Songs.setIcon(icon6)
        self.actionAdd_Songs.setObjectName("actionAdd_Songs")
        self.actionRemove_Selected = QtWidgets.QAction(SimpleMusiPlayer)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/img/images/Remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_Selected.setIcon(icon7)
        self.actionRemove_Selected.setObjectName("actionRemove_Selected")
        self.actionRemove_All = QtWidgets.QAction(SimpleMusiPlayer)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/images/Delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_All.setIcon(icon8)
        self.actionRemove_All.setObjectName("actionRemove_All")
        self.menuMenu.addAction(self.actionAdd_Songs)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionRemove_Selected)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionRemove_All)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(SimpleMusiPlayer)
        QtCore.QMetaObject.connectSlotsByName(SimpleMusiPlayer)

    def retranslateUi(self, SimpleMusiPlayer):
        _translate = QtCore.QCoreApplication.translate
        SimpleMusiPlayer.setWindowTitle(_translate("SimpleMusiPlayer", "Simple Music Player"))
        self.label.setText(_translate("SimpleMusiPlayer", "Volume:"))
        self.volume_label.setText(_translate("SimpleMusiPlayer", "50"))
        self.start_time_label.setText(_translate("SimpleMusiPlayer", "00:00:00"))
        self.end_time_label.setText(_translate("SimpleMusiPlayer", "00:00:00"))
        self.playpushButton.setToolTip(_translate("SimpleMusiPlayer", "Play"))
        self.pausepushButton.setToolTip(_translate("SimpleMusiPlayer", "Pause/Unpause"))
        self.stoppushButton.setToolTip(_translate("SimpleMusiPlayer", "Stop"))
        self.previouspushButton.setToolTip(_translate("SimpleMusiPlayer", "Previous"))
        self.nextpushButton.setToolTip(_translate("SimpleMusiPlayer", "Next"))
        self.menuMenu.setTitle(_translate("SimpleMusiPlayer", "Menu"))
        self.actionAdd_Songs.setText(_translate("SimpleMusiPlayer", "Add Songs"))
        self.actionAdd_Songs.setToolTip(_translate("SimpleMusiPlayer", "Add songs to music player"))
        self.actionAdd_Songs.setShortcut(_translate("SimpleMusiPlayer", "Alt+A"))
        self.actionRemove_Selected.setText(_translate("SimpleMusiPlayer", "Remove Selected"))
        self.actionRemove_Selected.setToolTip(_translate("SimpleMusiPlayer", "Remove Selected Song"))
        self.actionRemove_Selected.setShortcut(_translate("SimpleMusiPlayer", "Del"))
        self.actionRemove_All.setText(_translate("SimpleMusiPlayer", "Remove All"))
        self.actionRemove_All.setToolTip(_translate("SimpleMusiPlayer", "Remove All Songs"))
        self.actionRemove_All.setShortcut(_translate("SimpleMusiPlayer", "Alt+Del"))
import music_res_rc
