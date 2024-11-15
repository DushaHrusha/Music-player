import glob
import os
import sqlite3
#https://pythonru.com/biblioteki/rabota-s-izobrazhenijami-i-fajlami-v-sqlite



class MusicDatabase:
    def __init__(self):
        self.list_music = ''
        self.list_musics = []
        self.db = sqlite3.connect('music.db')
        self.cursor = self.db.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS autors (
                id INTEGER PRIMARY KEY,
                name TEXT,
                genre TEXT
            ) """)

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS  musics (
                id INTEGER PRIMARY KEY,
                name TEXT,
                photo BLOB,
                file BLOB,
                autor_name TEXT, 
                FOREIGN KEY (autor_name)  REFERENCES autors (name)
             ) """)

        try:
            self.cursor.execute("INSERT INTO autors VALUES(1 ,'Oxxxymiron', 'Hip-Hop')")
            self.cursor.execute("INSERT INTO autors VALUES(2 ,'Markul', 'Hip-Hop')")
            self.cursor.execute("INSERT INTO autors VALUES(3 ,'Ram', 'Hip-Hop')")
            self.cursor.execute("INSERT INTO autors VALUES(4 ,'Booker', 'Hip-Hop')")
            self.cursor.execute("INSERT INTO autors VALUES(5 ,'Metalica', 'Rock')")
        except:
            pass

    def convert_to_binary_data(filename):
        # Преобразование данных в двоичный формат
        with open(filename, 'rb') as file:
            blob_data = file.read()
        return blob_data

    def insert_blob(self, id, name_music, name_author, photo, music_file):
        try:
            cursorDB = self.cursor
            print("Подключен к SQLite")

            sqlite_insert_blob_query = """INSERT INTO musics
                                      (id, name, photo, file, autor_name) VALUES (?, ?, ?, ?, ?)"""

            photo_bin = MusicDatabase.convert_to_binary_data(photo)
            music_bin = MusicDatabase.convert_to_binary_data(music_file)

            # Преобразование данных в формат кортежа
            data_tuple = (id, name_music, name_author, photo_bin, music_bin)
            cursorDB.execute(sqlite_insert_blob_query, data_tuple)
            self.db.commit()
            print("Изображение и файл успешно вставлены как BLOB в таблиу")
            #cursorDB.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if self.db:
                #db.close()
                print("Соединение с SQLite закрыто")


    def take_name_musics(self):
        temp_list = []
        self.cursor.execute("SELECT name FROM musics")
        rows = self.cursor.fetchall()
        for row in rows:
            temp_list.append(row[0])
            print(temp_list)
        return temp_list

    def write_to_file(self, data, filename, ):
        # Преобразование двоичных данных в нужный формат
        with open(filename, 'wb') as file:
            file.write(data)
            self.list_music = filename
        print("Данный из blob сохранены в: ", filename, "\n")
        return self.list_music

    def read_blob_data(self,name):
        try:
            cursorDB = self.cursor
            print("Подключен к SQLite")

            sql_fetch_blob_query = """SELECT * from musics where name = ?"""
            cursorDB.execute(sql_fetch_blob_query, (name,))
            record = cursorDB.fetchall()
            for row in record:


                print("Id = ", row[0], "NameMusic = ", row[1],  "nameAutor =", row[2])
                nameMusic  = row[1]
                photo = row[3]
                file = row[4]

                self.list_musics.append([row[1], row[2], row[3],row[4]])

                print("Сохранение изображения сотрудника и резюме на диске \n")
                photo_path = os.path.join(nameMusic + ".png")
                music_path = os.path.join(nameMusic + ".mp3")
                photopng = MusicDatabase.write_to_file(self, photo, photo_path)
                musicmp3 = MusicDatabase.write_to_file(self, file, music_path)
                return [music_path,photo_path]
            #cursorDB.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if self.db:
                #db.close()
                print("Соединение с SQLite закрыто")


    txtfiles = []
    for file in glob.glob("*.mp3"):
        txtfiles.append(file)
    print(txtfiles)





    #db.commit()



    #db.close()

