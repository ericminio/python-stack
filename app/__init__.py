import os
from flask import Flask, jsonify
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from app.migrations import migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dev:dev@host.docker.internal:2345/exploration'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate(db)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')    
def data():
    value = { 'title':'hello world' }
    return jsonify(value)

@app.route('/users')    
def users():
    users = db.engine.execute('select username from foi_user').fetchall()
    value = { 'data': [ user['username'] for user in users ] }
    return jsonify(value)

