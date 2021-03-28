from flask import current_app
import os
import logging

def migrate(db):
    logging.debug("Running migrations")
    candidates = os.listdir('backend/migrations')
    candidates.sort()
    files = [f for f in candidates if f.endswith('.sql')]
    for file in files:
        with open('backend/migrations/' + file) as f:
            logging.debug(f.name)
            sql = f.read()
            db.engine.execute(sql)
