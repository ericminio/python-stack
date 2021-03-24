from flask import current_app
import os

def migrate(db):
    files = [f for f in os.listdir('backend/migrations') if f.endswith('.sql')]
    for file in files:
        with open('backend/migrations/' + file) as f:
            sql = f.read()
            db.engine.execute(sql)
