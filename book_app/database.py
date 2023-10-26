import sqlite3


def create_database():
    conn = sqlite3.connect('bookshelf.sqlite3')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT
    )
''')

    conn.commit()
    conn.close()


def add_book(new_title, new_author):
    conn = sqlite3.connect('bookshelf.sqlite3')
    cursor = conn.cursor()

    insert_command = "INSERT INTO books (title, author) VALUES (?, ?)"

    cursor.execute(insert_command, (new_title, new_author))

    conn.commit()
    conn.close()


def del_book(title):
    conn = sqlite3.connect('bookshelf.sqlite3')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books where title = ?", (title,))

    conn.commit()
    conn.close()


def list_book():
    conn = sqlite3.connect('bookshelf.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT title, author FROM books")

    books = cursor.fetchall()

    if books:
        for book in books:
            print("Title:", book[0])
            print("Author:", book[1])
            print("------")
    else:
        print("There's no books in the bookshelf")

    conn.close()
