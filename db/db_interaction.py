import sqlite3
from datetime import datetime


class DataBase:
    
    def __init__(self, db_file='/home/sebastjan/Documents/instaguiocrbot/instas.sqlite'):
        self.connect_sql(db_file)
        self.create_table()
    
    def connect_sql(self, db_file):
        # Connect to SQLite database (or create it if it doesn't exist)
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()
    
    def close_connection(self):
        self.conn.close()
    
    def create_table(self):
        # Create table
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS entries (
                username TEXT UNIQUE,
                date_added TIMESTAMP,
                followed_back  BOOLEAN
            )
        ''')
    
    def check_date_added(self, username):
        self.c.execute('''
            SELECT date_added FROM entries WHERE username = ?
        ''', (username,))
        result = self.c.fetchone()
        return result[0] if result else None

    # Function to add an entry
    def add_entry(self, username):
        try:
            self.c.execute('''
                INSERT INTO entries (username, date_added, followed_back) VALUES (?, ?, ?)
            ''', (username, datetime.now().timestamp(), False))
            self.conn.commit()
            print(f'"{username}" has been added to the database at {datetime.now().timestamp()}.')
        except sqlite3.IntegrityError:
            print(f'"{username}" is already in the database.')
            
    # Function to check if a user followed back
    def check_followed_back(self, username):
        self.c.execute('''
            SELECT followed_back FROM entries WHERE username = ?
        ''', (username,))
        result = self.c.fetchone()
        return result[0] if result else None
    
    # Function to update the followed_back field
    def update_followed_back(self, username, followed_back):
        self.c.execute('''
            UPDATE entries SET followed_back = ? WHERE username = ?
        ''', (followed_back, username))
        self.conn.commit()

    # Function to check if an entry exists
    def check_entry(self, username):
        self.c.execute('''
            SELECT * FROM entries WHERE username = ?
        ''', (username,))
        return bool(self.c.fetchone())

