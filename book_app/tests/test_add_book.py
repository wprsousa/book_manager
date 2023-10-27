import unittest
import sqlite3
from book_app.database import add_book, create_database


class TestAddBook(unittest.TestCase):

    def setUp(self):
        # Connect to a test database (use an in-memory database)
        self.conn = sqlite3.connect('bookshelf.sqlite3')
        self.cursor = self.conn.cursor()

    def test_add_book(self):
        # Execute the create_database function
        create_database()

        # Execute the add_book function
        new_title = "Test Book"
        new_author = "Test Author"
        add_book(new_title, new_author)

        # Check if the book was inserted into the table
        self.cursor.execute("SELECT title, author FROM books where title = ? AND author = ?", (new_title, new_author))
        book = self.cursor.fetchall()
        self.assertIsNotNone(book, "The book was not inserted correctly into the 'books' table.")

    def tearDown(self):
        # Close the test connection
        self.conn.close()


if __name__ == '__main__':
    unittest.main()
