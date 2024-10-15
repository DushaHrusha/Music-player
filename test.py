import sqlite3
import sys
from bitstring import BitArray

conn = sqlite3.connect('audio.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS AUDIO")

# Creating table as per requirement
sql = "CREATE TABLE audio_table (id, name TEXT NOT NULL, audio BLOB NOT NULL, resume BLOB NOT NULL);"
#cursor.execute(sql)
print("Table created successfully.....")


def insert_blob(emp_id, name, audio, resume_file):
    try:
        sqlite_connection = sqlite3.connect('audio.db')
        cursor = sqlite_connection.cursor()
        print("Connected to SQLite")
        sqlite_query = "INSERT INTO audio_table (id, name, audio, resume) VALUES (?, ?, ?, ?)"
        emp_audio = BitArray(audio)
        resume = BitArray(resume_file)
        # Convert data into tuple format
        data_tuple = (emp_id, name, emp_audio, resume)
        cursor.execute(sqlite_query, data_tuple)
        sqlite_connection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print(f"Failed to insert blob data into sqlite table {error}")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The sqlite connection is closed")


if __name__ == '__main__':
    insert_blob(1, "Adele - Set Fire To The Rain", "Adele - Set Fire To The Rain.mp3",
                "Adele - Set Fire To The Rain.txt")
    insert_blob(2, "Clean Bandit", "Clean Bandit.mp3", "Clean Bandit.txt")


def write_file(data, filename):
    '''Convert binary data and write it on Hard Disk'''
    with open(filename, 'wb') as file:
        file.write(data)
    print(f"Stored blob data into:{filename}\n")


def read_blob(emp_id, audio_path, describe_path):
    try:
        sqlite_con = sqlite3.connect('audio.db')
        cursor = sqlite_con.cursor()
        print("Connected to SQLite")
        sql_blob_query = "SELECT * from audio_table where id = ?"
        cursor.execute(sql_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            name = row[1]
            photo = row[2]
            resumeFile = row[3]
            print("Storing employee image and resume on disk \n")

            audio = f"{audio_path}{name}.mp3"
            describe = f"{describe_path}{name}.txt"
            write_file(photo, audio)
            write_file(resumeFile, describe)
        cursor.close()

    except sqlite3.Error as error:
        print(f"Failed to read blob data from sqlite table {error}")
    finally:
        if sqlite_con:
            sqlite_con.close()
            print("sqlite connection is closed")


if __name__ == '__main__':
    audio_path = "G:/div_code/audio_env/from_db/"
    describe_path = "G:/div_code/audio_env/from_db/"
    read_blob(1, audio_path, describe_path)
    read_blob(2, audio_path, describe_path)