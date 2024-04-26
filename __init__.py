from flask import Flask
app = Flask(__name__)
import main

from flaskr import db
db.create_books_table()