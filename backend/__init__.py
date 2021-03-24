import os
from flask import Flask, jsonify
from flask import send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from backend.migrations import migrate

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dev:dev@host.docker.internal:2345/exploration'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate(db)

@app.route('/data')    
def data():
    value = { 'title':'hello world' }
    return jsonify(value)

@app.route('/users')    
def users():
    users = db.engine.execute('select id, username from foi_user order by username').fetchall()
    value = { 'entries': [ { 'id':user['id'], 'username':user['username'] } for user in users ] }
    return jsonify(value)

