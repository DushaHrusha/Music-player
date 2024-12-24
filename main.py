import os.path
import time
import eyed3

from PyQt5 import QtMultimedia, QtGui
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtGui import QWindow
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import *

from database_music import MusicDatabase
from music import Ui_SimpleMusiPlayer

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
        self.menuAdd_Songs_2.clicked.connect(self.add_songs)
        self.menuRemove_Songs.clicked.connect(self.remove_one_song)
        self.actionRemove_Selected.triggered.connect(self.remove_one_song)
        self.actionRemove_All.triggered.connect(self.remove_all_songs)
        self.playpushButton.clicked.connect(self.play_song)
        self.pausepushButton.clicked.connect(self.pause_and_unpause)
        self.nextpushButton.clicked.connect(self.next_song)
        self.previouspushButton.clicked.connect(self.previous_song)
        self.stoppushButton.clicked.connect(self.stop_song)

        self.music = MusicDatabase()
        self.music.insert_blob( 0, 'Мир Горит', 'Oxxxymiron', 'static/img/MusicCover/79a82ce939dbbbe836222cf2352c6e20.1000x1000x1.png','static/files/MusicServer/oxxxymiron-mir-gorit-mp3.mp3')
        self.music.insert_blob(1, 'In The End', 'Linkin Park', 'static/img/MusicCover/LinkinParkIntheEnd.jpg','static/files/MusicServer/linkin-park-in-the-end.mp3')
        #MusicDatabase.insert_blob(self.music, 2, 'Одинокий каннибал', 'Loqiemean ', 'MusicCover/ab67616d0000b273c525001ff36d4f0492b12ecc.jpg','static/files/MusicServer/loqiemean-odinokij-kannibal-mp3.mp3')
        #MusicDatabase.insert_blob(self.music, 3, 'Frau and Mann', 'Lindemann', 'MusicCover/sddefault.jpg','static/files/MusicServer/Lindemann - Frau and Mann.mp3')
        #MusicDatabase.insert_blob(self.music, 4, 'Сказки', 'Хаски', 'MusicCover/1200x1200bb.jpg','static/files/MusicServer/haski-skazki-mp3.mp3')
        #MusicDatabase.insert_blob(self.music, 5, 'Welcome To Brixton ', 'SR', 'MusicCover/artworks-pCZlcuZ3ZOYg-0-t500x500.jpg','static/files/MusicServer/SR - Welcome To Brixton.mp3')
        #MusicDatabase.insert_blob(self.music, 6, 'Красота и Уродство ', 'Linkin Park', 'MusicCover/Обложка_Красота_и_уродство.jpg','static/files/MusicServer/Oxxxymiron - Красота и Уродство.mp3')
        #MusicDatabase.insert_blob(self.music, 7, 'The Search', 'NF', 'MusicCover/ab67616d0000b273942a0c9ac8f1def7c8805044.jpg','static/files/MusicServer/NF - The Search - Edit.mp3')
        #MusicDatabase.insert_blob(self.music, 8, 'Кукла колдуна ', 'Король и Шут ', 'MusicCover/72b8e793ae6943cdf5aaa0f198a31118.1000x1000x1.png','static/files/MusicServer/Король и Шут - Кукла колдуна (OST Король и Шут).mp3')
        #MusicDatabase.insert_blob(self.music, 9, 'Hotline', 'Kaito Shoma', 'MusicCover/artworks-Th4EWoYzpvwZyFfz-vILRGg-t1080x1080.jpg','static/files/MusicServer/Kaito Shoma - HOTLINE.DEATH WISH.mp3')
        #MusicDatabase.insert_blob(self.music, 10, 'Гитлер живёт в Антарктиде ', 'Б.А.У.', 'MusicCover/ab67616d0000b27306d510fc5f9fcee6840a40af.jpg','static/files/MusicServer/Bezdna_Analnogo_Ugneteniya_-_Gitler_zhivyot_v_Antarktide_(Bib.fm).mp3')

        self.add_song()
        self.add_songs()
        self.id_next = MusicDatabase.check_id_music(self.music)

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

    def add_songs(self):
        self.id_next = MusicDatabase.check_id_music(self.music)
        files, _ = QFileDialog.getOpenFileNames(
            self, caption='Add Songs',
            directory=':\\', filter="Supported Files (*.mp3;*.mpeg;*.ogg;*.m4a;*.MP3;*.wma;*.acc;*.amr)"
        )
        if files:
            for file in files:
                print(file)
                audiofile = eyed3.load(file)
                if (audiofile.tag == None):
                    audiofile.initTag()

                if audiofile.tag is not None and audiofile.tag.artist:
                    artist = audiofile.tag.artist
                else:
                    parts = [part.strip() for part in os.path.basename(file).split('-')]
                    if len(parts) == 2:
                        artist = parts[0]
                        print("Первая часть:", parts[0])
                    else:
                        print("Строка не содержит символа '-' или содержит больше одного символа '-'")
                        artist = os.path.basename(file)

                if audiofile.tag is not None and audiofile.tag.title:
                    title = audiofile.tag.title
                else:
                    parts = [part.strip() for part in os.path.basename(file).split('-')]
                    if len(parts) == 2:
                        title = parts[1]
                        if title.endswith(".mp3"):
                            title = title[:-4]  # Убираем последние 4 символа
                        else:
                            title = title
                        print("Первая часть:", parts[1])
                    else:
                        print("Строка не содержит символа '-' или содержит больше одного символа '-'")
                        title = os.path.basename(file)

                images = audiofile.tag.images
                image_path = ''
                if audiofile.tag is not None and audiofile.tag.images:
                    for image in audiofile.tag.images:
                        image_data = image.image_data
                        cover_image_path = title + ".png"
                        image_path = cover_image_path
                        with open(cover_image_path, "wb") as img_file:
                            img_file.write(image_data)
                        break
                    try:
                        MusicDatabase.insert_blob(self.music, self.id_next, title, artist, image_path, file)
                        self.listWidget.addItem(title)
                        self.current_songs.append(MusicDatabase.read_blob_data(self.music, title))
                    except Exception as e:
                        print(f"Музыка не добавилась: {e}")
                else:
                    print("Обложка не найдена.")
                    try:
                        if audiofile.tag.title is None:
                            print(artist)
                            MusicDatabase.insert_blob(self.music, self.id_next, title, artist , ".png", file)
                            self.listWidget.addItem(title)
                            self.current_songs.append(MusicDatabase.read_blob_data(self.music, title))
                    except Exception as e:
                        print(f"Музыка не добавилась: {e}")

    def add_song(self):
        for music_name in self.music.take_name_musics():
            print(music_name)
            self.listWidget.addItem(os.path.basename(music_name))
            self.current_songs.append(MusicDatabase.read_blob_data(self.music, music_name))

    def open_playlist(self):
        #if(self.listWidget.isEnabled()):
        self.listWidget.activateWindow()
        #else:

    def play_song(self):
        try:
            global stopped
            stopped = False

            current_selection = self.listWidget.currentRow()
            current_song = self.current_songs[current_selection]
            song_url = QMediaContent(QUrl.fromLocalFile(current_song[0]))
            self.player.setMedia(song_url)
            self.player.play()
            self.move_slider()

            self.photo_music.setPixmap(QtGui.QPixmap(current_song[1]))
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
            #self.volume_label.setText(f"{self.current_volume}")
        except Exception as e:
            print(f"Changing volume error: {e}")

    def remove_one_song(self):
        try:
            current_selection = self.listWidget.currentRow()
            self.current_songs.pop(current_selection)
            self.listWidget.takeItem(current_selection)
            current_song = self.current_songs[current_selection]
            print(current_song[0])
            MusicDatabase.remove_song(self.music, current_song[0])
        except Exception as e:

            print(f"An error occurred: {str(e)}")



    def remove_all_songs(self):
        self.stop_song()
        self.listWidget.clear()
        self.current_songs.clear()
