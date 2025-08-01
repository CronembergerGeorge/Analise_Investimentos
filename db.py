import sqlite3

def connection():
    return sqlite3.connect('data/investimentos.db', timeout=10)