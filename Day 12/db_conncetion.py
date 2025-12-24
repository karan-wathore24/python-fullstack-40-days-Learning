import sqlite3 as sq

def connect_db():
    return sq.connect("student.db")