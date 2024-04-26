import sqlite3

DATABASE = 'database.db'

def create_books_table():
    con = sqlite3.connect(DATABASE)
    cursor = con.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='books';")
    if not cursor.fetchone():
        con.execute('CREATE TABLE books (title TEXT, price REAL, arrival_day TEXT)')
    con.close()