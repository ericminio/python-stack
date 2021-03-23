import os
from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)
    
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')    
def data():
    value = { 'title':'hello world' }
    return jsonify(value)


  