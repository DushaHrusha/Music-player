import os.path
import time
from logging import debug

from PyQt5 import QtMultimedia, QtGui
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtGui import QWindow
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import *
from sqlalchemy import false

from database_music import MusicDatabase, MusicContainer
from music import Ui_SimpleMusiPlayer


class Screen2():
    def __init__(self):
        super().__init__()
        self.window = QWindow()
        self.setupUi(self)

        self.playlistButton.clicked.connect(self.open_playlist)


class SimpleMusicPlayer(QMainWindow, Ui_SimpleMusiPlayer):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.setupUi(self)
        self.show()

        # Inits
        self.current_songs = []
        self.current_volume = 10

        global stopped
        stopped = False

        self.player = QtMultimedia.QMediaPlayer()
        self.player.setVolume(self.current_volume)

        # Slider Timer
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.move_slider)

        # Connections
        self.musicSlider.sliderMoved[int].connect(lambda: self.player.setPosition(self.musicSlider.value()))
        self.volumeSlider.sliderMoved[int].connect(lambda: self.volume_changed())
        self.actionAdd_Songs.triggered.connect(self.add_songs)
        self.actionRemove_Selected.triggered.connect(self.remove_one_song)
        self.actionRemove_All.triggered.connect(self.remove_all_songs)
        self.playpushButton.clicked.connect(self.play_song)
        self.pausepushButton.clicked.connect(self.pause_and_unpause)
        self.nextpushButton.clicked.connect(self.next_song)
        self.previouspushButton.clicked.connect(self.previous_song)
        self.stoppushButton.clicked.connect(self.stop_song)

        self.music = MusicDatabase()
        self.add_song( self.music.take_name_music())

    def move_slider(self):
        if stopped:
            return
        else:
            # Update the slider
            if self.player.state() == QMediaPlayer.PlayingState:
                self.musicSlider.setMinimum(0)
                self.musicSlider.setMaximum(self.player.duration())
                slider_position = self.player.position()
                self.musicSlider.setValue(slider_position)

                current_time = time.strftime('%H:%M:%S', time.localtime(self.player.position() / 1000))
                song_duration = time.strftime('%H:%M:%S', time.localtime(self.player.duration() / 1000))
                #self.start_time_label.setText(f"{current_time}")
                #self.end_time_label.setText(f"{song_duration}")

    def add_songs(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, caption='Add Songs',
            directory=':\\', filter="Supported Files (*.mp3;*.mpeg;*.ogg;*.m4a;*.MP3;*.wma;*.acc;*.amr)"
        )

        if files:
            for file in files:
                self.current_songs.append(file)
                self.listWidget.addItem(os.path.basename(file))

    def add_song(self, files):

        if files:
            for file in files:
                self.current_songs.append(file)
                self.listWidget.addItem(os.path.basename(file))

    def open_playlist(self):
        #if(self.listWidget.isEnabled()):
        self.listWidget.activateWindow()
        #else:

    def play_song(self):
        try:
            global stopped
            stopped = False
            print("____________________________",)

            current_selection = self.listWidget.currentRow()
            print("____________________________", )
            current_song = self.current_songs[current_selection]
            print("____________________________", current_song)

            MusicDatabase.read_blob_data(self.music, current_song)
            print("____________________________",current_song)
            song_url = QMediaContent(QUrl.fromLocalFile(current_song + ".mp3"))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()

            self.photo_music.setPixmap(QtGui.QPixmap(current_song + ".png"))
        except Exception as e:
            print(f"Play song error: {e}")

    def pause_and_unpause(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def next_song(self):
        try:
            current_selection = self.listWidget.currentRow()

            if current_selection + 1 == len(self.current_songs):
                next_index = 0
            else:
                next_index = current_selection + 1
            current_song = self.current_songs[next_index]
            self.listWidget.setCurrentRow(next_index)
            song_url = QMediaContent(QUrl.fromLocalFile(current_song))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()
        except Exception as e:
            print(f"Next song error: {e}")

    def previous_song(self):
        try:
            current_selection = self.listWidget.currentRow()

            if current_selection == 0:
                previous_index = len(self.current_songs) - 1
            else:
                previous_index = current_selection - 1

            current_song = self.current_songs[previous_index]
            self.listWidget.setCurrentRow(previous_index)
            song_url = QMediaContent(QUrl.fromLocalFile(current_song))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()
        except Exception as e:
            print(f"Previous song error: {e}")

    def stop_song(self):
        self.player.stop()
        self.musicSlider.setValue(0)
        self.start_time_label.setText(f"00:00:00")
        self.end_time_label.setText(f"00:00:00")

    def volume_changed(self):
        try:
            self.current_volume = self.volumeSlider.value()
            self.player.setVolume(self.current_volume)
            self.volume_label.setText(f"{self.current_volume}")
        except Exception as e:
            print(f"Changing volume error: {e}")

    def remove_one_song(self):
        current_selection = self.listWidget.currentRow()
        self.current_songs.pop(current_selection)
        self.listWidget.takeItem(current_selection)

    def remove_all_songs(self):
        self.stop_song()
        self.listWidget.clear()
        self.current_songs.clear()
