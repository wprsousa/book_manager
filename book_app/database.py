import sqlite3
import requests
from book_app.config.config import API_KEY


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


def find_book_info_by_isbn(isbn):
    conn = sqlite3.connect('bookshelf.sqlite3')
    cursor = conn.cursor()

    api_key = API_KEY
    base_url = 'https://www.googleapis.com/books/v1/volumes'

    params = {
        'q': f'isbn:{isbn}',
        'key': api_key
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if 'items' in data and len(data['items']) > 0:
            book_info = data['items'][0]['volumeInfo']
            title = book_info.get('title', 'Book not found')
            authors = book_info.get('authors', ['Author not found'])

            insert_command = "INSERT INTO books (title, author) VALUES (?, ?)"

            cursor.execute(insert_command, (book_info['title'], ', '.join(book_info['authors'])))

            conn.commit()
            conn.close()

            return {
                'title': title,
                'authors': authors
            }

        return {
            'title': 'Book not found',
            'authors': ['Author not found']
        }

    except Exception as e:
        print(f"Request error: {e}")
    return {
        'title': 'Request error',
        'authors': []
    }


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
