import sqlite3


connection = sqlite3.connect("notes.db")
cursor = connection.cursor()


def all_notes():
    with connection: # ����� �������� ���� �������
        return cursor.execute("SELECT name FROM note").fetchall()


def note(name):
    with connection:
        # ����� ���������� ������� � ������������ ������
        return cursor.execute("SELECT text FROM note WHERE name=?", (name,)).fetchone()


def search_note():
    with connection:
        # ����� ��� ���������� �� ��
        return cursor.execute("SELECT * FROM note").fetchall()


def delete_note(name):
    with connection:
        # ������� ������� � ������������ ������
        return cursor.execute("DELETE FROM note WHERE name=?", (name,)).fetchone()


def add_note(name, text):
    with connection:
        # ��������� ������� � ��
        cursor.execute("INSERT INTO note (name, text) VALUES (?, ?)", (name, text,))
        connection.commit()