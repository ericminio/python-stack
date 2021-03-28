import os
import logging
from flask import Flask, jsonify
from flask import send_from_directory, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from backend.migrations import migrate

def database_url():
    url = os.environ.get('DATABASE_URL').replace("postgres://", "postgresql://")
    logging.info("DATABASE_URL={url}".format(url = url))
    return url

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S %z'
)
logging.info("Starting...")
logging.info("PORT={value}".format(value=os.environ.get("PORT")))

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate(db)
logging.info("The database has been migrated")

@app.before_request
def before_request_func():
    logging.debug(request)

@app.route('/data')    
def data():
    value = { 'title':'hello world' }
    return jsonify(value)

@app.route('/users')    
def users():
    users = db.engine.execute('select id, username from foi_user order by username').fetchall()
    value = { 'entries': [ { 'id':user['id'], 'username':user['username'] } for user in users ] }
    return jsonify(value)

