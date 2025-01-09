# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rmusic.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SimpleMusiPlayer(object):
    def setupUi(self, SimpleMusiPlayer):
        SimpleMusiPlayer.setObjectName("SimpleMusiPlayer")
        SimpleMusiPlayer.resize(979, 685)
        SimpleMusiPlayer.setMaximumSize(QtCore.QSize(1000, 700))
        SimpleMusiPlayer.setSizeIncrement(QtCore.QSize(1000, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/images/CD.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SimpleMusiPlayer.setWindowIcon(icon)
        SimpleMusiPlayer.setLayoutDirection(QtCore.Qt.LeftToRight)
        SimpleMusiPlayer.setAutoFillBackground(False)
        SimpleMusiPlayer.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(SimpleMusiPlayer)
        self.centralwidget.setObjectName("centralwidget")
        self.menuAdd_Songs = QtWidgets.QFrame(self.centralwidget)
        self.menuAdd_Songs.setGeometry(QtCore.QRect(0, 0, 981, 681))
        self.menuAdd_Songs.setStyleSheet("background-color: rgb(56, 56, 56);")
        self.menuAdd_Songs.setObjectName("menuAdd_Songs")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.menuAdd_Songs)
        self.horizontalLayout_5.setContentsMargins(25, 25, 25, 25)
        self.horizontalLayout_5.setSpacing(25)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.menuAdd_Songs)
        self.listWidget.setMinimumSize(QtCore.QSize(456, 631))
        self.listWidget.setMaximumSize(QtCore.QSize(456, 631))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setStyleSheet("background-color: rgb(66, 66, 66);\n"
"color: rgb(240, 240, 240);\n"
"selection-background-color: rgb(255, 255, 82);\n"
"selection-color: rgb(66, 66, 66);")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_5.addWidget(self.listWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.photo_music = QtWidgets.QLabel(self.menuAdd_Songs)
        self.photo_music.setEnabled(True)
        self.photo_music.setMaximumSize(QtCore.QSize(400, 400))
        self.photo_music.setSizeIncrement(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.photo_music.setFont(font)
        self.photo_music.setTabletTracking(False)
        self.photo_music.setAutoFillBackground(False)
        self.photo_music.setText("")
        self.photo_music.setTextFormat(QtCore.Qt.AutoText)
        self.photo_music.setPixmap(QtGui.QPixmap(":/img/images/1679569032_bogatyr-club-p-rasteniya-na-chernom-fone-instagram-3.jpg"))
        self.photo_music.setScaledContents(True)
        self.photo_music.setWordWrap(False)
        self.photo_music.setObjectName("photo_music")
        self.verticalLayout_2.addWidget(self.photo_music, 0, QtCore.Qt.AlignHCenter)
        self.frame_4 = QtWidgets.QFrame(self.menuAdd_Songs)
        self.frame_4.setMaximumSize(QtCore.QSize(500, 28))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.musicSlider = QtWidgets.QSlider(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.musicSlider.sizePolicy().hasHeightForWidth())
        self.musicSlider.setSizePolicy(sizePolicy)
        self.musicSlider.setMinimumSize(QtCore.QSize(300, 0))
        self.musicSlider.setMaximumSize(QtCore.QSize(400, 50))
        self.musicSlider.setSizeIncrement(QtCore.QSize(0, 0))
        self.musicSlider.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.musicSlider.setStyleSheet("")
        self.musicSlider.setTracking(True)
        self.musicSlider.setOrientation(QtCore.Qt.Horizontal)
        self.musicSlider.setObjectName("musicSlider")
        self.horizontalLayout_3.addWidget(self.musicSlider)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.menuAdd_Songs)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(200, 40))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(9, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previouspushButton = QtWidgets.QPushButton(self.frame_3)
        self.previouspushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previouspushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("static/utils/images/Previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previouspushButton.setIcon(icon1)
        self.previouspushButton.setIconSize(QtCore.QSize(24, 24))
        self.previouspushButton.setFlat(True)
        self.previouspushButton.setObjectName("previouspushButton")
        self.horizontalLayout_2.addWidget(self.previouspushButton)
        self.playpushButton = QtWidgets.QPushButton(self.frame_3)
        self.playpushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playpushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("static/utils/images/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playpushButton.setIcon(icon2)
        self.playpushButton.setIconSize(QtCore.QSize(24, 24))
        self.playpushButton.setFlat(True)
        self.playpushButton.setObjectName("playpushButton")
        self.horizontalLayout_2.addWidget(self.playpushButton)
        self.pausepushButton = QtWidgets.QPushButton(self.frame_3)
        self.pausepushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pausepushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("static/utils/images/Pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pausepushButton.setIcon(icon3)
        self.pausepushButton.setIconSize(QtCore.QSize(24, 24))
        self.pausepushButton.setFlat(True)
        self.pausepushButton.setObjectName("pausepushButton")
        self.horizontalLayout_2.addWidget(self.pausepushButton)
        self.menuRemove_Songs = QtWidgets.QPushButton(self.frame_3)
        self.menuRemove_Songs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuRemove_Songs.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("static/utils/images/Remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuRemove_Songs.setIcon(icon4)
        self.menuRemove_Songs.setIconSize(QtCore.QSize(24, 24))
        self.menuRemove_Songs.setFlat(True)
        self.menuRemove_Songs.setObjectName("menuRemove_Songs")
        self.horizontalLayout_2.addWidget(self.menuRemove_Songs)
        self.menuAdd_Songs_2 = QtWidgets.QPushButton(self.frame_3)
        self.menuAdd_Songs_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuAdd_Songs_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("static/utils/images/Create.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAdd_Songs_2.setIcon(icon5)
        self.menuAdd_Songs_2.setIconSize(QtCore.QSize(24, 24))
        self.menuAdd_Songs_2.setFlat(True)
        self.menuAdd_Songs_2.setObjectName("menuAdd_Songs_2")
        self.horizontalLayout_2.addWidget(self.menuAdd_Songs_2)
        self.stoppushButton = QtWidgets.QPushButton(self.frame_3)
        self.stoppushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stoppushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("static/utils/images/Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stoppushButton.setIcon(icon6)
        self.stoppushButton.setIconSize(QtCore.QSize(24, 24))
        self.stoppushButton.setFlat(True)
        self.stoppushButton.setObjectName("stoppushButton")
        self.horizontalLayout_2.addWidget(self.stoppushButton)
        self.nextpushButton = QtWidgets.QPushButton(self.frame_3)
        self.nextpushButton.setMaximumSize(QtCore.QSize(250, 50))
        self.nextpushButton.setSizeIncrement(QtCore.QSize(250, 50))
        self.nextpushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextpushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("static/utils/images/Next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextpushButton.setIcon(icon7)
        self.nextpushButton.setIconSize(QtCore.QSize(24, 24))
        self.nextpushButton.setFlat(True)
        self.nextpushButton.setObjectName("nextpushButton")
        self.horizontalLayout_2.addWidget(self.nextpushButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.volumeSlider = QtWidgets.QSlider(self.menuAdd_Songs)
        self.volumeSlider.setMinimumSize(QtCore.QSize(250, 0))
        self.volumeSlider.setMaximumSize(QtCore.QSize(200, 30))
        self.volumeSlider.setSizeIncrement(QtCore.QSize(200, 30))
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
        self.verticalLayout_2.addWidget(self.volumeSlider, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        SimpleMusiPlayer.setCentralWidget(self.centralwidget)
        self.actionAdd_Songs = QtWidgets.QAction(SimpleMusiPlayer)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/img/images/Create.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Songs.setIcon(icon8)
        self.actionAdd_Songs.setObjectName("actionAdd_Songs")
        self.actionRemove_Selected = QtWidgets.QAction(SimpleMusiPlayer)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/img/images/Remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_Selected.setIcon(icon9)
        self.actionRemove_Selected.setObjectName("actionRemove_Selected")
        self.actionRemove_All = QtWidgets.QAction(SimpleMusiPlayer)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/img/images/Delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_All.setIcon(icon10)
        self.actionRemove_All.setObjectName("actionRemove_All")

        self.retranslateUi(SimpleMusiPlayer)
        QtCore.QMetaObject.connectSlotsByName(SimpleMusiPlayer)

    def retranslateUi(self, SimpleMusiPlayer):
        _translate = QtCore.QCoreApplication.translate
        SimpleMusiPlayer.setWindowTitle(_translate("SimpleMusiPlayer", "Andrew Music Player "))
        self.previouspushButton.setToolTip(_translate("SimpleMusiPlayer", "Previous"))
        self.playpushButton.setToolTip(_translate("SimpleMusiPlayer", "Play"))
        self.pausepushButton.setToolTip(_translate("SimpleMusiPlayer", "Pause/Unpause"))
        self.menuRemove_Songs.setToolTip(_translate("SimpleMusiPlayer", "Previous"))
        self.menuAdd_Songs_2.setToolTip(_translate("SimpleMusiPlayer", "Previous"))
        self.stoppushButton.setToolTip(_translate("SimpleMusiPlayer", "Stop"))
        self.nextpushButton.setToolTip(_translate("SimpleMusiPlayer", "Next"))
        self.actionAdd_Songs.setText(_translate("SimpleMusiPlayer", "Add Songs"))
        self.actionAdd_Songs.setToolTip(_translate("SimpleMusiPlayer", "Add songs to music player"))
        self.actionAdd_Songs.setShortcut(_translate("SimpleMusiPlayer", "Alt+A"))
        self.actionRemove_Selected.setText(_translate("SimpleMusiPlayer", "Remove Selected"))
        self.actionRemove_Selected.setToolTip(_translate("SimpleMusiPlayer", "Remove Selected Song"))
        self.actionRemove_Selected.setShortcut(_translate("SimpleMusiPlayer", "Del"))
        self.actionRemove_All.setText(_translate("SimpleMusiPlayer", "Remove All"))
        self.actionRemove_All.setToolTip(_translate("SimpleMusiPlayer", "Remove All Songs"))
        self.actionRemove_All.setShortcut(_translate("SimpleMusiPlayer", "Alt+Del"))
