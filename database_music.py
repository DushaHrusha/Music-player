import glob
import sqlite3
#https://pythonru.com/biblioteki/rabota-s-izobrazhenijami-i-fajlami-v-sqlite

db = sqlite3.connect('music.db')

cursor = db.cursor()

cursor.execute("""CREATE TABLE autors (
    id INTEGER PRIMARY KEY,
    name TEXT,
    genre TEXT
) """)

cursor.execute("""CREATE TABLE musics (
    id INTEGER PRIMARY KEY,
    name TEXT,
    photo BLOB,
    file BLOB,
    autors_id INTEGER, 
    FOREIGN KEY (autors_id)  REFERENCES autors (id)
 ) """)

cursor.execute("INSERT INTO autors VALUES(1 ,'Oxxxymiron', 'Hip-Hop')")
cursor.execute("INSERT INTO autors VALUES(2 ,'Markul', 'Hip-Hop')")
cursor.execute("INSERT INTO autors VALUES(3 ,'Ram', 'Hip-Hop')")
cursor.execute("INSERT INTO autors VALUES(4 ,'Booker', 'Hip-Hop')")
cursor.execute("INSERT INTO autors VALUES(5 ,'Metalica', 'Rock')")



def convert_to_binary_data(filename):
    # Преобразование данных в двоичный формат
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def insert_blob(autor_id, name, photo, resume_file):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursorDB = cursor

        print("Подключен к SQLite")

        sqlite_insert_blob_query = """INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)"""

        emp_photo = convert_to_binary_data(photo)
        resume = convert_to_binary_data(resume_file)
        # Преобразование данных в формат кортежа
        data_tuple = (autor_id, name, emp_photo, resume)
        cursorDB.execute(sqlite_insert_blob_query, data_tuple)
        sqlite_connection.commit()
        print("Изображение и файл успешно вставлены как BLOB в таблиу")
        cursorDB.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")



import sqlite3, os

def write_to_file(data, filename):
    # Преобразование двоичных данных в нужный формат
    with open(filename, 'wb') as file:
        file.write(data)
    print("Данный из blob сохранены в: ", filename, "\n")

def read_blob_data(emp_id):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[2]
            resume_file = row[3]

            print("Сохранение изображения сотрудника и резюме на диске \n")
            photo_path = os.path.join("db_data", name + ".jpg")
            resume_path = os.path.join("db_data", name + "_resume.txt")
            write_to_file(photo, photo_path)
            write_to_file(resume_file, resume_path)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


txtfiles = []
for file in glob.glob("*.mp3"):
    txtfiles.append(file)
print(txtfiles)






cursor.execute("SELECT * FROM autors")
print(cursor.fetchall())


db.commit()



db.close()