from flask import current_app
import os

def migrate(db):
    print("migrating")
    files = [f for f in os.listdir('app/migrations') if f.endswith('.sql')]
    print(files)
    for file in files:
        with open('app/migrations/' + file) as f:
            sql = f.read()
            db.engine.execute(sql)
