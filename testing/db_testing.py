import unittest
import os
from datetime import datetime, timedelta
from db.db_interaction import DataBase


class TestDataBase(unittest.TestCase):

    def setUp(self):
        # Create a test database
        self.db = DataBase('test.db')

    def tearDown(self):
        # Delete the test database
        os.remove('test.db')

    def test_add_and_check_entry(self):
        self.db.add_entry('testuser')
        self.assertTrue(self.db.check_entry('testuser'))
        self.assertFalse(self.db.check_entry('nonexistentuser'))

    def test_check_date_added(self):
        now = datetime.now()
        self.db.add_entry('testuser')
        date_added = datetime.fromtimestamp(self.db.check_date_added('testuser'))
        print(type(date_added))
        self.assertTrue(now - timedelta(seconds=1) <= date_added <= now + timedelta(seconds=1))
        self.assertIsNone(self.db.check_date_added('nonexistentuser'))

    def test_check_and_update_followed_back(self):
        self.db.add_entry('testuser')
        self.assertFalse(self.db.check_followed_back('testuser'))
        self.db.update_followed_back('testuser', True)
        self.assertTrue(self.db.check_followed_back('testuser'))
        self.assertIsNone(self.db.check_followed_back('nonexistentuser'))


if __name__ == '__main__':
    unittest.main()
