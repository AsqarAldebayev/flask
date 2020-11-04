import sqlite3
import os
from flask import Flask, render_template, request

# конфигурация
DATABASE = '/tmp/flbase.db'
DEBUG = True
SECRET_KEY = 'dsf7gd987shhdf#@sjkgddg,dfsgd9'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flbase.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    """Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())

    db.commit()
    db.close()


# if __name__ == "__main__":
#     app.run(debug=True)