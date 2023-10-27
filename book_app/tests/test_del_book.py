import unittest
import sqlite3
from book_app.database import add_book, del_book


class TestDelBook(unittest.TestCase):

    def setUp(self):
        # Connect to a test database (use an in-memory database)
        self.conn = sqlite3.connect('bookshelf.sqlite3')
        self.cursor = self.conn.cursor()

    def test_del_book(self):
        # Execute the add_book function
        new_title = "Test Book"
        new_author = "Test Author"
        add_book(new_title, new_author)
        # Check if the book was inserted into the table
        self.cursor.execute("SELECT title, author FROM books where title = ? AND author = ?", (new_title, new_author))
        book = self.cursor.fetchall()
        self.assertIsNotNone(book, "The book was not inserted correctly into the 'books' table.")

        # Execute the function del_book
        del_book(new_title)

        # Check if the book was deleted
        self.cursor.execute("SELECT title FROM books where title = ?", (new_title,))
        book = self.cursor.fetchall()
        self.assertEqual(book, [], "The book was deleted correctly from the 'books' table.")

    def tearDown(self):
        self.conn.close()


if __name__ == '__main__':
    unittest.main()
