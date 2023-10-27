import unittest
import sqlite3
from book_app.database import create_database


class TestCreateDatabase(unittest.TestCase):

    def setUp(self):
        # Connect to a test database (use an in-memory database)
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

    def test_create_database(self):
        # Execute the create_database function
        create_database()

        self.conn = sqlite3.connect('bookshelf.sqlite3')
        self.cursor = self.conn.cursor()
        # Check if the "books" table was created
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books'")
        table_exists = self.cursor.fetchone()
        self.assertIsNotNone(table_exists, "The 'books' table was not created.")

    def tearDown(self):
        # Close the test connection
        self.conn.close()


if __name__ == '__main__':
    unittest.main()
